# T-test

Wald test is great.

It has lots of flexibility.

Unlike tests based on confidence intervals,

we don't have to think about the form of our confidence interval

before we devise the Wald test.

You give me one of the three types

of hypotheses, one-sided or two-sided,

and then I can build a Wald test.

I can compute the p-values.



One of the issue with this test is

that it relies on asymptotic statements.

![image-20220329140443250](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329140443250.png)

we cannot actually use the central limit theorem

or Slutsky, all these asymptotic statements that rely

on a sample size to be at least 40 or even 50 in general.



So instead, we **assume** that our data is **Gaussian**.

**an example** where we might have a small number of measurements.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329142459602.png" alt="image-20220329142459602" style="zoom: 25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329142839415.png" alt="image-20220329142839415" style="zoom: 25%;" />

because the sample sizes are too small for Slutsky's theorem to apply

### The Chi-squared distribution

k-degree of freedom

![image-20220329151304216](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329151304216.png)

PDF?

a chi square is always the sum of squares of random variable.

![image-20220329152233602](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329152233602.png)

### Sample Variance and Sample Mean of IID Gaussians: Cochran's Theorem

Unbiased sample variance

But, rather than having n degrees of freedom, I'm losing one degree of freedom, which is the price to pay for replacing mu by Xn bar



So saying that Xn bar and Sn squared are independent random variables is the same as saying that the numerator is independent of the denominator.

![image-20220329154709848](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329154709848.png)

#### <img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329154823559.png" alt="image-20220329154823559" style="zoom:50%;" />

### Student’s T distribution

![image-20220329161325456](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329161325456.png)

Well, this distribution, as a name,

it does not depend on any unknown parameter.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329162103991.png" alt="image-20220329162103991" style="zoom:50%;" />

So, as n goes to infinity, the denominator here will converge to 1, so T_n will looks like Z

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329161745077.png" alt="image-20220329161745077" style="zoom: 25%;" />

### Student’s T Test

So we're going to be able to apply essentially

the same machinery that we applied for the Wald test,

except that our main ingredient, which

was this asymptotic normality statement for an estimator

of the parameter theta, will be replaced

by an exact distribution.

Now, this looks great, but remember

that this came at a price.

The first price is that we actually assume

that our data is Gaussian.

And something that is maybe a bit more subtle

is that this only applies when the parameter of interest

is the expected value.

![image-20220329163458420](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329163458420.png)

reject performed at level $\alpha$, not asynomtotic level.

![image-20220329163616019](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329163616019.png)

### P-values for the T-test

![image-20220329165618536](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329165618536.png)

### Comparison between the T-test and the Wald test

And the reason is because the Gaussian has lighter tails than the t11 distribution.

And so the quantiles for the t11 are a bit larger, which will also result in larger p-values, more conservative.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329205152750.png" alt="image-20220329205152750" style="zoom:30%;" />

So the next question is, why would I

want to use the Wald test when I can actually

use a more precise test?

T-score calculator: https://goodcalculators.com/student-t-value-calculator/



### Two-sample Test

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329214628008.png" alt="image-20220329214628008" style="zoom:50%;" />

sigma hat…

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329214853291.png" alt="image-20220329214853291" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329215005240.png" alt="image-20220329215005240" style="zoom:40%;" />

And what can be checked is that, in fact, this N can always

be taken--

N is the degree of freedom.

will always be at least the minimum of n and m.

So, if we don't want to bother computing this quantity,

what we can do is be a little more conservative

and take the minimum of n and m.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329215205825.png" alt="image-20220329215205825" style="zoom:33%;" />

why n-1? The round..

![image-20220329215456609](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329215456609.png)

Now we have to round it, but it is 12 or 13??

We could round it to 13.

But, in fact, we have to always make

the more conservative choice.

And the more conservative choice is

to take the **smaller number of degrees of freedom.**

So here, in fact, the rounding I should be taken is **12**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329215646476.png" alt="image-20220329215646476" style="zoom:50%;" />

# Comparison

