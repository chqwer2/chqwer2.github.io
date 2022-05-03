# Lecture 8 EM

![image-20220301093859181](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301093859181.png)

![image-20220301215533434](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301215533434.png)

### Examples of Maximum Likelihood Estimators: Bernoulli Model

![image-20220301093805613](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301093805613.png)

Not Strickly Concave



### Examples of Maximum Likelihood Estimators: Poisson Model

![image-20220301094119143](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301094119143.png)

OK, that was a little less sweat, but still.





MLE of these three cases is actually equal to X$\bar X_n$.

### Maximum Likelihood Estimator of Gaussian Statistical Model: the mean

the derivative with respect to sigma,

but with respect to sigma squared

because that's the parameter.

![image-20220301094521313](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301094521313.png)

![image-20220301094600156](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301094600156.png)

### Maximum Likelihood Estimator of Gaussian Statistical Model: the Variance

And here, when I'm going to take the derivative with respect to **sigma squared**

![image-20220301221107185](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301221107185.png)

and plug-in $\hat \mu$ with the expectation $\bar X_n$

![image-20220301221302389](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301221302389.png)

### Maximum Likelihood Estimator of Uniform Statistical Model

There's actually a kink here.

There's even a discontinuity.

So not only is it not differentiable,

it's not even continuous.

![image-20220301095857257](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301095857257.png)

And this estimator just says, well, the last one should

be pretty close to lambda.

It's never going to be lambda, so I actually know--

I know something about my estimator.

It's always strictly less than lambda.

So in particular, it's going to be biased.

But it's actually a very good estimator.

It's closer.

But it's always under shooting.





### MLE of Mixture Gaussian





### Overview of the EM algorithm

Every time we wanted to compute a maximum likelihood estimator,

it happened that the likelihood or the log likelihood function

was a concave function.

And therefore to find its maximum, all we had to do

was to set its derivative equal to 0

and then to solve for the unknown parameter.



But how about not longer concave?

Maximizing non-concave functions is a notoriously hard problem

from a computational perspective.

And we're going to have to resort

to what's called an algorithm.

![image-20220301100755885](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301100755885.png)

### Complete observations

what I do is that I write it as the marginal density

or the marginal PMF of z ($p(z)$) times the conditional density

So p of z gives me straight up this one half.

All I'm doing here is factoring out 1 over square root 2 pi.

![image-20220301102213537](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301102213537.png)

![image-20220301102614136](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301102614136.png)

What I would do is that I would split male on the one hand

and female on the other hand and then compute the mean for each

of the subpopulations.

And this is what this is doing because if you

So here, I'm only summing over the xi's that corresponds to the first component. And this denominator here is just counting how many terms come from-- how many observations come from the first component. And here's the same thing. This is just the average over the xi's in the second 

![image-20220301103336404](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301103336404.png)

I don't know what the distribution of z given x is,

but I certainly know what the distribution of x given z is.

The distribution of x given z is equal to 1

is a Gaussian with mean mu 1.



And now a few things simplify.

So for example, I'm going to have that my 1/2s are

going to cancel.

My 1 over square root 2 pi are going to cancel. And in the end, I end up with just this simplified form.

### M-step

I'm going to plug them in my log likelihood.

Here they go-- w i, 1 minus w i.

Because this was z i, so I said I'm

going to replace z i by w i.

And now, this thing is something which is easy to maximize.

![image-20220301103440648](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301103440648.png)

So this is something that's very convenient for me.

I'm just taking some weights, weighted average of the x i's.

This is what I was doing before, except that I'm not entirely



![image-20220301103614656](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220301103614656.png)

### Lecture 9: Statistical Properties of the MLE

### Objectives



At the end of this lecture, you will be able to do the following:

- Derive the maximum likelihood estimator for the uniform statistical model and prove its consistency. 
- Recognize that the maximum likelihood estimator is consistent. 
- Compute the Fisher information of a statistical model 
- Establish asymptotic normality of a maximum likelihood estimator and compute its asymptotic variance using Fisher information 

### Consistency of the Maximum Likelihood Estimator 

And once I do this, which is really just one way, which

is taking the maximum of the likelihood, once I have this,

I would like you--

you might question whether this estimator is actually

a good estimator.

Is it unbiased?

Does it have small variance?

Does it have a small quadratic risk?

Is it consistent?



but remember, at some point, we did 

replace an expectation

by an average when we were on our way

to compute the maximum likelihood estimator.

The law of large numbers really just tells you

that averages converge to expectation.

And that's basically what justified this entire process

in the first place.

