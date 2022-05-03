# Infimum and supremumGoodness of Fit Test for Discrete Distributions

Chi Score： https://shiny.rit.albany.edu/stat/chisq/

Non-parametric hypothesis

So, that's a very difficult question

because there's many candidates that actually, are much more

likely to fit our data well.

So, we're going to have to be a little careful about how

we make those tests, OK?

### GoF

Whether or not this is a good distribution candidate?

![image-20220405143932722](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405143932722.png)

the only thing that plays a role in the fluctuations-- there's

no variance term, there's no variance parameter or anything.

It's just this random sampling.



### The Probability Simplex of Discrete Distributions

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405144721024.png" alt="image-20220405144721024" style="zoom:50%;" />

![image-20220405150059041](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405150059041.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405150032959.png" alt="image-20220405150032959" style="zoom:50%;" />

![image-20220405150432569](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405150432569.png)

Only 1,2.

X in uniform distribution

![image-20220405150235153](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405150235153.png)

![image-20220405150159748](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405150159748.png)

![image-20220405150351938](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405150351938.png)

![image-20220405150510217](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405150510217.png)

Done

### GoF

![image-20220405150631226](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405150631226.png)

![image-20220405150744298](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405150744298.png)

### The Goodness of Fit Test: Categorical Likelihoods



The t-test is to test the mean of a Gaussian when I don't know the variance.

Wald's test is one of those guys.

Wald's test is definitely one.

It's based on the maximum likelihood estimator,

which certainly is generic.

All you need to give me is a PMF for a PDF.

I can compute the maximum likelihood estimator,

can compute the Fisher information matrix.

And I can construct Wald test.



The likelihood ratio test, correct.

So the likelihood ratio test was boiled down

to actually being Wald's test in one dimension.

It was just a different way.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405151958613.png" alt="image-20220405151958613" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405153417944.png" alt="image-20220405153417944" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405153949299.png" alt="image-20220405153949299" style="zoom:50%;" />

![image-20220405154514191](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405154514191.png)

### MLE for Multinomial Distribution

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405155146285.png" alt="image-20220405155146285" style="zoom:50%;" />

What got wrong here?

The last guy depends on the sum of the previous one.

So this last PK really is 1 minus the sum for j equals 1

to K minus 1 the Pj's.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405155456726.png" alt="image-20220405155456726" style="zoom:50%;" />

But it now depends on $N_k$?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405155647891.png" alt="image-20220405155647891" style="zoom:50%;" />

All the left hands side equal to each other, called $\gamma$.
$$
p_j = \frac{N_j}{\gamma}, \gamma=n
$$
<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405155945586.png" alt="image-20220405155945586" style="zoom:50%;" />



### A Degenerate Gaussian Random Variable

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405162606408.png" alt="image-20220405162606408" style="zoom:50%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405163428578.png" alt="image-20220405163428578" style="zoom:50%;" />

And now it means that my data is actually always--

p hat minus p0 is always perpendicular to it.

So if I have a Gaussian, asymptotically it's

going to be a Gaussian that is distributed exactly

along this line.



**chi** for chi-squared distribution, **T** for Student's T distribution, **G** for standard Gaussian distribution. 

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405165427093.png" alt="image-20220405165427093" style="zoom:50%;" />

### The Chi-Squared Test for Testing Goodness of Fit of Discrete Distributions

Chi-Squared Test

Theorem under  $H_0$

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405172500553.png" alt="image-20220405172500553" style="zoom:50%;" />

So really what I want is precisely something that says

the limit of this square root of N,

p hat minus p rescaled by the Fisher information is not

a  Gaussian in d dimension.

It's a Gaussian in whatever is orthogonal to the all ones

vector.

I  want a Gaussian that lives on this two dimensional space.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405172635431.png" alt="image-20220405172635431" style="zoom:50%;" />

**But why k minus 1 degrees of freedom rather than k?**

Because we're actually losing this degree of freedom,

which is associated to the fact that we

have no variance in the direction of the all ones

vector.



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405173056086.png" alt="image-20220405173056086" style="zoom:50%;" />

But it is not true, We know that this thing is not a Gaussian

with some covariance matrix because we know that it has

no variance in one direction. So in particular, what it means is that this covariance matrix

has to have no inverse.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405173247317.png" alt="image-20220405173247317" style="zoom:50%;" />

But it is not right, I can only do is to remove one degree of freedom (this space where there's no variability.)

So the idea is that it's sort of working except that we have

to [? mud ?] out this annoying direction where

we have no variance.



### The Chi-Squared Test - Main Ideas

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405212814287.png" alt="image-20220405212814287" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405212952862.png" alt="image-20220405212952862" style="zoom:50%;" />

Others will be 0.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405213202032.png" alt="image-20220405213202032" style="zoom:50%;" />

This derive right answe but wrong.

I'm going to end up where the fisher information.

Which is actually not well-defined, in the sense

that it's not invertible.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405214321189.png" alt="image-20220405214321189" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405215207587.png" alt="image-20220405215207587" style="zoom:50%;" />

It's completely symmetric.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405215742841.png" alt="image-20220405215742841" style="zoom:50%;" />

we would have to actually remove--

from the matrix-- the thing that's

corresponding to this all one's vector.

Which is the one that really is killing everything, here.

And then once you remove it--

if you actually take this matrix and project it

onto the orthogonal of the all ones vector--

you would end up with precisely that matrix over there.

Like this, but it is not the way we should actually get this.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405220040535.png" alt="image-20220405220040535" style="zoom:50%;" />

Here, I'm trying to explain to you a few things.

**The first one is**, why do I divide here by p and not

by p squared, right?

I mean, that's not, probably, the most natural thing to do.

But we know that it's coming from this half fisher

information matrix that's coming up here.

And we have some issues with this fisher information matrix.

So, that's the first thing.

**And the second one is** why do we have only t minus 1 degrees

of freedom?

Well, it's because the asymptotic Gaussian vector

that we have actually lives in k minus dimension,

not in k dimension.

It lives on this linear space that's

orthogonal to the all ones vector, OK?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405220510331.png" alt="image-20220405220510331" style="zoom:50%;" />

So, having this joint convergence--

of the p hat j's to the p-- is important, here,

because they sum to zero.

So, something is really happening

when you look at the joint convergence of all of them

together, rather than looking at individual convergences,

all right?

### The Correct Number of Degrees of Freedom Matters in the Chi-Squared Test

So the chi squared k degrees of freedom

has larger critical value q alphas because I

have more fluctuations in chi square with k

degrees of freedom.



So, let's look at the case, k is equal to 2, OK?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405221541831.png" alt="image-20220405221541831" style="zoom:50%;" />

So, this is the test statistic Tn for the chi squared test.

p naught

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405221725426.png" alt="image-20220405221725426" style="zoom:50%;" />

### Empirical CDF

![image-20220405221841756](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405221841756.png)

So, it's the expectation of some things, the expectation

of an indicator.

And therefore, I can use my statistical hammer.

I replace the expectation by an average,

and I get what's called the empirical CDF.

Tool: https://shiny.rit.albany.edu/stat/chisq/



![image-20220405224446074](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405224446074.png)



![image-20220405224457224](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405224457224.png)

![image-20220405224652179](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405224652179.png)

![image-20220405225234323](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220405225234323.png)

# Kolmogorov-Smirnov test

Still GoF, but goto the continuous case.



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406110616955.png" alt="image-20220406110616955" style="zoom:50%;" />



And clearly, the chi squared test is not

going to work off the shelf for this, OK?

Because what is the number of modalities

that a continuous standard Gaussian can take?

It's a continuum infinite, so the number

of degrees of freedom is going to be a little too

large for you to find it, even if you remove one from it.



And so one thing that you could do is to bin your data, OK?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406111015339.png" alt="image-20220406111015339" style="zoom:50%;" />

I can use the chi-square test here..

So we'd like to have a way to do this that's

systematic and also works for continuous random variables,

You're not testing if your data is standard Gaussian.

What you're testing is, is my data

likely to come from this histogram?

OK, from this pdf.

![image-20220406112654716](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406112654716.png)

The probability of an event is a real number, not a random variables.

### Empirical Cumulative Distribution

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406113132221.png" alt="image-20220406113132221" style="zoom:50%;" />

And use statistical hammer to replace the expectation by average.

![image-20220406113508268](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406113508268.png)

### Uniform versus Pointwise Convergence

![image-20220406113814701](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406113814701.png)



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406114205048.png" alt="image-20220406114205048" style="zoom:50%;" />

What is this sup?

since I'm allowed to first take the worst possible t, it could be that this t depends on n.

so here, the worst case

is t is equal to infinity, but even if I allow t

to be equal to n, this difference

would be equal to one and would certainly not go

to zero as n goes to infinity.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406114642086.png" alt="image-20220406114642086" style="zoom:50%;" />

But Glivenko-Cantelli tells us that this thing can not happen.

#### Infimum and Supremum

![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/250px-Infimum_illustration.svg.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406115556967.png" alt="image-20220406115556967" style="zoom:50%;" />

### Asymptotic Normality of the Empirical CDF

I mean, it's an indicator, so therefore, it has to be a Bernoulli.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406152403120.png" alt="image-20220406152403120" style="zoom:50%;" />





And I claim that this thing is converging

to the soup of something.

Well it's kind of expected here.

OK, I'm taking a soup, so it's going

to be the worst case of something.

The worst case of what?

Well this thing here is called a Brownian bridge.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406153836611.png" alt="image-20220406153836611" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406154001302.png" alt="image-20220406154001302" style="zoom:50%;" />

Pivotal distribution..



So the Brownian motion is something

that looks like this, right?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406152737609.png" alt="image-20220406152737609" style="zoom:50%;" />

So you start at zero and you make those, like, you know,

tiny increments, and basically what's happening here,

this is a stochastic process.

**Why do I need a stochastic process here?**

Because here, I have something that's index by t.

All right?

So I have a random variable that's indexed by t

and I'm looking at its worst possible value.



We say, oh, you do whatever you want with this Gaussian stuff,

but at a time one, you have to be back at zero. what is called **Brownian bridge**.



When I look at the worst possible t on the real line,

I'm actually looking at the worst possible F of t times--

while I'm looking at the worst possible F of t and that

gives me precisely my Brownian bridge.

![image-20220407153941043](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220407153941043.png)

### Kolmogorov-Smirnov Test

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406155252279.png" alt="image-20220406155252279" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406155507498.png" alt="image-20220406155507498" style="zoom:50%;" />

Now, of course, I'm going to see a discrepancy.

The yellow curve is not the white curve.

And the question is how big those fluctuations should be.

And this is what Donsker is going to tell me.

It's going to say, in the worst case,

this is how far Fn can get to F, OK,



This is telling me that Fn minus F in the worst case

is going to be this guy divided by square root of n, OK?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406155601846.png" alt="image-20220406155601846" style="zoom:50%;" />

And so Donsker tells me that if you actually

had F instead of F0, this thing would

go to a supremum of the absolute value of a Brownian bridge, OK?

But now, I don't know what F is.



**how do you compute this thing?**

I mean, look at it.

I have to take the sup over R. That's

a big number to maximize over.

So one thing I could do is do grid R extremely thin.

At epsilon machine, though, even that--

I still would have to take care of the very large values.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406160811682.png" alt="image-20220406160811682" style="zoom:50%;" />

So per point, I have two possible **discrepancies**

that I need to look at.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406161213085.png" alt="image-20220406161213085" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406161248100.png" alt="image-20220406161248100" style="zoom:50%;" />

So this makes my life much easier

because now, I have only to look at the maximum of end values.

And so two end values, I guess.

The nice thing about the supremum of Brownian bridge is that it has a PDF

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406165158194.png" alt="image-20220406165158194" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406165232347.png" alt="image-20220406165232347" style="zoom:50%;" />

Pivotal distribution

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406170145228.png" alt="image-20220406170145228" style="zoom:33%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406171012532.png" alt="image-20220406171012532" style="zoom: 33%;" />
$$
x= F(t
$$
<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406171302837.png" alt="image-20220406171302837" style="zoom: 50%;" />

![image-20220406172221604](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406172221604.png)

### Quantiles of the Pivotal Distribution and P-values

![image-20220406173444881](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406173444881.png)





<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406173432569.png" alt="image-20220406173432569" style="zoom:33%;" />

K-S Table: https://www.real-statistics.com/statistics-tables/kolmogorov-smirnov-table/



![image-20220406174504785](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406174504785.png)

### Other Goodness of Fit Tests

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220406175508143.png" alt="image-20220406175508143" style="zoom:33%;" />

To say that two functions are close,

here we just said, well, they're close if they're

close at every point simultaneously.

So we looked at what's called the sup norm of the difference

between those functions, right?

So that's the **L infinity distance**

between random variables and that's

what led to Kolmogorov-Smirnov.



the second one

is called the L2 distance.

So this is actually the L2 squared distance.but this is actually not the distance you want

to use for a test statistic.

And the reason is because this would not give you

a pivotal distribution.

The distribution that you would get

if you were to actually measure this

would actually depend on F.



### Goodness of Fit Tests Continued: Kolmogorov-Lilliefors and QQ-Plots 

Everywhere here, we assumed that F0

was completely deterministic, and now we're

making F0 depend on our estimated parameters

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220407154105615.png" alt="image-20220407154105615" style="zoom:50%;" />

### K-L test

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220407154441373.png" alt="image-20220407154441373" style="zoom:50%;" />



Kolmogorov-Smirnov test was designed to test if the data **has a specific distribution**; it  is not useful for deciding whether or not the true distribution  lies in a given **family of distributions**. 

is pivotal

![image-20220408115110924](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220408115110924.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220408115245185.png" alt="image-20220408115245185" style="zoom:40%;" />

### Quantile-Quantile test

essentially

plots that give you quantiles on x and quantiles on y.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220407161753811.png" alt="image-20220407161753811" style="zoom:50%;" />

![image-20220407164040923](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220407164040923.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220407165905538.png" alt="image-20220407165905538" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220407170408877.png" alt="image-20220407170408877" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220407170613788.png" alt="image-20220407170613788" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220408123449585.png" alt="image-20220408123449585" style="zoom:50%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220408123501894.png" alt="image-20220408123501894" style="zoom:50%;" />

![QQ plot sketch diagram](https://i.stack.imgur.com/00mrt.png)

