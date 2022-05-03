# Linear Regression

Statistics for PCA??

### Goals of Regression

### Partial Modeling, Regression Function, and Conditional Quantiles

Focus on the conditional density of Y given X

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220425164555557.png" alt="image-20220425164555557" style="zoom:50%;" />

Quantile regression: such as median regression

![image-20220425165308824](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220425165308824.png)

### Plots of Conditional Distributions and Conditional Quantiles and Box-and-Whisker Plots

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220427152720138.png" alt="image-20220427152720138" style="zoom:50%;" />

25~75 percentile within the box, a thicker line is the median.

### Linear Regression - Basic Setup

![image-20220427165003669](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220427165003669.png)

talk about linear regression

![image-20220427171600662](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220427171600662.png)

### Linear Regression in Practice: Linear Model Plus Noise

![](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220427165800630.png)

![image-20220427170008821](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220427170008821.png)

### Least Squares Estimator (LSE)

![image-20220427170522325](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220427170522325.png)

And you can see that this is what--

this is expectation of XY minus expectation of X expectation

of Y. That's the empirical covariance between X and Y.

And this is the average of the X squared

minus the square of the average, which is the sample variance.

### Optimal Theoretical Regression Line

![image-20220428100147429](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220428100147429.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220428100703513.png" alt="image-20220428100703513" style="zoom:50%;" />



![image-20220428100802204](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220428100802204.png)

![image-20220428100824638](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220428100824638.png)



### Multivariate Regression: Definitions, Modeling, and Matrix LSE

![image-20220429144510526](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220429144510526.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220429144843564.png" alt="image-20220429144843564" style="zoom:50%;" />



### Review: Setup of Multivariate Linear Regression

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220430104552341.png" alt="image-20220430104552341" style="zoom:50%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501111255552.png" alt="image-20220501111255552" style="zoom:50%;" />

![image-20220501111638361](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501111638361.png)

Then we can solve a question with rank(A) equations

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220430104951871.png" alt="image-20220430104951871" style="zoom:50%;" />



That means that if you want to do these squares

estimator, et cetera, you'd better

have at least 20,001 observations to actually

be able to do this.

Clearly, this is not going to happen.

You're not going to have-- well, maybe 23andMe

has this kind of data set.

But most regular genomic studies don't

have that kind of samples.

And so we have to do some regularization.

We have to, essentially, cheat to make this matrix invertible.

And there's many ways to do it.

One way is to say, well, if this matrix is not invertible,

I'm just going to add the identity to it,

and that's going to make it invertible,

that's called [INAUDIBLE] regression.

### Geometric Interpretation of Linear Regression

![image-20220430110025304](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220430110025304.png)

![image-20220501113806625](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501113806625.png)

![image-20220430120223546](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220430120223546.png)





### Linear Regression with Deterministic Design

![image-20220430230415627](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220430230415627.png)

![image-20220501163443236](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501163443236.png)



### Deterministic Design with Gaussian Noise

![image-20220501164810261](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501164810261.png)

#### The Least Square Estimator is the MLE in Deterministic Design

#### Distribution of the Least Square Estimator



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501171935284.png" alt="image-20220501171935284" style="zoom:50%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501172354899.png" alt="image-20220501172354899" style="zoom:50%;" />

![image-20220501175613436](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501175613436.png)

#### Quadratic Risk and Variance

Trace, what is it? TODO

![image-20220501173941510](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501173941510.png)



### Prediction Error

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501175222261.png" alt="image-20220501175222261" style="zoom:33%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501175416748.png" alt="image-20220501175416748" style="zoom:50%;" />



plus P orthogonal of what



#### Significance Tests

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502093833158.png" alt="image-20220502093833158" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502101108560.png" alt="image-20220502101108560" style="zoom:50%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502101456308.png" alt="image-20220502101456308" style="zoom:50%;" />

### Bonferroni's Test

So in practice, maybe I don't want

to test just if one gene is here or not, right?

I'm going to go and look at gene number 9,624.



So you want to control just the proportion of false discoveries

among the discoveries that you're making,

rather than the proportion of discoveries among everything.



And so, Bonferroni's test is trying

to say, OK, I want to combine all those tests at once.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502173829405.png" alt="image-20220502173829405" style="zoom:50%;" />

But may never reject null.

### Closing Remarks

Correlation









### Ridge Regression

1. Linear Regression and Bayesian Estimation

![image-20220502105540848](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502105540848.png)





What I'm saying is beta actually comes

from a Gaussian distribution, which is homoscedastic.

So there are no differences between any directions here.



**How to calculate Posterior Distribution?**

Mu and sigma is defined..

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502111927950.png" alt="image-20220502111927950" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502181337451-1511618.png" alt="image-20220502181337451" style="zoom:33%;" />

**What is Ridge?**

This is often called a ridge estimator.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502112705122.png" alt="image-20220502112705122" style="zoom:50%;" />



What is the risk?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502113402502.png" alt="image-20220502113402502" style="zoom:50%;" />

How to find lambda to decrease the risk?



![image-20220502171703337](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502171703337.png)





<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502171653276.png" alt="image-20220502171653276" style="zoom:50%;" />