![image-20220304104907445](https://chqwer2.github.io/img/Typora/image-20220304104907445.png)

![image-20220304104920720](https://chqwer2.github.io/img/Typora/image-20220304104920720.png)

shifted by a constant

![image-20220304105037332](https://chqwer2.github.io/img/Typora/image-20220304105037332.png)

Now, what I'm actually telling you is that in the y-axis, those two things become the same.

But what I really want is that the arg

min this guy, which is theta hat here,

is actually becoming close to theta star on the x-axis.

So I need to translate the y-axis convergence

to an x-axis convergence.

And hopefully, this should work. (The last sentence in the pic)

![image-20220304105120081](https://chqwer2.github.io/img/Typora/image-20220304105120081.png)

And you know, things can go wrong when you have,

say, these discontinuous functions, when you

have weird things happening. But in general, it's actually fine

when you have nice, smooth functions.

![image-20220306150501540](https://chqwer2.github.io/img/Typora/image-20220306150501540.png)

![image-20220306150524254](https://chqwer2.github.io/img/Typora/image-20220306150524254.png)

Maximum likelihood estimators are often consistent estimators of the  unknown parameter provided some regularity conditions are met. Here, one such regularity condition does not hold; notably the support of the  distribution depends on the parameter. So we are resorting to the  definitions to prove consistency

https://stats.stackexchange.com/questions/370725/showing-maxx-i-is-the-consistent-estimator-for-pdf-fx%CE%B8-2x-%CE%B82

![image-20220306151912148](https://chqwer2.github.io/img/Typora/image-20220306151912148.png)

![image-20220306151925988](https://chqwer2.github.io/img/Typora/image-20220306151925988.png)



# Fisher Information

So what's also very nice about this family of estimates

is this method of estimation is that all the maximum likelihood

estimators come with theoretical guarantees

all at once under some regularity assumptions.



So we've already seen that since the log likelihood

is a consistent estimator of the negative KL

divergence of two constants.

![image-20220304105556180](https://chqwer2.github.io/img/Typora/image-20220304105556180.png)

defined in two possible ways.

![image-20220304105743160](https://chqwer2.github.io/img/Typora/image-20220304105743160.png)

needed to be twice differentiable.

![image-20220306160241005](https://chqwer2.github.io/img/Typora/image-20220306160241005.png)

quadratic means $\bar X_n^2$

### Equivalence between the two definitions of Fisher Information

I'm just going to say, OK, what does

it mean to take an expectation?

Well, it's just integrating this quantity here

against the density.

no need to multiply n

![image-20220304110648429](https://chqwer2.github.io/img/Typora/image-20220304110648429.png)

![image-20220304110956651](https://chqwer2.github.io/img/Typora/image-20220304110956651.png)

![image-20220304111742729](https://chqwer2.github.io/img/Typora/image-20220304111742729.png)

and missing a lecture video here..

### Fisher Information of the Bernoulli Random Variable

![image-20220304111852470](https://chqwer2.github.io/img/Typora/image-20220304111852470.png)

but I can promise you that procrastination does not pay.

![image-20220304112332418](https://chqwer2.github.io/img/Typora/image-20220304112332418.png)

So the first thing that I can do is

to compute the variance of this quantity.

factor out x, so we have a times x plus b.

And the variance of a times x plus b

will be a squared times the variance of x,

which is p 1 minus p.



![image-20220304112912702](https://chqwer2.github.io/img/Typora/image-20220304112912702.png)

![image-20220304113216620](https://chqwer2.github.io/img/Typora/image-20220304113216620.png)

So I have two ways of computing it.

You pick your favorite one.

So here it's not super illustrative

that the second one is actually the fastest one,

but it often is the case that the second one is the fastest

one. And the main reason is because in the end,

you can just push your expectation everywhere

you want.

**Fisher Info of Binomial**

![image-20220306161612022](https://chqwer2.github.io/img/Typora/image-20220306161612022.png)

![image-20220306162336970](https://chqwer2.github.io/img/Typora/image-20220306162336970.png)

![image-20220306162325274](https://chqwer2.github.io/img/Typora/image-20220306162325274.png)

### Asymptotic normality of the maximum likelihood estimator

![image-20220304113426157](https://chqwer2.github.io/img/Typora/image-20220304113426157.png)

![image-20220304113452935](https://chqwer2.github.io/img/Typora/image-20220304113452935.png)



So this is an important one because these are actually

nice setups where we can compute, for example,

the quadratic risk, but for which we do not

have this asymptotic normality.

In fact, the result is better than asymptotic normality.

Asymptotic normality gives us a square root

of n convergence rate.

And, in that case, we typically have a n rate of convergence,

so an order of magnitude better.

![image-20220304113946650](https://chqwer2.github.io/img/Typora/image-20220304113946650.png)

For a large collection of distributions

of statistical models, I can actually

make a blanket statement about the fact

that the maximum likelihood estimator is consistent

and also that it's asymptotically normal.

What's also quite interesting is that I

have a functional way of computing

what the asymptotic variance is going to be.



There's a variety of techniques that we have,

but they're all ad hoc.

Based on what the form of the maximum likelihood estimator

is, we can compute its asymptotic variance.

Here this is kind of a magical tool.

It says, well, all you have to do

is to compute the Fisher information.

We have two ways to do this.

Either it's the variance of l prime of theta,

or it's minus the expectation of l prime prime of theta.

We just compute this.

This is just a simple calculus exercise.

And then 1 over the quantity that we

get evaluated at theta star is precisely

the asymptotic variance.

So this is really a remarkable result.



is asymptotically normal with asymptotic variance given by 1

over the Fisher information at theta star,

### An idea of the proof of asymptotic normality.

So there are two questions here.

The first one is, well, the maximum likelihood

is not necessarily an average or even a function of an average.

So how does asymptotic normality show up?

The only way we know how to prove asymptotic normality

is by using the central limit theorem.

So to answer this question, it turns out

that there is an average that's hidden.

So to answer this question, it turns out

that there is an average that's hidden.

It's hidden when we talk about the log likelihood.

So the rescaled log likelihood will converge to a Gaussian,

and that's where it's coming from.



The second question is, where does the Fisher information

show up?

How does the Fisher information or 1 over the Fisher

information end up being the asymptotic variance

of the maximum likelihood?

![image-20220304114929591](https://chqwer2.github.io/img/Typora/image-20220304114929591.png)

![image-20220304115448863](https://chqwer2.github.io/img/Typora/image-20220304115448863.png)

![image-20220304115822535](https://chqwer2.github.io/img/Typora/image-20220304115822535.png)

### Recitation

In this recitation, we're going to look

at how we can compare estimators using mean squared error.

The setup for these problems is that we

observe x1 to xn, which are random variables that



![image-20220304161213268](https://chqwer2.github.io/img/Typora/image-20220304161213268.png)

And the main idea is that you see this decomposition of mean squared error into variance and bias.

And a lot of the time we work with unbiased estimators,

right?

So the expectation of my estimator

just equals the true parameter.

So the bias is 0, which means that my mean squared error is

just the variance of my estimator, theta hat.

Now the idea behind **shrinkage estimators**

is that maybe I could trade some of my variance

for a little bit of bias and make my mean squared error even smaller than my unbiased estimator was.



### Comparing Two Estimators for the Poisson Parameter



### Inference for the variance of a Gaussian distribution

$\alpha$ is an unbiased estimator

![image-20220304162108493](https://chqwer2.github.io/img/Typora/image-20220304162108493.png)

### Comparing Two Estimators for the Upper Limit of the Uniform Distribution I 

![image-20220304162657406](https://chqwer2.github.io/img/Typora/image-20220304162657406.png)

b estimator is biased, because its expectation is not equal to $\theta$

### Comparing Two Estimators for the Upper Limit of the Uniform Distribution I 

![image-20220304163645346](https://chqwer2.github.io/img/Typora/image-20220304163645346.png)

OK, you see that, even though the maximum of the x's is

a biased estimator, as n goes to infinity, or as n is large,

this is actually going to be much smaller--

sorry-- than the MSE here.

### Relative Efficiency of Estimators

Compare MSE between two unbiased estimators

Now, something we use to compare the MSEs of unbiased estimators

it's called the relative efficiency.

![image-20220304163959831](https://chqwer2.github.io/img/Typora/image-20220304163959831.png)

One thing you can do with biased estimator.

You might have to scale it a little bit to find an unbiased estimator, 

### shrinkage estimators

![image-20220304164757118](https://chqwer2.github.io/img/Typora/image-20220304164757118.png)

So what we see is that the MSE of this a xn bar

actually is smaller than the MSE of xn bar

when we take a to be a little bit less than 1.



And the reason we call this a shrinkage estimator

is that this number $a$ is a number slightly less than 1.



And so what we're doing is we're taking our sample mean,

we're shrinking it a little bit towards 0,

and adding a little bit of bias.

But by adding this bias, we're actually

decreasing the variance by a lot more than we add in the bias.



as well, that applying some slight shrinking

to my estimator will actually reduce

the MSE over the unbiased estimate.



Maybe you really prefer that your estimator is unbiased.

And if that's the case, then you just

want to find the estimator that's

most efficient overall unbiased estimators.

That goes back to part 2, where we looked

at those relative efficiencies.

However, if you're willing to actually add

a little bit of bias to your estimator, what you can see

is that we can actually get smaller MSE's and a little bit

better performance than if we just

considered the standard sort of unbiased estimators.



### EM examples

only takes 3 values (1,2,3)

![image-20220311170352651](https://chqwer2.github.io/img/Typora/image-20220311170352651.png)

Estep output the probability

![image-20220311171724834](https://chqwer2.github.io/img/Typora/image-20220311171724834.png)

M-step

![image-20220311171553453](https://chqwer2.github.io/img/Typora/image-20220311171553453.png)

![image-20220311223647262](https://chqwer2.github.io/img/Typora/image-20220311223647262.png)