![image-20220330093332546](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330093332546.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330093545317.png" alt="image-20220330093545317" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330093743375.png" alt="image-20220330093743375" style="zoom:50%;" />

So plug in for the standard deviation portion

of this normal variable. And this will define Wald's test, right?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330094515655.png" alt="image-20220330094515655" style="zoom:50%;" />

much greater than 1, right, logC

 So as you can see, you can actually derive two tests that have asymptotic chi-squared distributions.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330095949489.png" alt="image-20220330095949489" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330100418028.png" alt="image-20220330100418028" style="zoom:50%;" />

![image-20220330101016998](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330101016998.png)

Different answers..



### Proof of Cochran's Theorem and T Test

![image-20220330102602424](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330102602424.png)

I'm looking for a non-asymptotic test here.

#### MLE for Gaussian Variables

![image-20220330103757012](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330103757012.png)

#### Proving Cochran's Theorem: Orthogonal Matrices

pivot. $\tilde T_n$

Orthogonal Matrices

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330104919217.png" alt="image-20220330104919217" style="zoom:50%;" />

And with this, I should have enough tools to now

actually investigate the distribution of sigma

hat squared on the next slide.

But these w's do not go away, essentially

because you're projecting down to a smaller space.

#### Sample Variance as a Norm

# TODO NOT GET IT

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330110555715.png" alt="image-20220330110555715" style="zoom:50%;" />

![image-20220330110644639](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330110644639.png)



Miss one video: 

### T-test

![image-20220330111009931](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330111009931.png)

![image-20220330111332520](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330111332520.png)



# Multiple Hypothesis Testing

So what you do is you record the t-value,

which is a strong indicator of what the p-value actually is.

OK, so the t-value is the value of the absolute value

of your test statistic.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331162819003.png" alt="image-20220331162819003" style="zoom:30%;" />

Now, of course, this is completely wrong, right?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331163219288.png" alt="image-20220331163219288" style="zoom:33%;" />

This should be attributed to type 1 error.

**Errors in multiple hypothesis testing**

So what went wrong with the salmon example?

Well, we're facing what's called a multiple testing

problem or a multiple hypothesis testing problem.

And this is precisely the topic of this lecture.

So the issue here is that we have a lot of individual tests.

And we're trying to make a conclusion based

on their aggregate decision.

In a way, what we're trying to say

is, well, if there is at least one voxel that activates,

then it must mean that there is some brain

activity in this dead salmon.



U is the union

But the problem is that this union thing is becoming so huge when

N is, say, 20,000 in the gene example

or 8,000 in the voxel examples that keeping it under this probability alpha really

makes for tiny rejection regions.

And, essentially, we never make any discovery.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331163842181.png" alt="image-20220331163842181" style="zoom:40%;" />

So we need FDR - False Discovery Rate and has different C for each test

![image-20220331164029458](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331164029458.png)

his will actually buy us a lot of power

and allow us to at least reject some of the tests

and make some scientific discovery.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331164132995.png" alt="image-20220331164132995" style="zoom:50%;" />

**The Bonferonni method to control FWER**

**Family-wise error rate (FWER)** : the probability of making at least one false discovery, or type I error; 

It just says, wherever you used to use alpha,

now, you use alpha over capital N

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331205642177.png" alt="image-20220331205642177" style="zoom:50%;" />

really very small p-values

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331210540908.png" alt="image-20220331210540908" style="zoom:50%;" />

![image-20220331211217827](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331211217827.png)

T calculator - https://homepage.divms.uiowa.edu/~mbognar/applets/t.html 

### The Bejamini Hochberg to control the FDR

And this is, for example, the case

of the Bonferroni correction.

It says keep only those p-values that

are at most alpha over capital N.

And you have some more complicated ways,

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331211701109.png" alt="image-20220331211701109" style="zoom:50%;" />





as long as there

is one that satisfies this, I can actually

take it to be i max and reject all the i's that

are smaller than this i max.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331211951380.png" alt="image-20220331211951380" style="zoom:35%;" />

P must follow an increasing order



### Exercise

![image-20220331214902505](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331214902505.png)

![image-20220331214929578](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331214929578.png)

![image-20220331215130236](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220331215130236.png)

### 

### Recitation

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220404230745996.png" alt="image-20220404230745996" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220404231344569.png" alt="image-20220404231344569" style="zoom:50%;" />



Under the null hypothesis, I have

to plug in some value of theta here.

I know g of theta is 0 under the null hypothesis,

but what do I know about these?

And this is where the two versions

of Walds test, or the Wald test, come into play.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220404231439173.png" alt="image-20220404231439173" style="zoom:50%;" />

![image-20220404231909213](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220404231909213.png)

### likelihood ratio test

![image-20220405075702055](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405075702055.png)



Well, the expectation of an indicator

is just the probability of that indicator equaling

1, which is just, again, the probability that x

equals each of these values.

![image-20220405090435007](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405090435007.png)

![image-20220405090505670](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405090505670.png)

Miss two recitation here



### Recitation T test

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405090912754.png" alt="image-20220405090912754" style="zoom:50%;" />



**Pros and Cons of T test**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405091229691.png" alt="image-20220405091229691" style="zoom:50%;" />

**Example:**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405091526543.png" alt="image-20220405091526543" style="zoom:50%;" />



So keep in mind that if we chose a different value of mu,

some value of mu not equal to 1, then tn,

which is this expression--

it would not have a student's t distribution.

And the reason is we're not subtracting away

the true parameter here if mu is not equal to 1.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405092702397.png" alt="image-20220405092702397" style="zoom:50%;" />

1-sided, 1-sample

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405092840602.png" alt="image-20220405092840602" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405092925926.png" alt="image-20220405092925926" style="zoom:50%;" />

2-sample

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405092904731.png" alt="image-20220405092904731" style="zoom:50%;" />

![](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405095420452.png)

![0, 027() 2-0 D Given X(i) = 2.01, and n18 Test stansns](https://media.cheggcdn.com/coop/00d/00deb796-e7f4-4f72-baaa-8f7949b32a8b/1597512453710_WhatsAppImage2020-08-15at10.56.02PM.png)

![© we will level 0.05 if oreject Ho at observed T Xco) ice, PHO CXcm <e ) >0 > a= 0.05 PHO (x,ce, X₂ ce, X is ce ce) =0.05 Pto](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/1597512465620_WhatsAppImage2020-08-15at10.56.02PM1.png)
