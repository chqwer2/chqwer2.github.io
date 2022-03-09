# XGBoost with Time Series

Extreme GradientBoosting (XGBoots)

— XGBoost:A Scalable Tree Boosting System, 2016.

https://arxiv.org/abs/1603.02754

Google+陈天奇有关XGBOOST



XGBoost is designed to cooperate with tabular data. However, the trivial physical environment tend to be more time-corelated that the time series should be taken into consideration.



### K-fold

It is traditional that split time series into K folds and fore-forward predict.

In the forward verification, the data is first divided into training  sets and test sets by selecting a split point, such as the last 12  months of data for training, and the last 12 months is used for testing.

《How To Backtest Machine Learning Models for Time Series Forecasting》

链接：https://machinelearningmastery.com/backtest-machine-learning-models-time-series-forecasting/）



可以用XGBRegressor类来做一步预测。xgboost_forecast()方法实现的是，以训练集、测试集的输入作为函数的输入，拟合模型，然后做一步长预测。

![img](https://image.jiqizhixin.com/uploads/editor/2b30ef5d-d45e-4b95-b67d-306183930e9c/640.png)

机器之心: https://www.jiqizhixin.com/articles/2020-09-02-2

原文: https://machinelearningmastery.com/xgboost-for-time-series-forecasting

**Reference**

《机器学习中梯度提升算法的简要概括》

链接：https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/



有关准备时间序列预测数据的滑动窗口方法的更多信息，请参阅教程：

《Time Series Forecasting as Supervised Learning》

链接：https://machinelearningmastery.com/time-series-forecasting-supervised-learning/

可以用pandas库的shift()方法，按照给定的输入输出的长度，把时间序列数据转换为新框架。



```python
from sklearn.model_selection import cross_val_score,KFold
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib

# setup regressor
xgb_model = xgb.XGBRegressor() 
# performance a grid search
tweaked_model = GridSearchCV(
    xgb_model,   
    {
        'max_depth':[1,2,5,10,20],
        'n_estimators':[20,30,50,70,100],
        'learning_rate':[0.1,0.2,0.3,0.4,0.5]
    },   
    cv = 3,   
    verbose = 1,
    n_jobs = -1,  
    scoring = 'neg_median_absolute_error', 
tweaked_model.fit(X_train[:-1],y_train)
print('Best: %f using %s'%(tweaked_model.best_score_, tweaked_model.best_params_))
    
# Predict
  #saving and load models
def save_model(model,filename):
    return joblib.dump(model,filename)

def load_model(filename):
    return joblib.load(filename)

#四、预测新数据
save_model(tweaked_model,'XGB-model_lag=7.pkl')
model = load_model('XGB-model_lag=7.pkl')

model1 = xgb.XGBRegressor(learning_rate= 0.1, max_depth= 5, n_estimators= 100)
model1.fit(X_train[:-101],y_train[:-100])

#以最后100天的数据为测试数据
X_predict = model1.predict(X_train[-101:])

plt.plot(y_train[-100:],color='blue',label='actul')
plt.plot(X_predict,color='red',label='predict')
plt.legend(loc='best')
plt.title('RMSE:%.4f'%np.sqrt((sum((X_predict[:-1]-y_train[-100:])**2))/len(X_predict)))
plt.show()
print("the next day predict is %.f"%X_predict[-1])
```





# 时序算法Prophet+xgboost

https://zhuanlan.zhihu.com/p/187543618