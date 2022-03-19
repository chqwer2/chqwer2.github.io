### Lecture 5: Confidence Intervals and Delta Method

Confidence Intervals Concept Checks Continued





![image-20220214093714487](https://chqwer2.github.io/img/Typora/image-20220214093714487.png)

### Modeling Inter-arrival Times of a Subway System

![image-20220214100343476](https://chqwer2.github.io/img/Typora/image-20220214100343476.png)

what is the probability that T exceeds T plus S given

that T exceeds T.

Given that I've waited already T minutes,

what is the probability that I need

to wait an extra S minutes?

![image-20220214100321581](https://chqwer2.github.io/img/Typora/image-20220214100321581.png)



So the probability that I need to wait S more minutes given

that I've already waited t minutes

is actually just the same as if I start from scratch

and I have to wait for S minutes.

And that's this memoryless property, lack of memory.

The probability that I wait five more minutes

after waiting 10 minutes is the same as probability waiting

for five minutes from scratch.

### Estimating the Parameter for an Exponential Model

So it's biased, but it's still consistent.

![image-20220214101829791](https://chqwer2.github.io/img/Typora/image-20220214101829791.png)

So it is not an unbiased estimator

by Jensen's inequality, like we saw last time.

One over x is a complex function.

So the expectation of this guy is certainly

not one over the expectation of T n bar.

Is it going to be larger or smaller?



The expectation will be larger, right?

Because this is one over x.

The expectation is this little chord,

so the chord is above it.

So the expectation of one over T n bar

is larger than one over the expectation of T n bar,

which is lambda.

So it's biased, but it's still consistent.

![image-20220214101850358](https://chqwer2.github.io/img/Typora/image-20220214101850358.png)

### The One-Dimensional Delta Method

I want to see:

![image-20220214102316726](https://chqwer2.github.io/img/Typora/image-20220214102316726.png)

But I get:

![image-20220214102443720](https://chqwer2.github.io/img/Typora/image-20220214102443720.png)

So the **delta method**

Now we have g($\cdot$), under the assumption than g’(theta) is continuous, means continuously differentiable.

![image-20220216113459796](https://chqwer2.github.io/img/Typora/image-20220216113459796.png)

Is 1/x^2 continuously differentiable function?





So let's see what could be the asymptotic variance.

So just the Taylor expansion after.

![image-20220214103133901](https://chqwer2.github.io/img/Typora/image-20220214103133901.png)



What is the order of magnitude of z n

minus theta from the first line that you see up there?

Roughly?  1/n

![image-20220214103435419](https://chqwer2.github.io/img/Typora/image-20220214103435419.png)

![image-20220214103502507](https://chqwer2.github.io/img/Typora/image-20220214103502507.png)

### Applying the Delta Method

But theta, in all the examples where

we're going to want to apply the delta method,

is not the parameter of interest.

It is the function of the parameter

that we're trying to actually infer.

![image-20220214105427841](https://chqwer2.github.io/img/Typora/image-20220214105427841.png)

![image-20220214105449124](https://chqwer2.github.io/img/Typora/image-20220214105449124.png)

There's going to be one caveat, which

is that just like for the Bernoulli proportion p,

my variance depends on my unknown parameter.

So we will have to also solve this.

![image-20220214105848507](https://chqwer2.github.io/img/Typora/image-20220214105848507.png)

![image-20220214110105147](https://chqwer2.github.io/img/Typora/image-20220214110105147.png)

Plug-in ![image-20220214110340321](https://chqwer2.github.io/img/Typora/image-20220214110340321.png)

### Frequentist Interpretation of a Confidence Interval

![image-20220214110605795](https://chqwer2.github.io/img/Typora/image-20220214110605795.png)

Lambda is the reciprocal of the expected waiting time,

not the waiting time but the expected waiting time itself.

![image-20220214110817142](https://chqwer2.github.io/img/Typora/image-20220214110817142.png)

5: The frequentist approach is often contrasted with the bayesian approach



the proportion of time the true parameter belongs

to this interval, if I repeat this experiment,

say, m times as m goes to infinity,

this number goes to 95%.

So that's the frequentist thing.

### Introduction to Hypothesis Testing

It really is the engine of data-driven scientific

discovery.

yes or not question.





### Recitation

Consider a sample of $n$ i.i.d. continuous random variables $X_{1}, \ldots, X_{n}$ with density
$$
f(x)=e^{-(x-a)} \mathbf{1}_{x \geq a}
$$
where $a \in \mathbb{R}$ is an unknown parameter.
1. Find an estimator $\hat{a}$ for the unknown shift parameter $a$.
2. Determine the (asymptotic) distribution of $\hat{a}$.
3. Compute confidence intervals for $a$ based on $\hat{a}$
4. Compare results with a different estimator of the same parameter $a$.
5. $\mathbb 1$ is indicator function

So in this whole confidence interval number

one will be asymptotic.

That means we'll be content with having results

that need large sample sizing.

![image-20220216164221922](https://chqwer2.github.io/img/Typora/image-20220216164221922.png)

![image-20220216164746629](https://chqwer2.github.io/img/Typora/image-20220216164746629.png)

![image-20220216165255698](https://chqwer2.github.io/img/Typora/image-20220216165255698.png)

Another idea of estimator for a



Remember what our model looks like.

We draw from exponential distributions

that are shifted by a.

That means all our samples will fall in the region

from a to infinity.



So that means I for sure know that a needs

to be less or equal than all of my samples.

So why don't I just pick the minimum of all my samples

and let that be my estimator?



![image-20220216211059576](https://chqwer2.github.io/img/Typora/image-20220216211059576.png)

This is much faster than the one over square root of n

we had here, which is a particular effect of the model

we are postulating.

**Comparing the two estimators**

The first one:

a rate of 1 over square root of n

or a size of confidence interval of 1 over square root of n,

while, for A2 hat, this is an approach that's specifically

tailored to the model.



Well, maybe it will apply to other problems--

namely, whenever I actually have a distribution that

is only one-sided in nature, such as the one we were looking

at.



And the estimator-- the parameter to be estimated

is actually the location of the start of the distribution,

so to speak.

Estimator 2 Because this estimator can be very non-robust against

outliers.

![image-20220216211729257](https://chqwer2.github.io/img/Typora/image-20220216211729257.png)

### Exercise

Confidence Intervals for Curved Gaussian Family

### **asymptotic** variances



indicator functions

![image-20220216224832949](https://chqwer2.github.io/img/Typora/image-20220216224832949.png)



Var[g(x)]=g’(mu)Var(x)

![image-20220216231221004](https://chqwer2.github.io/img/Typora/image-20220216231221004.png)

![image-20220216231346596](https://chqwer2.github.io/img/Typora/image-20220216231346596.png)
