# Petfinder.my 2019

### 2nd Solution

[[code]](https://www.kaggle.com/calvchen/stack-480-speedup-groupkfold/edit)

##### LGBM2 + XGB

[XGB_based_kernel](https://www.kaggle.com/reppy4620/xgboost)

![image-20220105113733417](https://chqwer2.github.io/img/Typora/image-20220105113733417.png)

[dataset](https://www.kaggle.com/hocop1/cat-and-dog-breeds-parameters) [Demographics](https://en.wikipedia.org/wiki/Demographics_of_Malaysia)



##### Feature engineering

<img src="https://chqwer2.github.io/img/Typora/image-20220105114421883.png" alt="image-20220105114421883" style="zoom:50%;" />

<img src="https://chqwer2.github.io/img/Typora/image-20220105114412638.png" alt="image-20220105114412638" style="zoom:50%;" />

![image-20220105112853536](https://chqwer2.github.io/img/Typora/image-20220105112853536.png)

**Aggregation**: 

![image-20220105112843557](https://chqwer2.github.io/img/Typora/image-20220105112843557.png)

(Age/12).astype(int)

flag which shows they are over 1 year old or not.

##### == Others ==

- Cute or not binary features by model trained by external cats and dogs pictures

##### Metadata

![image-20220105114503734](https://chqwer2.github.io/img/Typora/image-20220105114503734.png)

### interactions features

Age * Quantity
Age / Quantity
PhotoAmt / Quantity



LB score Stratified K fold=Group K fold>Group Stratified K fold

![image-20220105120235603](https://chqwer2.github.io/img/Typora/image-20220105120235603.png)