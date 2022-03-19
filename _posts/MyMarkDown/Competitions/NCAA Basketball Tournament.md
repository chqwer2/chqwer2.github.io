# 2021 NCAA Man 

## 2nd Solution

[github ](https://github.com/dusty-turner/ncaa_tournament_2021_beat_navy)based on R.

#### Key factors in our model

- Average ranking across all Massey Ordinals 
- Clustering of teams based on offensive efficiency, defensive  efficiency, percentage of points from 3s, possessions per game, assist  to turnover ratio 
- Winning percentage 
- Free throw rate   
- COL Ranking from Massey Ordinals  
- Conference win/loss against all other conferences 
- Quad 1 wins and Quad 4 losses  
- Tournament Seed of Team 
- Schedule Ranking 
- The following average statistics from the last 3 games of the season 
  - Offensive efficiency 
  - Defensive efficiency 
  - Possessions per game  

#### External Data

We used data from the link below for team efficiency, percentage of  points from 3s, possessions per game, and assist to turnover ratio.   

https://www.teamrankings.com/ncb/rankings/ 

#### Model Workflow

While we feel the most important part of creating this model was  development of features, our modeling workflow helped keep things  organized.  We did the following: 

- We created one r script that did all of our data cleaning and sourced it in our execution script. 
- We created one r script that contained all the functions we used and sourced it in the main execution script. 
- We created a model registry that tracked factors used in the model,  model type, tuning grid size, model performance, and special notes we  wanted to track. 
- We created one major function to execute models.  This function did the following: 
- Check the model registry to see if the model had already been executed. 
- Used the tidymodels workflow to create test/train data, develop a  tuning grid, tune the model through cross validation, select the best  model parameters, apply it to the entire dataset, then apply it to the  validation data.   
- Save model performance information to the model registry. 



## 3rd place solution | NCAAM 2021

https://www.kaggle.com/timsereno/ncaam-march-mania-2021

 This did not include the Massey Ordinals.  My goal was to focus my  attention on the model tuning rather than on data wrangling.



10 fold cross-validation, and blended (ensembled) three models using Extra Trees, LDA, and NB linear regression algorithms.  



 out-of-the box grid search

 LogLoss

Catboost and LightGBM were really slow to train model even with GPU  acceleration and metrics were not improving, so decided to go with the  faster classic algorithms.  



### Others

# Modeling

So, my final solution contains an ensemble of `LGB`, `XGB`, `HistGradientBoostingClassifier`, `RandomForestClassifier` and `LogisticRegression`. I also tried models like `SVM` & `LinearRegression` but it decreased the CV, so I excluded those models from the final ensemble.

Basically, my goal was to reduce the bias of a model as much as possible. 
Ensemble weights are decided by the CV score.



I preferred `GroupKFold` with the `season` column as a group over other alternatives as it will treat all the season together instead of random shuffling.

And obviously, I only used data until 2015 in the CV & model building to avoid any leakage.

The score on 2015 to the latest year data will be treated as test. So,  any improvement in that score highly likely to convert to the 2021  score.

Also, I created some `magic` features out of higher  importance features from the LGB feature importance graph. Which may  have some effect as well. I would recommend seeing the [notebook](https://www.kaggle.com/prashantkikani/ncaam-2021-diverse-model-ensemble) for more details.





https://www.kaggle.com/c/ncaam-march-mania-2021/discussion/231068