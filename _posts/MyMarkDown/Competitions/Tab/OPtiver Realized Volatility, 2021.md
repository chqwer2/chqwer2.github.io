# OPtiver Realized Volatility, 2021

## Data Leak

1. Recovering the actual price from the "tick_size" leak
2. Reverse-engineering time-id order
3. Using future information for features or models

## 2nd Place Solution - Nearest Neighbors

Web: https://www.kaggle.com/c/optiver-realized-volatility-prediction/discussion/274970

Blend of LightGBM, 1D-CNN, and MLP

The 1D-CNN is a simplified version of the architecture used in MoA 2nd  place solution. (This CNN worked surprisingly well in both the recent  MLB and Optiver competition.)

- Time-series cross-validation by reverse engineering of time-id order
- Nearest neighbor aggregation features (boost from 0.21 to 0.19)
- Blend of LightGBM, MLP, and MoA’s 1D-CNN

You can also see my notebook here:
https://www.kaggle.com/nyanpn/public-2nd-place-solution

### Reverse engineering of time-id order

The prices in the competition data are normalized, but as someone pointed  out in the discussion, you can use "tick size" to recover the real  prices before normalization.

Furthermore, by compressing the **time-id x stock-id price** matrix to one dimension using t-SNE, I was able to recover the order of the time-id with sufficient accuracy.

The correctness of the recovery of the time-id order for the training data  can be easily verified by comparing it with the real market data. By  doing so, we know that the training data is for the period between **2020/1/1~2021/3/31**.

- **Time series cross-validation**. Now that we know the correct order of the timestamps, we can construct  the validation sets as if they were normal time-series data.
- **Detection of covariate shifts**. Using methods such as **adversarial validation** enables us to find features that change over time.
- **Data exclusion**. I didn't do this because it didn't work for me, but we can exclude  periods of specific market events from our data, for example, the stock  market crash in early 2020.

Time series CV was especially important. I used a 4-fold **time-series CV**, with 10% of
data used for validation for each fold. This allowed me to get a good enough (though not perfect) correlation between CV and LB throughout the  competition.



The order of test set cannot be directed used. However, even if it cannot  be used directly for features, the order of the time-id can be used in  various ways.

> ```
> import glob
> 
> import numpy as np
> import pandas as pd
> from joblib import Parallel, delayed
> from sklearn.manifold import TSNE
> from sklearn.preprocessing import minmax_scale
> 
> 
> def calc_price_from_tick(df):
>     tick = sorted(np.diff(sorted(np.unique(df.values.flatten()))))[0]
>     return 0.01 / tick
> 
> 
> def calc_prices(r):
>     df = pd.read_parquet(r.book_path,
>                          columns=[
>                              'time_id',
>                              'ask_price1',
>                              'ask_price2',
>                              'bid_price1',
>                              'bid_price2'
>                          ])
>     df = df.groupby('time_id') \
>         .apply(calc_price_from_tick).to_frame('price').reset_index()
>     df['stock_id'] = r.stock_id
>     return df
> 
> 
> def reconstruct_time_id_order():
>     paths = glob.glob('/kaggle/input/optiver-realized-volatility-prediction/book_train.parquet/**/*.parquet')
> 
>     df_files = pd.DataFrame(
>         {'book_path': paths}) \
>         .eval('stock_id = book_path.str.extract("stock_id=(\d+)").astype("int")',
>               engine='python')
> 
>     # build price matrix using tick-size
>     df_prices = pd.concat(
>         Parallel(n_jobs=4)(
>             delayed(calc_prices)(r) for _, r in df_files.iterrows()
>         )
>     )
>     df_prices = df_prices.pivot('time_id', 'stock_id', 'price')
> 
>     # t-SNE to recovering time-id order
>     clf = TSNE(
>         n_components=1,
>         perplexity=400,
>         random_state=0,
>         n_iter=2000
>     )
>     compressed = clf.fit_transform(
>         pd.DataFrame(minmax_scale(df_prices.fillna(df_prices.mean())))
>     )
> 
>     order = np.argsort(compressed[:, 0])
>     ordered = df_prices.reindex(order).reset_index(drop=True)
> 
>     # correct direction of time-id order using known stock (id61 = AMZN)
>     if ordered[61].iloc[0] > ordered[61].iloc[-1]:
>         ordered = ordered.reindex(ordered.index[::-1])\
>             .reset_index(drop=True)
> 
>     return ordered[['time_id']]
> ```





### How is the data being generated?

### Feature engineering

predict the next 10 minutes of realized volatility (RV) from the previous 10  minutes of data, the most important feature would obviously be the **RV of the previous 10 minutes.**

we can expect the RV at the next time-id to be a very powerful feature.

If we generalize further, we can improve the prediction accuracy by using  not only the next time-id, but also the information of time-ids that are "similar" in some distance metric. For example, the RV of the same  stock when the market had similar price, volatility, and trading volume  would be useful for predicting the RV at a certain time-id.

So, I used **NearestNeighbor** with various distance metrics to find the similar N time-ids and  calculate the average of features like RV and stock size  (N=2,3,5,10,20,40).

In addition to the time-id, I also calculated  the aggregation between similar stock-ids. Furthermore, by combining  these ideas, I calculated features such as "the average tau of 20  similar stocks with similar volatility in 5 closest time-ids".

