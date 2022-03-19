### 1st Solution

[[notebook]](https://www.kaggle.com/nyanpn/1st-place-public-2nd-place-solution?scriptVersionId=85907908), [[Discussion]](https://www.kaggle.com/c/optiver-realized-volatility-prediction/discussion/274970)

LightGBM + CNN + MLP

My final submission was an ensemble of 5xLightGBM, 3x1D CNN, and 3xMLP



### 3rd Solution

[[discussion]](https://www.kaggle.com/c/optiver-realized-volatility-prediction/discussion/278588), [[notebook]](https://www.kaggle.com/eduardopeynetti/third-place-solution?scriptVersionId=84913897)







### Public 1398th → Private 24th Solution

Final submission code is [here](https://www.kaggle.com/shigeria/optiver-lgbm-tabnet-nn).

#### Features

We added some features used in the following Notebooks.
 https://www.kaggle.com/tommy1028/lightgbm-starter-with-feature-engineering-idea
 https://www.kaggle.com/denisvodchyts/lgbm-slightly-different-features
 https://www.kaggle.com/alexioslyon/lgbm-baseline

#### Validation

We used group kfold by stock id, 

In NN, group kfold was based on knn algorithms 

and in Tabnet and LGBM, We just used sklearn group kfold.



```
x = keras.layers.Embedding(max(cat_data)+1, 
			stock_embedding_size, 
            input_length=1, name='stock_embedding')(stock_id_input)
```

```
x = keras.layers.Bidirectional(
tf.compat.v1.keras.layers.CuDNNLSTM(256, return_sequences=True))(x)
x = keras.layers.Bidirectional(
tf.compat.v1.keras.layers.CuDNNGRU(128, return_sequences=True))(x)
```

```
avg_pool = keras.layers.GlobalAveragePooling1D()(x)
max_pool = keras.layers.GlobalMaxPooling1D()(x)
conc = keras.layers.concatenate([avg_pool, max_pool])
out = keras.layers.Flatten()(conc)
for n_hidden in hidden_units:
        out = keras.layers.Dense(n_hidden, activation='swish')(out)
```

We ensembled NN * 0.4 + Tabnet * 0.4 + LGBM * 0.2





