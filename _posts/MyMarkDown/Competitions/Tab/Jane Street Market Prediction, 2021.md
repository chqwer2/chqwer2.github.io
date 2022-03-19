# Jane Street Market Prediction, 2021

### Content

Code: https://www.kaggle.com/gogo827jz/jane-street-supervised-autoencoder-mlp?scriptVersionId=73762661

Code base: https://www.kaggle.com/aimind/bottleneck-encoder-mlp-keras-tuner-8601c5

Model: MLP + XGBoost

<img src="https://chqwer2.github.io/img/Typora/image-20211013084231915.png" alt="image-20211013084231915" style="zoom:50%;" />



### Training

Supervised autoencoder is trained separately before cross-validation (CV) split lead to → label leaking?

Instead train the supervised autoencoder along with MLP in one model in each CV split. 

weight average:

https://www.sciencedirect.com/science/article/abs/pii/S0925231213000209?via%3Dihub

```
# weighted average as per Donate et al.'s formula
# https://doi.org/10.1016/j.neucom.2012.02.053
# [0.0625, 0.0625, 0.125, 0.25, 0.5] for 5 fold
```

Feature Engineering:

1. 5-fold 31-gap purged group time-series split
2. Remove first 85 days for training
3. Forward-fill missing
4. Transfer all resp targets (resp0~4) to action for multi-label classification
5. Use the mean of the absolute values of all resp targets as sample weights for training so that the model can focus on capturing samples with large absolute resp.
6. During inference, the mean of all predicted actions is taken as the final probability

AE to create new features, concatenate with original features to the downstream MLP (BN+Dropout)

Train AE and MLP together in each CV split

Add target info to AE to force it to generate relevent features and create shortcut for backpropogation of gradient

Add Gaussian noise layer before encoder for DA and preventing overfitting

Use swish to prevent 'dead neuron'

3 model with diff seeds and average to reduce prediction variance

Only BCE for early stopping + Hyperopt



```python
def create_ae_mlp(num_columns, num_labels, hidden_units, dropout_rates, ls = 1e-2, lr = 1e-3):
    
    inp = tf.keras.layers.Input(shape = (num_columns, ))
    x0 = tf.keras.layers.BatchNormalization()(inp)
    
    encoder = tf.keras.layers.GaussianNoise(dropout_rates[0])(x0)
    encoder = tf.keras.layers.Dense(hidden_units[0])(encoder)
    encoder = tf.keras.layers.BatchNormalization()(encoder)
    encoder = tf.keras.layers.Activation('swish')(encoder)
    
    decoder = tf.keras.layers.Dropout(dropout_rates[1])(encoder)
    decoder = tf.keras.layers.Dense(num_columns, name = 'decoder')(decoder)

    x_ae = tf.keras.layers.Dense(hidden_units[1])(decoder)
    x_ae = tf.keras.layers.BatchNormalization()(x_ae)
    x_ae = tf.keras.layers.Activation('swish')(x_ae)
    x_ae = tf.keras.layers.Dropout(dropout_rates[2])(x_ae)

    out_ae = tf.keras.layers.Dense(num_labels, activation = 'sigmoid', name = 'ae_action')(x_ae)
    
    x = tf.keras.layers.Concatenate()([x0, encoder])
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dropout(dropout_rates[3])(x)
    
    for i in range(2, len(hidden_units)):
        x = tf.keras.layers.Dense(hidden_units[i])(x)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Activation('swish')(x)
        x = tf.keras.layers.Dropout(dropout_rates[i + 2])(x)
        
    out = tf.keras.layers.Dense(num_labels, activation = 'sigmoid', name = 'action')(x)
    
    model = tf.keras.models.Model(inputs = inp, outputs = [decoder, out_ae, out])
    model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = lr),
                  loss = {'decoder': tf.keras.losses.MeanSquaredError(), 
                          'ae_action': tf.keras.losses.BinaryCrossentropy(label_smoothing = ls),
                          'action': tf.keras.losses.BinaryCrossentropy(label_smoothing = ls), 
                         },
                  metrics = {'decoder': tf.keras.metrics.MeanAbsoluteError(name = 'MAE'), 
                             'ae_action': tf.keras.metrics.AUC(name = 'AUC'), 
                             'action': tf.keras.metrics.AUC(name = 'AUC'), 
                            }, 
                 )
    
    return model
```

```python
if not TEST:
    scores = []
    batch_size = 4096
    gkf = PurgedGroupTimeSeriesSplit(n_splits = n_splits, group_gap = group_gap)
    for fold, (tr, te) in enumerate(gkf.split(train['action'].values, train['action'].values, train['date'].values)):
        ckp_path = f'JSModel_{fold}.hdf5'
        model = create_ae_mlp(**params)
        ckp = ModelCheckpoint(ckp_path, monitor = 'val_action_AUC', verbose = 0, 
                              save_best_only = True, save_weights_only = True, mode = 'max')
        es = EarlyStopping(monitor = 'val_action_AUC', min_delta = 1e-4, patience = 10, mode = 'max', 
                           baseline = None, restore_best_weights = True, verbose = 0)
        history = model.fit(X[tr], [X[tr], y[tr], y[tr]], validation_data = (X[te], [X[te], y[te], y[te]]), 
                            sample_weight = sw[tr], 
                            epochs = 100, batch_size = batch_size, callbacks = [ckp, es], verbose = 0)
        hist = pd.DataFrame(history.history)
        score = hist['val_action_AUC'].max()
        print(f'Fold {fold} ROC AUC:\t', score)
        scores.append(score)

        K.clear_session()
        del model
        rubbish = gc.collect()
    
    print('Weighted Average CV Score:', weighted_average(scores))
```