> ```
> target_feature = 'book.log_return1.realized_volatility'
> n_max = 40
> 
> # make neighbors
> pivot = df.pivot('time_id', 'stock_id', 'price')
> pivot = pivot.fillna(pivot.mean())
> pivot = pd.DataFrame(minmax_scale(pivot))
> 
> nn = NearestNeighbors(n_neighbors=n_max, p=1)
> nn.fit(pivot)
> neighbors = nn.kneighbors(pivot)
> 
> # aggregate
> 
> def make_nn_feature(df, neighbors, f_col, n=5, agg=np.mean, postfix=''):
>     pivot_aggs = pd.DataFrame(agg(neighbors[1:n,:,:], axis=0), 
>                               columns=feature_pivot.columns, 
>                               index=feature_pivot.index)
>     dst = pivot_aggs.unstack().reset_index()
>     dst.columns = ['stock_id', 'time_id', f'{f_col}_cluster{n}{postfix}_{agg.__name__}']
>     return dst
> 
> feature_pivot = df.pivot('time_id', 'stock_id', target_feature)
> feature_pivot = feature_pivot.fillna(feature_pivot.mean())
> 
> neighbor_features = np.zeros((n_max, *feature_pivot.shape))
> 
> for i in range(n):
>     neighbor_features[i, :, :] += feature_pivot.values[neighbors[:, i], :]
> 
> for n in [2, 3, 5, 10, 20, 40]:
>     dst = make_nn_feature(df, neighbors, feature_pivot, n)
>     df = pd.merge(df, dst, on=['stock_id', 'time_id'], how='left')
> ```

using Nearest Neighbor to aggregate nearby features can probably be used in a real model.

## Feature processing

Now that we know the order of the time-id, we can detect features that are  changing over time. By performing adversarial validation, I noticed that the features aggregated from `trade.order_count` and `book.total_volume` changed remarkably over time. Therefore, instead of using their raw features, **I converted these features into ranks within the same time-id.**

I also applied `np.log1p` to features that have large skew, as they may degrade the predictions if large outliers come during the 2nd stage.

These have little improvement on the LB scores, but I believe they help to reduce the risk of shakedown in private LB.

### **GNN short solution LB=0.18345**

https://www.kaggle.com/max2020/0928-trans-5-topn-2

graphsage+5 neighbors=0.187xx

transformerConv+5 neighbors = 0.186xx

transformerConv+3 neighbors=0.185xx

transformerConv+3 neighbors+5 random number seeds=0.1843 A

transformerConv + 2 neighbors + 5 random number seeds = 0.1840 B

A+B=0.18345

**Have not time to**:

- Ensembles with LSTMs and RNNs that do not create features
- Auto-encoder
- 300-sec model (split the training data into the first and second halves, and  create a model that predicts the RV of the second half from the first  half and use it as meta-feature or data augmentation)

**Work tried but not work:**

**Yirun Zhang**

Feature Engineering:

1. Advanced Realized Volatility and Quarticity features
2. KMeans + PCA features
3. Microstructural features for HFT such as Volume synchronized probability of informed  trading, Hasbrouck's flow, Hasbrouck's lands, Amihuds Lamda, Kyle’s  Lamda, Becker Parkinson volatility, Corwin Shultz spread, etc.
4. Median, Median Absolute Deviation, Entropy, skewness, kurtosis of original features
5. Ranking features in each time id
6. Exponential decay RV
7. RV feature calculated by optimising the number of seconds in the bucket  (or percentage of length) considered for calculating the RV value for  each stock

Modelling:

1. Stacking
2. Tabular Transformer Autoencoder + NN/Ridge Regression
3. AE-MLP, ResDTNet, NODE, GrowNet, and lots of fancy NN model architectures
4. RNN, CNN, Transformer models on time-span aggregated features or raw book features (special case)
5. Training separate model for each stock id
6. SVM, KNN, XGB, HGB (Sklearn)
7. Post-processing by shifting mean and std of prediction
8. Removing outlier time_ids by isolation forest trained on the feature importance of each time id
9. Adding Dropout or Gaussian noise after the input layer of NN

**Mingjie Wang:**
Feature Engineering:

1. Second-order features. For important features, cross-construct feature engineering  again. For example, dot product, Euclidean distance etc
2. Sampling, id 31
3. Random initialization. Randomly delete some features in batch.

Modelling：

1. R-DROP
2. SimCSE
3. Mutil attention module, such as self-attention, co-attention
4. SEQ2SEQ model, like m5.

### **12nd Solutions**

**https://www.kaggle.com/c/optiver-realized-volatility-prediction/discussion/275169**

![img](https://confluence-apps-us.asml.com:8443/download/attachments/166131971/image2021-10-9_15-10-33.png?version=1&modificationDate=1633763434000&api=v2)

##### **[Evolution 1]**

Issue: The training was too slow
Solution: Replace RNN parts with handmade features
\- training is much faster
\- almost no difference in performance

**Performance: cv: 0.211, lb: ~0.200**

##### **[Evolution 2]**

Issue: As hint by the top team, we did not consider the relationship between time_ids.
Solution: Use Nearest Neighbors to find top-N closest time_ids, and average the  features for each stock from the time_id neighbors as new features.

**Performance: cv: ~0.198, lb: ~0.189**

##### **[Blending]**

Transformer + Tabnet + NN with different feature sets.