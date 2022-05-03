# Unit 6

unconditional (or prior) probability

conditional (or posterior)

## Derived Distribution

Given the distribution of $X, Y$, find the distribution of $Z=g(X, Y)$.

**Discrete:**

![image-20220315144454365](https://chqwer2.github.io/img/Typora/image-20220315144454365.png)

**Continuous:**

![image-20220315144739282](https://chqwer2.github.io/img/Typora/image-20220315144739282.png)

**How to find a PDF of r.v.?**

<img src="https://chqwer2.github.io/img/Typora/image-20220315145620969.png" alt="image-20220315145620969" style="zoom: 67%;" />

Example 1

![image-20220315150012454](https://chqwer2.github.io/img/Typora/image-20220315150012454.png)

Example 2

![image-20220315150159819](https://chqwer2.github.io/img/Typora/image-20220315150159819.png)

### The monotonic case

Monotonic function is $g(\cdot)$ = $x^3, a/x$ etc., we have if $x < x' \to g(x)<g(x')$ or vise. 

inverse function we call $h(\cdot) = g'(\cdot)$, when g increase, h also increase

<img src="https://chqwer2.github.io/img/Typora/image-20220315155433045.png" alt="image-20220315155433045" style="zoom:50%;" />

<img src="https://chqwer2.github.io/img/Typora/image-20220315155510279.png" alt="image-20220315155510279" style="zoom:67%;" />

It is simpler because we only do $h(\cdot)$ function

General Method for Nonmonotonic Case

![image-20220315160814139](https://chqwer2.github.io/img/Typora/image-20220315160814139.png)

![image-20220315164126318](https://chqwer2.github.io/img/Typora/image-20220315164126318.png)

### Sum of independent continuous r.v.'s

<img src="https://chqwer2.github.io/img/Typora/image-20220315171314982.png" alt="image-20220315171314982" style="zoom:67%;" />

Proof:

![image-20220315171924290](https://chqwer2.github.io/img/Typora/image-20220315171924290.png)

![image-20220315211020632](https://chqwer2.github.io/img/Typora/image-20220315211020632.png)



It is a convolution with , the key is to specify the $z$.

![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/0*xnvnYarM1bjUYkPm.png)



![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/0*LWFWRQwofjc8slsg.gif)

of multinomial:

https://math.stackexchange.com/questions/1669513/find-the-covariances-of-a-multinomial-distribution

Covariance of multinomial is $-n*p_1*p_2$

Problem:

https://learning.edx.org/course/course-v1:MITx+6.431x+1T2022/block-v1:MITx+6.431x+1T2022+type@sequential+block@Problem_Set_6/block-v1:MITx+6.431x+1T2022+type@vertical+block@ch9-s7-tab5

![image-20220321163333924](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321163333924.png)

### Covariance

![image-20220315211310011](https://chqwer2.github.io/img/Typora/image-20220315211310011.png)

Independent = $Conv(X,Y) = 0$ (converse is not true)

Or simply:

![image-20220315212340858](https://chqwer2.github.io/img/Typora/image-20220315212340858.png)

**The variance of the sum of r.v.'s**

![image-20220315212752501](https://chqwer2.github.io/img/Typora/image-20220315212752501.png)

All possible covariance between all pairs

### correlation coefficient

![image-20220315213838229](https://chqwer2.github.io/img/Typora/image-20220315213838229.png)

is dimensionless

### Interpreting the correlation coefficient

![image-20220315214755006](https://chqwer2.github.io/img/Typora/image-20220315214755006.png)

### Correlations matter

![image-20220315220028095](https://chqwer2.github.io/img/Typora/image-20220315220028095.png)

## Conditional Expectation and Variance

In this segment we revisit the concept of conditional expectation and view it as an abstract object

of a special r.v. $g(y)$.

![image-20220316102554732](https://chqwer2.github.io/img/Typora/image-20220316102554732.png)

The Law of iterated expectations

![image-20220316103541185](https://chqwer2.github.io/img/Typora/image-20220316103541185.png)

![image-20220317200226259](https://chqwer2.github.io/img/Typora/image-20220317200226259.png)

![image-20220317200739986](https://chqwer2.github.io/img/Typora/image-20220317200739986.png)

**Stick-breaking revisited**

![image-20220316104118244](https://chqwer2.github.io/img/Typora/image-20220316104118244.png)

### The conditional variance

as a random variable

![image-20220317175043901](https://chqwer2.github.io/img/Typora/image-20220317175043901.png)

proof of this equality:

>  Derivation of the law of total variance

![image-20220317175559717](https://chqwer2.github.io/img/Typora/image-20220317175559717.png)

And according to the law of iterated expectations, it is

the same as the unconditional expectation.

![image-20220317175744268](https://chqwer2.github.io/img/Typora/image-20220317175744268.png)

![image-20220317201936918](https://chqwer2.github.io/img/Typora/image-20220317201936918.png)

**A simple example**

![image-20220317180319094](https://chqwer2.github.io/img/Typora/image-20220317180319094.png)

### Section means and variances

We will now go through another example to consolidate our

intuition about the content of the law of iterated

expectations and the law of the total variance.

![image-20220317180714804](https://chqwer2.github.io/img/Typora/image-20220317180714804.png)

![image-20220317180907945](https://chqwer2.github.io/img/Typora/image-20220317180907945.png)



### Mean of the sum of a random number of random variables

![image-20220320223230927](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320223230927.png)

### Variance of the sum of a random number of random variables

![image-20220320224048435](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220320224048435.png)

What this expression tells us is that the variance of the

total amount that you spend, which is a certain measure of

the amount of randomness in how much you are spending

overall, this amount of randomness

is due to two causes.

One cause is the randomness that there is in how much

money you spend in any given store, and that's captured by

the variance of X. It's the variance of the distribution

of the amount of money that you spend in a typical store.

But there is another source of randomness, and that source of

randomness comes from the fact that the number of stores

itself is random, and this gives us this contribution to

the variance of Y.

By taking into account these two sources of randomness, we

can figure out the overall variance of the random variable Y.





### Recitation

### Derived distribution example

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321094437227.png" alt="image-20220321094437227" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321094452878.png" alt="image-20220321094452878" style="zoom:50%;" />

The last thing that we need to take care of is, what is the range? Remember it's important when you calculate out PDFs to always think about the ranges where things are valid.



![image-20220321095308413](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321095308413.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321095358048.png" alt="image-20220321095358048" style="zoom:50%;" />

### Ambulance travel question

![image-20220321095613057](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321095613057.png)

![image-20220321095729047](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321095729047.png)

![image-20220321100127112](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321100127112.png)





Interchange the derivative and the summation.

![image-20220321101237744](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321101237744.png)

similar to the conv formula

![image-20220321102141000](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321102141000.png)

![image-20220321102306738](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321102306738.png)

![image-20220321102812757](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321102812757.png)

Condition can break the problem into parts that you can calculate easily

![image-20220321103537987](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321103537987.png)

![image-20220321103859650](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321103859650.png)

Try to do it another way

![image-20220321104003683](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321104003683.png)

![image-20220321104027678](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321104027678.png)



![image-20220321104622806](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321104622806.png)

![image-20220321105001353](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321105001353.png)

![image-20220321105730934](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220321105730934.png)

And so we have found a way of simulating

exponential random variables, starting with a random number

generator that produces uniform random variables.





