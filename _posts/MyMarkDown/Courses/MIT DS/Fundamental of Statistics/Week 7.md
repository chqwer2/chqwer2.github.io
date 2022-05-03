# Parametric Hypothesis Testing

**Waiting time in Emergency Room (ER)**

<img src="/Users/haochen/Desktop/Python Project/chqwer2.github.io/img/Typora/image-20220319225804800.png" alt="image-20220319225804800" style="zoom:50%;" />

**Null hypothesis and alternative hypothesis**

A test is typically either one-sided or two-sided

<img src="/Users/haochen/Desktop/Python Project/chqwer2.github.io/img/Typora/image-20220319230228594.png" alt="image-20220319230228594" style="zoom:50%;" />

In two-sided test, this alternative allows you to be on either side of theta 0.

**How to turn specific problem into statistical problem?**

Control group and test group.. : Two-sample test.

We want to prove the alternative hypothesis is complied.

<img src="/Users/haochen/Library/Application%20Support/typora-user-images/image-20220320101740968.png" alt="image-20220320101740653" style="zoom:50%;" />

So what we want to do is to decide whether to  *reject* $H_0$.

status quo... or scientific discovery that we ask many evidences to against status quo.

Note that we only proof we did not collect enough evidence to show that the drug was better than control.

![image-20220320102546129](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320102546129.png)

![image-20220320103657610](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320103657610.png)

Now we need a test to proof is.

A test is a statistic $\psi \in \{0,1\}$, can be written as indicator.

![image-20220320104249346](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320104249346.png)



**Error of a test**

two types of error: Type 1 error and type 2 error.

Power function. $\beta(\cdot)$.

![image-20220320105124705](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320105124705.png)



$1 - P(type 2)$

### Level and asymptotic level

Never reject or never accept.

But we need to medigate both problem..

called **multi-object optimization**, is very difficult.

So we decide that one of the errors is actually more important than the other one.

(Type 1 error is more important.)

![image-20220320110102712](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320110102712.png)



How to pick $\alpha$?

Convert level to asymptotic level..

![image-20220320113721789](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320113721789.png)



How do we build a test from a confidemce interval?

![image-20220320114603678](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320114603678.png)

$\alpha$ probability of rejection

at most $\alpha$ of the test will make an error of type 1 error.



![image-20220320114938159](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320114938159.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320115343915.png" alt="image-20220320115343915" style="zoom:50%;" />

**P-value**

$\beta(\theta) = 1- P(\theta) \text{ in the }\psi(\cdot)$

![image-20220320220520213](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320220520213.png)

![image-20220321225953374](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321225953374.png)

![image-20220322143039361](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322143039361.png)

![image-20220324114019764](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220324114019764.png)

![image-20220320220912375](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320220912375.png)

# The evidence scale



![image-20220320222303490](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320222303490.png)

![image-20220322144008366](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322144008366.png)

![image-20220322144056946](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322144056946.png)



### Recitation of Hypothesis Testing

![image-20220323210004707](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220323210004707.png)



X is the custormer obversed in some time period, $\lambda$ is the number of customers expected

we're putting on the number of customers, but Poisson distribution is usually

but Poisson distribution is usually a good choice for things like how many customers do I see in a specific time period.



Level of the test $\alpha$ is the biggest probability the we tolerate the type I error occurs

![image-20220323211654931](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220323211654931.png)

Pivot 

#### Two-sided Test

we will often do when trying to come up

with a hypothesis test and a test statistic

is to find an estimator for the underlying parameter

because at the end of the day, we

want to be able to make statements about lambda.

So we should try and extract as much information

as possible from our data points pertaining to lambda,

the underlying lambda.



1. I want to have something that whenever it's small,
2. it should be an indicator for H0 to be true.
3. And whenever it's large, it should be an indicator for H1
4. to be true.

![image-20220323213151141](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220323213151141.png)

![image-20220324210532504](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220324210532504.png)

### One-Sided Test

![image-20220323223740879](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220323223740879.png)

1. Maybe we want to give her some tolerance.
1. Composite Test

![image-20220323234527365](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220323234527365.png)





### Example

![image-20220324095108316](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220324095108316.png)



1. Well, we know that these are just sample averages.
2. So we actually know what's going to happen as n goes to infinity
3. by the central limit theorem.
4. The problem is we are mixing them up,
5. so we need to first use the high dimensional central limit
6. theorem, and then we need to think
7. about what that implies if we take
8. the difference between the two.



Delta method

$\sum$ is the covariance matrix

![image-20220324100052076](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220324100052076.png)

![image-20220324100242056](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220324100242056.png)

![image-20220324100835745](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220324100835745.png)



![image-20220324100938931](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220324100938931.png)![image-20220324101517445](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220324101517445.png)





1. It might be hard in practice to actually find any such setup
2. where the sample sizes of both groups are equal.
3. Often, you will have different sample sizes.



![image-20220324102551135](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220324102551135.png)

So what is the variance?