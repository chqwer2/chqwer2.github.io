# Lecture 3 Parametric Statistical Models

### Inference

3 fundamental aspects: **estimation, confidence intervals, and hypothesis testing**.

Estimation produces a single number, say 69%.

Confidence intervals produce error bars around this number.

And finally, will lay the foundations of statistical hypothesis testing, which is the basis of data-driven scientific inquiry.

A **statistic**  is any measurable function of the sample. An **estimator**  of  is a statistic  whose expression **does not** depend on . 

![image-20220211212442595](https://chqwer2.github.io/img/Typora/image-20220211212442595.png)



we'll really do a deep dive into statistics.

But it's really the three main questions

that are recurrent every time you

get data, the three types of questions that you may ask.

##### Trinity of Statistical Inference

![image-20220204204242267](https://chqwer2.github.io/img/Typora/image-20220204204242267.png)

**Estimation:** If I knew this, if I have a good estimator,

then I get a good idea of what the probability distribution is for the entire population, the thing that

generates the data itself.

estimator $\bar R_n$



Once you have this estimator, you

might want to have a confidence interval,

some error bars around the number that you get.

**Confidence:** 

So that's version 2.0 of the estimator.

![image-20220204204711989](https://chqwer2.github.io/img/Typora/image-20220204204711989.png)

'm going to give you a range just to make sure that you understand that I'm not entirely sure about the number

that I computed, because they computed it only after 124 numbers after all.

And if I had a million, maybe I would have a much narrower confidence interval.

**Hypothesis Testing**

What hypothesis testing is trying to do as a statement is we find statistical evidence

namely, yes/no answer.

Yes! we find statistical evidence, or no we don’t.

But why you want to narrow down to this simple yes/no answer?  which seems provide less information.

Well, because most of the time, that's all we care about.

People want to have this to understand.

“Yes, people are running faster this year with the new Nike

### An example of a statistical modeling

![image-20220204210842717](https://chqwer2.github.io/img/Typora/image-20220204210842717.png)

all x are IID distributed according to some distribution.

What is PMF?

probability mass function



Modeling:

I'm going to propose a candidate distribution that

can model integer numbers between zero and infinity, say.

**Poission**

![image-20220204211809218](https://chqwer2.github.io/img/Typora/image-20220204211809218.png)

$X - 1 \~ Poiss(\lambda)$, now we have to learn one parameter

So what happens is that now I can pool all my observations to contribute to learning one parameter

rather than dividing them.

**The rule of thumb** is if you need to learn two parameters,

you need twice as much observations.



Why you would want to collapse your completely vague PMF, which is seven parameters in this case, but could really be an infinite number of parameters if I didn't lump all these last guys into learning

one simple parameter.

And if I learned lambda, and if this is actually

a good approximation of the two PMF,

then I actually get the entire numbers that I want.

For example, here's one that I can make.

I take the absolute value of a Gaussian,

and I round it to the nearest integer.

That's another distribution.

### Statistical model: definition

Here I said, you know, I want to replace

my PDF by a particular statistical model, which was

in this case a Poisson model.

![image-20220206205709144](https://chqwer2.github.io/img/Typora/image-20220206205709144.png)

So keep in mind that when I ask you

what is the statistical model, the answer should always

be a pair.

There should be two things in your answer.

And the first one is E, which is this guy, which

is the space on which you know your random variables live.

And of course you could be vague, because I just told you

that E is always a subset of R. But you should

be as precise as possible.

You could tell me that my integer random variables live

in R. It's true technically, but it's not as precise as it gets.

The second one is a family of probability distributions.



So if you pay careful attention, I'm

saying that a statistical model is a pair.

But really, it's really three things.

It's the sample space.

It's the form of the distribution

as a function of theta.

And it's also the candidate thetas that I want you to have.

### Types of Statistical Models

##### Parametric, nonparametric, and semiparametric models





OK, so well specified just means that it actually

can reach the actual distribution that you have.



The parameter space is where my parameter lives, OK?

And so we're typically going to assume that theta

is a subset of RD, OK?

That means that theta contains vectors

of dimension D. When this is the case,

we call this model parametric.



All it means-- nonparametric doesn't

mean that there's no parameter.

It sounds like that would be the right thing.

I mean, things with no parameter.

It just means that the parameter is itself infinite dimensional.

All probability distributions, that's infinite dimensional.

But even if I reduce the space of all probability measures

to a smaller infinite dimensional space,

you still have to do more work than if you had

a finite dimensional problem.

OK, so in this case, this is called nonparametric.

##### semiparametric model

What is semiparametric?

Well, it's when you're theta has two components.

When you're theta is actually, for example, something

of the form, let's say PF.

Where P is a number between zero and one.

That's it from a Bernoulli, and F is a function.

All right, a function typically lives

in an infinite dimensional space.

A number between zero and one is a parametric set,

so this is basically-- there's two things in the thing

that you want to learn.

##### Examples of parametric and nonparametric models

![image-20220206224549145](https://chqwer2.github.io/img/Typora/image-20220206224549145.png)

left is sample space, right is distribution.

$\mathbb N$ for non-negative intergers, $\mathbb R$ for real numbers

$N_d$ is d-dimensional Gaussian random variable

$I^d$ for d-dimensional Indentities

### Mixtures of Gaussians

Prof Rigollet: So I would like now to introduce

a new family of probability distributions called Mixtures

of Gaussians.

This is a pure probability question.

useful In particular, modeling in the case

when we have subpopulations, heterogeneous subpopulations.

![image-20220206224858196](https://chqwer2.github.io/img/Typora/image-20220206224858196.png)

![image-20220206225047442](https://chqwer2.github.io/img/Typora/image-20220206225047442.png)

![image-20220206225416673](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\_posts\image-20220206225416673.png)

It is not symmetric.

![image-20220206225651611](https://chqwer2.github.io/img/Typora/image-20220206225651611.png)

It is unimode, This is to be compared with multimodal or bimodal

or trimodal.

![image-20220206225728836](https://chqwer2.github.io/img/Typora/image-20220206225728836.png)

So we can, of course, make multimodal distributions

appear within the class of mixtures of Gaussians.

if we're mixing two Gaussians.

And the way to do this is simply to spread the means more,

compared to the size of the variances.

![image-20220206225857878](https://chqwer2.github.io/img/Typora/image-20220206225857878.png)

##### Another representation of Gaussian Mixtures

![image-20220206213426538](https://chqwer2.github.io/img/Typora/image-20220206213426538.png)

First, I'm going to draw what is called a latent variable. So latent here means that I don't get to observe it. And it's going to be called z.

### Mixture of Gaussians Model

![image-20220208195832406](https://chqwer2.github.io/img/Typora/image-20220208195832406.png)

Often we say, well there's almost too

much flexibility in this family of distributions.

So we're going to start fixing some parameters to some values

that we like.

For example, we could fix the variances.

So if we fix, for example, the variances to be equal to 1, then we can see that now all we have to fit is the center, is the weight on the first one and the two centers, so

the two means, u1 and u2.

![image-20220209095347521](https://chqwer2.github.io/img/Typora/image-20220209095347521.png)

or the above computations, do you have to assume that X1 is independent of X2? 

[What is the variance of the weighted mixture of two gaussians?](https://stats.stackexchange.com/questions/16608/what-is-the-variance-of-the-weighted-mixture-of-two-gaussians)

Using these formulae, , the variance can be written



Var(*f*)=*μ*(2)−(*μ*(1))2=∑*i**p**i**μ*(2)*i*−(∑*i**p**i**μ*(1)*i*)2.

![image-20220209095736384](https://chqwer2.github.io/img/Typora/image-20220209095736384.png)

  This allows us to understand the formula as stating **the variance of the mixture is the mixture of the variances \*plus\* a non-negative term accounting for the (weighted) dispersion of the means.**



##### Examples of nonparametric models

![image-20220209085645486](https://chqwer2.github.io/img/Typora/image-20220209085645486.png)

But if I start telling you something specific shape of the distribution…

![image-20220209090205712](https://chqwer2.github.io/img/Typora/image-20220209090205712.png)

But all I'm telling you is that there's just two pieces.

One is going up, the other one's going down. ?? 





Desmos?

![image-20220209092624152](https://chqwer2.github.io/img/Typora/image-20220209092624152.png)



<img src="https://chqwer2.github.io/img/Typora/image-20220209092925117.png" alt="image-20220209092925117" style="zoom:67%;" />

Note that the sample space of  is *not unique*. For example, if , then both  and  can serve as a sample space. However, in general, we associate a random variable with its smallest possible sample space (which would be  if ). 





 m entries of the vector  theta ? m-dimensions? 

![image-20220209111444548](https://chqwer2.github.io/img/Typora/image-20220209111444548.png)

![image-20220209111455200](https://chqwer2.github.io/img/Typora/image-20220209111455200.png)

### Identifiability

Injectivity

OK, so maybe you don't remember exactly what injectivity means.

But what it means is that if I give you

two parameters to start from, I'm

going to end up with two distributions that

are different.

![image-20220209112356329](https://chqwer2.github.io/img/Typora/image-20220209112356329.png)

![image-20220209112506215](https://chqwer2.github.io/img/Typora/image-20220209112506215.png)

Cuz we have:
$$
\frac{\mu}{\sigma} = -\Phi^{-1}(1-p)
$$
and it is empirical porpotion

![image-20220209113518647](https://chqwer2.github.io/img/Typora/image-20220209113518647.png)



So this one is not the one you want.

So it's just a matter of how you want to write your model.

There's many models that are possible.

And some are identifiable.



Alternatively: a function is injective if we can **uniquely** recover some input $x$ based on an output $Y= f(x)$. 



![image-20220209113837866](https://chqwer2.github.io/img/Typora/image-20220209113837866.png)

The notation  denotes that  is a function, also called a **map** , defined on all of a set  and whose outputs lie in a set . A function  is **injective**  if for all ,  implies that . 



# Lec 4. Parametric Estimation and Confidence Intervals

At the end of this lecture, you will be able to 

- Distinguish between an **estimator**  and a **statistic** . 
- Compute the **bias** , **variance** , and **quadratic risk**  of an estimator. 
- Determine whether or not an estimator is **consistent** . 
- Construct a confidence interval for an unknown parameter. 
- Explain the frequentist interpretation of the confidence interval. 

### Statistics, Estimators, Consistency, and Asymptotic Normality

A **statistic**  is any measurable function of the sample. An **estimator** $\theta$ of  is a statistic $\hat \theta_n=\hat \theta_n(X_3,\cdots,X_n)$  whose expression **does not** depend on $\theta$. 

Recall that a statistic, loosely speaking, is a function of the data that can  be easily computed. Recall that an estimator is a special kind of  statistic, specifically one that does not depend on the unknown  parameter $\theta$.

The most natural question is, can I find which one is the correct distribution?

To identify it, if your model is both well specified

and identifiable, you can just go ahead

and identify the correct data.



Estimator

In particular, I need to rule out statistics that

depend on things I don't know. because I

want to be able to compute it as an estimator once I get data.





what's going to be the goal of this section,

will be to understand its properties

and how good of an estimator it is.



![image-20220209154925211](https://chqwer2.github.io/img/Typora/image-20220209154925211.png)

So I decide to use the word "asymptotic variance" (渐近的)

to denote the variance of theta hat n,

but once rescaled by the square root of n,

so that I have something that's meaningful

and not always equal to 0.



![image-20220213172924705](https://chqwer2.github.io/img/Typora/image-20220213172924705.png)

?

**Exercise**

By the weak law of large numbers, $\frac{1}{n} \sum_{i=1}^{n} X_{i} \rightarrow \mathbb{E}\left[X_{1}\right]=\theta$ in probability, so this is the correct choice.

By the weak law of large numbers, $\frac{1}{n} \sum_{i=1}^{n} X_{i} \rightarrow \mathbb{E}\left[X_{1}\right]=\theta$ in probability, so this is the correct choice.
From the previous question, the first and last choice, $\theta$ and $\frac{1}{n} \sum_{i=1}^{n} X_{i}-\theta_{1}$ are not even estimators, so these options are incorrect. Since $\theta \neq 4.2$, this estimator cannot be consistent. Finally, there is no guarantee that $\sum_{i=1}^{n} i^{2} X_{i}^{i}$ converges to $\theta$. In fact, for many choices of distribution, this statistic will diverge to $\infty$.





For *asymptotically normal*

![image-20220211215002233](https://chqwer2.github.io/img/Typora/image-20220211215002233.png)

Let $\sigma=\sqrt{p}(1-p)$ denote the common standard deviation of $X_{1}, \ldots, X_{n} .$ By the central limit theorem,
$$
\frac{\sqrt{n}}{\sigma}\left(\bar{X}_{n}-p\right)=\frac{\sqrt{n}}{\sigma}\left(\frac{1}{n} \sum_{i=1}^{n} X_{i}-p\right) \rightarrow N(0,1)
$$
where the convergence is in distribution. As a result, we see that for $c<1 / 2$,
$$
n^{c}\left(\bar{X}_{n}-p\right)=\frac{\sigma}{n^{1 / 2-c}} \frac{\sqrt{n}}{\sigma}\left(\bar{X}_{n}-p\right) \approx \frac{\sigma}{n^{1 / 2-c}} N(0,1) \rightarrow 0
$$
in probability as $n \rightarrow \infty .$ Hence, $c=1 / 2$ is the smallest possible value of $c$ such that
$$
n^{c}\left(\bar{X}_{n}-p\right)=n^{c}\left(\frac{1}{n} \sum_{i=1}^{n} X_{i}-p\right)
$$
does not converge to 0 in probability as $n \rightarrow \infty$.

Remark: As defined in the third video in this section, this implies that the estimator $\bar{X}_{n}$ is $\sqrt{n}$ -consistent. This means that the estimator $\bar{X}_{n}$ converges to the parameter at a relatively fast rate, so this gives us something stronger than just consistency.



### Bias Estimators and an application of Jensen's Inequality

I'm going to want to talk about it in terms of how far it is from theta and how much variability it has.

How close is it to theta?

theta is what you want to find.

![image-20220211222602955](https://chqwer2.github.io/img/Typora/image-20220211222602955.png)

Here's one way to measure this. What I want to know is how close theta hat n is from theta in expectation.

This difference, which is the expectation of theta hat n minus theta, will be called the "bias." 


$$
bias(\hat \theta) = \mathbb E[\hat \theta] - \theta
$$
![image-20220211221758223](https://chqwer2.github.io/img/Typora/image-20220211221758223.png)

![image-20220213165154957](https://chqwer2.github.io/img/Typora/image-20220213165154957.png)



**Why EXiXj = …..?**



But sometimes we prefer biased distribution because it's going to consistently give you values that are much closer to theta than this unbiased estimator, theta hat.

![image-20220210102117858](https://chqwer2.github.io/img/Typora/image-20220210102117858.png)



![image-20220213164346206](https://chqwer2.github.io/img/Typora/image-20220213164346206.png)

hint: rescale



Second one is also unbiased, but although Unbiasedness is a good thing, it's certainly not doing everything you want.



4. Well, the beauty of this is that the square root of a Bernoulli

   is a Bernoulli.

   That's the beauty with 0, 1.

   The square is a Bernoulli, and the square root is a Bernoulli.

Be a little careful when you see nonlinear functions,

because you're tempted to say that the expectation

of this function is the function of the expectation, which

is not true.

##### Jensen’s inequality

$f(\cdot)$ is convex, or concave
$$
E f(x)\geq f(E(x))
$$
![image-20220210103728712](https://chqwer2.github.io/img/Typora/image-20220210103728712.png)

![image-20220211223616612](https://chqwer2.github.io/img/Typora/image-20220211223616612.png)

It could be that those two are actually equal.

You're not really telling me anything.

But it turns out that if this function is really, truly

concave, meaning that at no point is it flat like this.





![image-20220210103938170](https://chqwer2.github.io/img/Typora/image-20220210103938170.png)

The way I remember which way Jensen goes

is that this chord here represents

all possible expectations that you

can get when you have a random variable that

takes two values, this guy and this guy with probability p,

and this guy with probability 1 minus p.

When you change p, you're actually

changing the expectation along this line.

All that Jensen is telling you is

that, well, if you have a convex function,

then this line is above the function

itself, which is precisely the definition of a convex

function.

**Unbiased estimators**

An unbiased estimator is a special kind of estimator; an estimator is a  special kind of statistic. Any statistic has to be measurable, which is  loosely defined in the lecture as 'if you can compute it exactly once  given data'. Can you *exactly* compute the *expectation* of the sample mean? ;)



### Variance of Estimators

![image-20220210150836145](https://chqwer2.github.io/img/Typora/image-20220210150836145.png)

**Video Note** :



1. 

Everybody remember this formula about variance of averages?

You can think of the variance of the sum, which

is the sum of the variance. So three unbiased estimators, but three different variances.

![image-20220210151233772](https://chqwer2.github.io/img/Typora/image-20220210151233772.png)

### Quadratic Risk of Estimators

Now we have bias and variance.

Now it turns out there's a very natural way of combining bias and variance:

**Quadratic Risk **= Var($\hat \theta$) + Bias($\hat \theta$)^2 + 0

denoted as 
$$
\mathbb E[(\hat \theta_n-\theta)^2]
$$
So it's trying to achieve having low bias and low variance

at the same time.

But rather than saying, oh, I'm going to take my bias

and multiply it by my variance and minimize the product

or take the bias and add the variance

and minimize those two things, what I do is I say,

OK, I want theta hat n to be close to theta.

And I don't care whether theta hat n is close from above

or close from below.

I'm just going to take the square of this distance



![image-20220210152253383](https://chqwer2.github.io/img/Typora/image-20220210152253383.png)

First is variance, second is expectation of deterministic square of bias. 

### Worked Example: Bias, Variance and Quadratic Risk

Yeah, so the variance of a uniform on the interval 0,

1, which is the same as the variance

on any uniform on an interval of size 1, is 1/12.

So this is equal to 1/12 n.
$$
Var(\bar X_n) = \frac{Var(X_1)}{n}
$$
![image-20220210153005617](https://chqwer2.github.io/img/Typora/image-20220210153005617.png)

 I want you to think a little bit about the meaning

of the quadratic risk.

![image-20220212201213335](https://chqwer2.github.io/img/Typora/image-20220212201213335.png)

All right, so this is close and it's getting closer

as my sample size increases.

![image-20220212201540950](https://chqwer2.github.io/img/Typora/image-20220212201540950.png)

![image-20220212201929805](https://chqwer2.github.io/img/Typora/image-20220212201929805.png)

![image-20220212201940860](https://chqwer2.github.io/img/Typora/image-20220212201940860.png)



### Confidence Intervals

Confidence Interval for the Kiss Example
$$
I(\tilde x) = [lower, upper]
$$
can you build error bars around this estimator?

Oh, and we saw asymptotic normality.



So confidence intervals will actually

help us use this asymptotic normality to build error bars.

So I'm going to give you an interval, two error bars.

And the probability that my theta is between those two

error bars will be at least 1 minus alpha,

will be at least 95%.

![image-20220211210656255](https://chqwer2.github.io/img/Typora/image-20220211210656255.png)

So now, of course, everything typically

relies on the central limit theorem.

And so I cannot really make statements that are valid

for finite sample size.

So what I'm going to do is I'm going

to talk about asymptotic confidence interval--

confidence intervals that typically arise from applying

the central limit theorem.

you say, the probability that my random interval contains theta,

![image-20220211210756289](https://chqwer2.github.io/img/Typora/image-20220211210756289.png)

![image-20220211211026822](https://chqwer2.github.io/img/Typora/image-20220211211026822.png)

And from the central limit theorem,

we know that this estimator is--



why needs sqrt(n) here?



asymptotically normal.

That was the definition that we had.

The central limit theorem typically

gives you asymptotic normality.

So what is it, asymptotic variance?

Is it 1?

Did I write something that was like square root of n Rn

bar minus p goes to N 0, 1?

Because that's the definition of the asymptotic variance.

So what is the asymptotic variance?

It's p 1 minus p.



What I'm asking is the probability

that the absolute value of Rn bar minus p exceeds x.

Why do I want this?

Because-- well, if I can tell you

this, if I can tell you a little x

is what I have on the right-hand side is about 1 minus alpha,

then I have myself error bars, which are of the form Rn bar

plus/minus this little x.

![image-20220211211546323](https://chqwer2.github.io/img/Typora/image-20220211211546323.png)

![image-20220211211727757](https://chqwer2.github.io/img/Typora/image-20220211211727757.png)

12mins…

![image-20220212175111236](https://chqwer2.github.io/img/Typora/image-20220212175111236.png)

Well, technically, it's the quantile of order 1 minus alpha

over 2, but we denote it only with alpha over 2,

![image-20220212175406225](https://chqwer2.github.io/img/Typora/image-20220212175406225.png)

Because it depends on p, or p factorial,

just an exclamation mark.

So it depends on p.

And I cannot do that, because if you give me data,

I can not build error bars, because there's this p here.

So what do I do?

Well, good news-- there's three ways to fix this.

![image-20220212181030515](https://chqwer2.github.io/img/Typora/image-20220212181030515.png)

![image-20220212180801501](https://chqwer2.github.io/img/Typora/image-20220212180801501.png)

And the thing is that the widest confidence interval

I'm going to get is precisely the one for which p 1 minus p

is maximum, and that's the value for which p is equal to 1/2.

And therefore, if I plug-in 1/2 here,

I'm going to have the widest possible confidence interval.

And now, this gives me a conservative asymptotic

confidence interval or a conservative confidence

interval at a asymptotic level 1 minus alpha.

And therefore, when I look at the limit of the probability

that this confidence interval, which I can now compute,

so it's therefore a valid confidence

interval, the probability that this guy contains p,

well, it's not exactly equal to 1 minus alpha

but it's at least larger than or equal to 1 minus alpha.

##### I Solve

![image-20220212182355339](https://chqwer2.github.io/img/Typora/image-20220212182355339.png)

![image-20220212233920162](https://chqwer2.github.io/img/Typora/image-20220212233920162.png)

So what happens is when I actually

write this inequalities, I have a set of two inequalities.

And if I square them, I have a set

of two quadratic inequalities in p.

That's just the way things are for a Bernoulli.

Now it's not going to be as nice for other things,



Now let me collect my terms in p squared.

OK, and this is a bona fide quadratic inequality, OK?

![image-20220212182227487](https://chqwer2.github.io/img/Typora/image-20220212182227487.png)

##### Using Slutsky Theorem: Plug-in

But the minute you want to do plug-in,

which is put a hat on stuff you don't know,

don't do that in public.But what's happening is that you can actually

just call this Slutsky.

But this one is actually valid, we call it a plug-in confidence

interval

![image-20220213110202581](https://chqwer2.github.io/img/Typora/image-20220213110202581.png)





![image-20220212183113773](https://chqwer2.github.io/img/Typora/image-20220212183113773.png)

The third one is to say, OK, I don't know p,

but I certainly have an estimator for p.

It's p-hat. And I knew that this p-hat is consistent.

So if I'm already in the regime where

I'm talking about the central limit theorem,

then I'm in regime where p-hat should be close to p.

So I might as well just replace p by p-hat.

Continuous mapping theorem -? CMT



![image-20220212182946376](https://chqwer2.github.io/img/Typora/image-20220212182946376.png)

**by Slutsky,** that if I have

a convergence of distribution, multiply

by a convergence in probability, or in convergence

of distribution to a deterministic number,

I can actually multiply the limits.

![image-20220213190437279](https://chqwer2.github.io/img/Typora/image-20220213190437279.png)

And somehow, we have the sense that we've done something

slightly less precise than I solve. Right?

I solve did not require a second asymptotic approximation

that comes from Slutsky.

Now, of course, if n is not infinite,

if n is for any finite n, you're sort of

accumulating the amount of approximations

that you're making.

So you're relying twice on asymptotics.

And if you don't want to do this,

you might want to stick to I solve.

![image-20220216155815949](https://chqwer2.github.io/img/Typora/image-20220216155815949.png)



### Comparisons of the Methods

 So let's apply those three methods--

the conservative method, the one that consists in solving

a quadratic equation, and the plug-in method--

to our kiss example.

So in the kiss example,

![image-20220212183825230](https://chqwer2.github.io/img/Typora/image-20220212183825230.png)

p hat, which we denoted by Rn bar,

Those three are essentially equivalent.



Why?

Well, simply because n is large, so they're

basically all in the same range.

And also because the value of Rn bar

is actually fairly close to 1/2.

### Two sided versus one sided confidence interval of Gaussians

![image-20220213112035455](https://chqwer2.github.io/img/Typora/image-20220213112035455.png)





For this, observe that mu hat here

is a sum of Gaussian random variables,

and that those Xi's are iid and Gaussian, hence

multivariate Gaussian.





![image-20220213113736225](https://chqwer2.github.io/img/Typora/image-20220213113736225.png)

This way of standardizing it-- this way of taking an estimator

and then manipulating it depending

on mu and maybe the sample size to produce a fixed

distribution.

So this function of your data here

is often called a pivot because we are taking our data,

So this is often going to be how you're starting out

to produce a confidence interval-- by finding

a pivot for your data.

##### Two-sided confidence interval

![image-20220213114547617](https://chqwer2.github.io/img/Typora/image-20220213114547617.png)

##### One-sided confidence interval

None..







 A model is **identifiable** if it is theoretically possible to learn the true values of this model's underlying parameters after obtaining  an infinite number of observations from it.

![image-20220213122526620](https://chqwer2.github.io/img/Typora/image-20220213122526620.png)

 confidence interval of asymptotic level 95%? what does it means? 

![image-20220213181323122](https://chqwer2.github.io/img/Typora/image-20220213181323122.png)
