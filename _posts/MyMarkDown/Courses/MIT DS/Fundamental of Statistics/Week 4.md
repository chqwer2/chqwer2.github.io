

# Hypothesis Testing

null hypothesis : $H_0$

![image-20220216161639002](https://chqwer2.github.io/img/Typora/image-20220216161639002.png)

The fact that we know a smaller possible alternative

might actually make us more powerful,

meaning we can actually squeeze more information out

of the same data if we put more knowledge into the statement

of a statistical hypothesis.



So another piece of terminology is

that we actually want to decide whether we reject H0.

And one of the decision of the test is either rejecting H0 or fail to reject H0.

We don't accept anything in this class.

# Lec 6.  Between Distributions

Goals
In the kiss example, the estimator was intuitively the right thing to do: $\hat{p}=\bar{X}_{n}$.
In view of $L L N$, since $p=\mathbb{E}[X]$, we have $\bar{X}_{n}$
so $\hat{p} \approx p$ for $n$ large enough.

If the parameter is $\theta \neq \mathbb{E}[X]$ ? How do we perform?

1. **Maximum likelihood estimation**: a generic approach with very good properties
2. **Method of moments:** a (fairly) generic and easy approach
3. **M-estimators**: a flexible approach, close to machine learning





Finally, we'll essentially generalize maximum likelihood estimation to what's called M-estimators.

And it's a more flexible approach.



### Total Variation Distance (TV)

Let's just say I give you two distributions. 


Let $\left(E,\left(\mathbb{P}_{\theta}\right)_{\theta \in \Theta}\right)$ be a statistical model associated with a sample of i.i.d. r.v. $X_{1}, \ldots, X_{n}$. 

Assume that there exists $\theta^{*} \in \Theta$ such that $X_{1} \sim \mathbb{P}_{\theta^{*}}: \theta^{*}$ is the true parameter.
Statistician's goal: given $X_{1}, \ldots, X_{n}$, find an estimator $\hat{\theta}=\hat{\theta}\left(X_{1}, \ldots, X_{n}\right)$ such that $\mathbb{P}_{\hat{\theta}}$ is close to $\mathbb{P}_{\theta^{*}}$ for the true parameter $\theta^{*}$.
This means: $\left|\mathbb{P}_{\hat{\theta}}(A)-\mathbb{P}_{\mathscr{\theta^*}}(A)\right|$ is small for all $A \subset E$.
**Definition**

The total variation distance between two probability measures $\mathbb{P}_{\theta}$ and $\mathbb{P}_{\theta^{\prime}}$ is defined by
$$
\operatorname{TV}\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right)=\max _{A \subset E}\left|\mathbb{P}_{\theta}(A)-\mathbb{P}_{\theta^{\prime}}(A)\right| .
$$
It's just different whether you have a PDF or whether you have a PMF.

**TV between discrete measures**
Assume that $E$ is discrete (i.e., finite or countable). T

So let's say, Bernoulli, binomial, Poisson, pick your favorite discrete distribution.
Therefore $X$ has a **PMF (probability mass function)**: $\mathbb{P}_{\theta}(X=x)=p_{\theta}(x)$ for all $x \in E$,
$$
p_{\theta}(x) \geq 0, \quad \sum_{x \in E} p_{\theta}(x)=1
$$
The total variation distance between $\mathbb{P}_{\theta}$ and $\mathbb{P}_{\theta^{\prime}}$ is a simple function of the PMF's $p_{\theta}$ and $p_{\theta^{\prime}}$ :
$$
\operatorname{TV}\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right)=\frac{1}{2} \sum_{x \in E}\left|p_{\theta}(x)-p_{\theta^{\prime}}(x)\right|
$$
**probability mass function** (**pmf**)
$$
f_{X}(x)={\begin{cases}\Pr(X=x),&x\in S,\\0,& x\in \mathbb {R} \backslash S.\end{cases}}
$$
**Why is there a one-half?**

If we starting from the definition, we'll see where the 1/2 actually shows up from this computation.
$$
T V\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right)=\underset{x \in E}{\max} \mid \mathbb{P}_{\theta}(A)-\mathbb{P}_{\theta'}(A)|
$$
It can be break into two parts, assume $A=\left\{x \in E: P_{0}(x) \geqslant P_{0}^{\prime}(x)\right\}$,
$$
\sum_{x:P_{\theta}(x) \geqslant P_{\theta}^{\prime}}\left|P_{\theta}(x)-P_{\theta^{\prime}}(x)\right|=\mathbb{P}_{\theta}\left(A\right)-\mathbb{P}_{\theta^{\prime}}\left(A\right) \\
\sum_{x:P_{\theta}(x) \leqslant P_{\theta}^{\prime}}\left|P_{\theta}(x)-P_{\theta^{\prime}}(x)\right|=\mathbb{P}_{\theta^{\prime}}\left(A^{c}\right)-\mathbb{P}_{\theta}\left(A^{c}\right)
$$

So we have,
$$
\left|\mathbb{P}_{\theta}(A)-\mathbb{P}_{\theta^{\prime}}(A)\right|=\frac{1}{2} \sum_{x \in E}\left|\mathbb{P}_{\theta}(x)-\mathbb{P}_{\theta'}(x)\right|
$$
The really interesting point Prof. Rigollet made in his lecture is that these two different approaches, taking a maximum over events **vs.** summing over elements and dividing by two, actually produce the same result.

**TV between continuous measures**

Assume that $X$ has a density $\mathbb{P}_{\theta}(X \in A)=\int_{A} f_{\theta}(x) d x$ for all $A \subset E$.
$$
f_{\theta}(x) \geq 0, \quad \int_{E} f_{\theta}(x) d x=1
$$
The total variation distance between $\mathbb{P}_{\theta}$ and $\mathbb{P}_{\theta^{\prime}}$ is a simple function of the densities $f_{\theta}$ and $f_{\theta^{\prime}}$ :
$$
\operatorname{TV}\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right)=\frac{1}{2} \int\left|f_{\theta}(x)-f_{\theta^{\prime}}(x)\right| d x .
$$


But in practice, if I'm going to want to minimize the TV, **I don't know what theta star is.**

#### Properties of Total variation

- **Symmetric:** $\operatorname{TV}\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right)=\operatorname{TV}\left(\mathbb{P}_{\theta^{\prime}}, \mathbb{P}_{\theta}\right) \quad$ 
- **Positive:** $1\geq\operatorname{TV}\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right) \geq 0$

- **Definite:** If $\operatorname{TV}\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right)=0$ then $\mathbb{P}_{\theta}=\mathbb{P}_{\theta}^{\prime}$
- Triangle Inequality: 
$\rightarrow \operatorname{TV}\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right) \leq T V\left(\mathbb{P}_{\theta'}, \mathbb{P}_{\theta^{\prime \prime}}\right)+T\left(\mathbb{P}_{\theta^{\prime \prime}}, \mathbb{P}_{\theta^{\prime}}\right)$ 

---

Total Variation Distance of two Bernoulli distributions
$$
TV(P,Q)=1/2(|(1−p)−0|+|p−(1−p)|+|0−p|)
$$
![image-20220226215609745](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220226215609745.png)

The probability they gain same result….

![image-20220226220735300](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220226220735300.png)

![image-20220226220752522](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220226220752522.png)

**Worked Examples of TV**

We have $f(x)=e^{-x} \mathbb 1(x \geq 0)$, $\ g(x)=\mathbb 1(0 \leq  x \leq 1)$


$$
\begin{aligned}
& \frac{1}{2} \int\left|e^{-x} \mu(x>0)-1 y(\phi \leq x \leq 1)\right| d x \\
=& \frac{1}{2} \int_{0}^{1} \cdot \underbrace{e^{-x}-1 \mid}_{1-e^{-x}} d x+\frac{1}{2} \int_{1}^{\infty} e^{-x} d x \\
=& \frac{1}{2}+\frac{1}{2} \int_{0}^{1} e^{-x} d x+\frac{1}{2} \int_{1}^{\infty} e^{-x} d x \\
=& \frac{1}{2}+\left.\frac{1}{2} \cdot e^{-x}\right|_{0} ^{1}-\frac{1}{2} \underbrace{\left.e^{-x}\right|_{1} ^{\infty}}_{-\frac{1}{e}}^{\frac{1}{e}-1}
\end{aligned}
$$
Properties of Total variation
$\operatorname{TV}\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right)=\operatorname{TV}\left(\mathbb{P}_{\theta^{\prime}}, \mathbb{P}_{\theta}\right) \quad$ (symmetric)
$\operatorname{TV}\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right) \geq 0, \quad$ TVC $\left.\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right) \leqslant 1 \quad$ (positive)

- If $\operatorname{TV}\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right)=0$ then $\mathbb{P}_{\theta}=\mathbb{P}_{\theta}^{\prime} \quad$ (definite)
$\rightarrow \operatorname{TV}\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime}}\right) \leq T V\left(\mathbb{P}_{\theta}, \mathbb{P}_{\theta^{\prime \prime}}\right)+T\left(\mathbb{P}_{\theta^{\prime \prime}}, \mathbb{P}_{\theta^{\prime}}\right)$ (triangle inequality)
These imply that the total variation is a
between probability distributions.

![image-20220220161233152](https://chqwer2.github.io/img/Typora/image-20220220161233152.png)

Now, to get rid of those indicators, all I'm going to do

is I'm just going to split my integral according

to where those indicators are.

![image-20220220161246685](https://chqwer2.github.io/img/Typora/image-20220220161246685.png)

![image-20220226221142582](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220226221142582.png)

![image-20220226221236603](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220226221236603.png)

those are literally four different terms.

random variables-- since a's not taking

value equal to 0 or to 1, **those two random variables never take the same values**, right?

There's no values that they can take.

We say that those two variables have disjoint support.

So the tv is the worst possible thing that can ever happen to you.

![image-20220226222422714](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220226222422714.png)

![image-20220226222556945](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220226222556945.png)

And so we know that this guy, as n goes to infinity,

becomes closer and closer to this one.

I just told you that TV was a measure of distance.

So this distance should become smaller and smaller.



this is the only example that we have

where we have a continuous distribution

versus a discrete distribution, right?



So when we don't have a formula for that, what do we do?

We turn to the definition, right?



A continuous random variable's probability

to take values in a finite set is 0.

in this case, it takes the form of what

we call the trivial metric.

There's a trivial notion of distance between anything

you can think of.



And that's the issue with the total variation.

It's a distance, that's fine.

And when things go well, it expresses what you want.

But when you have things that start

to have disjoint support, when you start measuring

the total variation between something which

is discrete and continuous, it captures nothing.

![image-20220227142927436](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227142927436.png)

### An Estimation Strategy and Definition of Kullback-Leibler (KL) Divergence

When $\theta$ is equal to $\theta^*$, the total variation is 0, but we don’t know what $P_\theta^*$ is, let's say I can estimate it.





![image-20220222220936201](https://chqwer2.github.io/img/Typora/image-20220222220936201.png)

let's see methods for estimation.

But then I'm saying, oh, to build a method for estimation

you need to estimate something.

So for that, you need a method for estimation.

And so at some points I'd be like, how do I do this?



Turns out that what you do is you

try to find a place where this naive method, that

consistent replacing the expectation

by the average, the thing that we did for the kiss example, The law of large number is a good guiding principle.



So if you can express this function that

is minimized at theta star as the expectation of something,

and you can replace the expectation by an average,

then you're golden.



If you have a function that is minimized

at the parameter you're looking for,

try to estimate that function, and minimize the estimator

instead.



The problem here is that it's very unclear

how to build an estimator for the total variation.



So if you can express this function that

is minimized at theta star as the expectation of something,

and you can replace the expectation by an average,

then you're golden.

Because now you have an estimator.

The law of large number tells you

that those fluctuations of the blue curve

around the black curve become smaller

as the sample size increases.



So we need a replacement.

We need something that says that replaces

the TV by another notion of distance between probability

measures, but that's the expectation of something,

![image-20220222215636643](https://chqwer2.github.io/img/Typora/image-20220222215636643.png)

which I will call the KL divergence from now on--

between two probability distributions

is also defined differently, whether you're

talking about discrete distributions,

or continuous distributions.

![image-20220222215503591](https://chqwer2.github.io/img/Typora/image-20220222215503591.png)

![image-20220227143151882](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227143151882.png)



# Properties of the Kullback-Leibler (KL) Divergence

![image-20220222220239386](https://chqwer2.github.io/img/Typora/image-20220222220239386-16455673742601.png)

It is not symmetric,  non-negative, and it is important to be definite.

There's something called the Shannon Jensen divergence, which is popular in deep neural nets these days.

It's making it symmetric but not much more.



Even if it's not symmetric, it's still the unique minimizer.

# Estimating the Kullback-Leibler (KL) Divergence

So now I could do the same estimation strategy

that I had here, except that I would have here KL,

and I would need to find an estimator for the KL.

![image-20220222220436221](https://chqwer2.github.io/img/Typora/image-20220222220436221.png)

Find an estimator to estimate TV(.)

And that's precisely what maximum likelihood estimation is doing.

1. 

So the first thing that I'm going to use

is the fact that I have a log here, and the log of A over B

is the log of A minus the log of B

Why is this useful?

Well, because the expectation has this linearity property.

So when I have the expectation of a difference,

I can write it as the difference of the expectations.

So I'm just going to write it as the expectation of log

of p theta star minus expectation

with respect to p theta star of log p theta of x.

For discrete 

![image-20220222221927186](https://chqwer2.github.io/img/Typora/image-20220222221927186.png)

That's just a trick to make my expectation appear.

Final ,

I have my observations x1 to xn.

So I'm going to replace my expectation with an average,

and that's my one and only trick,

![image-20220222222328073](https://chqwer2.github.io/img/Typora/image-20220222222328073.png)

![image-20220227162038797](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227162038797.png)

![image-20220227162029770](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227162029770.png)



# Maximum likelihood principle

So now I am just trying to minimize the KL.

But maximizing log of something, since log is an increasing

function, is the same as maximizing the something.

There's no difference.

I could put an exponential in there, I can put--

if those are non-negative numbers I can put x squared.

but they're still equivalent problems.

![image-20220222222723342](https://chqwer2.github.io/img/Typora/image-20220222222723342.png)

The product of the pmfs evaluated at the xis,

this is exactly what we call the likelihood.

What is likelihood?





# Likelihood of a Discrete Distribution

And so it's actually a function, which

takes my n sample, and a candidate parameter,

and tells me how likely it is that this data was generated by **P sub theta**.

That is what likelihood means.

![image-20220222223357361](https://chqwer2.github.io/img/Typora/image-20220222223357361.png)

![image-20220222224226531](https://chqwer2.github.io/img/Typora/image-20220222224226531.png)

### Likelihood of a Poisson Statistical Model

![image-20220222224411289](https://chqwer2.github.io/img/Typora/image-20220222224411289.png)

# Review and Likelihood of a Gaussian Distribution

![image-20220224160231749](https://chqwer2.github.io/img/Typora/image-20220224160231749.png)

For continuous case, we replace pmf to pdf.

**Gaussian: **

![image-20220224160744180](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\_posts\image-20220224160744180.png)

![image-20220224160917775](https://chqwer2.github.io/img/Typora/image-20220224160917775.png)

### Likelihood of an Exponential Distribution

![image-20220224161818931](https://chqwer2.github.io/img/Typora/image-20220224161818931.png)

And when you have product of indicators,

it's always a good idea to try to think of how to turn it

into just one single indicator. And usually it involves the min or the max.



![image-20220224162041736](https://chqwer2.github.io/img/Typora/image-20220224162041736.png)

### Likelihood of a Uniform Distribution

![image-20220224162348927](https://chqwer2.github.io/img/Typora/image-20220224162348927.png)

So the first indicator-- so as a rule--

is that this does not depend on the unknown parameter,

so we can just remove it.

![image-20220224162501306](https://chqwer2.github.io/img/Typora/image-20220224162501306.png)

![image-20220228085927481](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220228085927481.png)

# Likelihood of a Mixture of Gaussians

![image-20220224162643310](https://chqwer2.github.io/img/Typora/image-20220224162643310.png)

the weight is 1/2 and 1/2

So as we know, there's two descriptions

of a mixture of two Gaussians.

The first one is using the pdf.

So the latent variable z is a Bernoulli random variable

![image-20220224162851152](https://chqwer2.github.io/img/Typora/image-20220224162851152.png)

![image-20220224163043867](https://chqwer2.github.io/img/Typora/image-20220224163043867.png)

But really what I want to emphasize

is the fact that there will not be a very nice formula.

We will still be stuck with the sum of exponential like this.

And this is not something that lends itself

to optimization very easily.

### Definition of Maximum Likelihood Estimator and Log Likelihood

And remember what we did, we said that minimum estimated kl the same as maximizing likelihood.



if I have a function that I'm maximizing

or if I maximize an increasing function of this function,



max log-likelyhood

The reason why we take the log is because--

I don't know if you've noticed, but there's a lot of powers

there, and there's a lot of exponentials there.

And it's going to make our life much easier

by just taking the powers down and removing the exponentials,

and that's it.





of it as a function of X. But really, it's

a function of both X and B.

And what we're doing is that we start by thinking of it

as a function of X. We talk about PDF, we talk about PMF,

we write our log likelihood.

And then once the log likelihood is written,

we're going to want to maximize it in the parameter.

So we switch our point of view, and we

start talking about it as a function of B, of lambda,

of mu sigma squared, lambda, and P. OK?



You write, you think in terms of PDFs and PMF

as function of your data.

And once you've actually written this, you just make the switch,

and you think of it as a function of B or the parameter

or theta, I guess.

![image-20220227233115330](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227233115330.png)

### Interpreting the Likelihood

![image-20220227164103732](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227164103732.png)

![image-20220227164120960](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227164120960.png)

# Interlude: Minimizing and Maximizing Functions

NIPS: an optimization conference



A sufficient condition for it to be a minimum

is we'll talk about its derivative being equal to 0.

![image-20220224212319473](https://chqwer2.github.io/img/Typora/image-20220224212319473.png)

As a function of theta, I want the second derivative

to be negative.

Recall that the critical point is a **unique maximizer** of $f$. 

And so we're going to focus on convex functions

when we're talking about minimization or concave

function when we're talking about maximization.



So we'll take the analytic definition,

there's also a so-called synthetic definition,

which is the one that we used when we talked

about Jensen's inequality.

All right, so the synthetic one says

that the curve is below its chord,

and the function is below its chord.

For that, I didn't need to use the word derivative, anything.



**Concave** looks like this

![image-20220224212545391](https://chqwer2.github.io/img/Typora/image-20220224212545391.png)

So convex is just that the second derivative

is non-negative, and strictly convex

is the second derivative is strictly positive.

### Worked Examples: Concavity in 1 dimensions

![image-20220224213331275](https://chqwer2.github.io/img/Typora/image-20220224213331275.png)

### Strictly Concave Functions and Unique Maximizer

is that their minimum and maximum is achieved exactly

at one place.

And this place is where the derivative

is equal to 0, where the function just changes

its monotonicity, right?

It's going down, and then up.



![image-20220224214117210](https://chqwer2.github.io/img/Typora/image-20220224214117210.png)

And that's useful when you have theta that

has d different coordinates.

You have a system of d equations.



optimization algo

**Interior point methods.**

**Ellipsoid method is another one very much, so thank you.**

There's cutting plane methods.

There's a lot of variance around gradient descent.

The Simplex method is just for a very specific class,



But somethings we don’t need complex algo for such as -\theta^2$

You just take the derivative.

That's minus 2 theta.

Set it equal to 0.

That implies theta is equal to 0.





### Calculate Distances between probability distribution 

Recitation

**Recitation problem statement**

1. For $p, q \in(0,1)$ and $n \geq 1$, compute the Kullback-Leibler divergence between $\mathrm{B}(n, p)$ and $\mathrm{B}(n, q)$
2. Compute the Kullback-Leibler divergence between two Gaussian distributions that have the same variance. 
3. Show that the Poisson distribution with parameter  converges in total variation distance to the Dirac distribution at zero (i.e., the distribution of the random variable that is always equal to  zero). 

Review: Definitions of TV and KL

![image-20220227145457488](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227145457488.png)

### Comparing properties of TV and KL

![image-20220227151623614](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227151623614.png)

Amenable to E

### Convergence of Poisson distributions to the delta function

Poisson

lambda of k of lambda to the k over k factorial times

e to the minus lambda.

So e to the minus lambda is the normalizing constant.

And this is what it is proportional to for every k.

And k is 0, 1, and so on.

Q = Delta(0)

![image-20220227152522833](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227152522833.png)

![image-20220227152606166](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227152606166.png)

What about P = Geom(1-$\frac{1}{n}$)?

### KL between binomial distributions

n choose k, q to the k = 
$$
  \left({\begin{array}{cc}
   n  \\
   k \\
  \end{array} } \right)
, q^k
$$
And we know that as an aside, if x follows a binomial distribution, then the expectation of x is n times p.

![image-20220227153833816](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227153833816.png)

### KL between Gaussian distributions

![image-20220227154139597](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227154139597.png)

with same variances $\sigma$?

![image-20220227160256389](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227160256389.png)

reference link: https://courses.edx.org/courses/course-v1:MITx+18.6501x+1T2022/discussion/forum/186501x_1T2022_discussion_u03s01_methodestimation-tab10_discussion/threads/6210be5f9cfb2404a08453fa

![image-20220227160708801](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227160708801.png)

![image-20220227160719299](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227160719299.png)

![image-20220227170452984](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227170452984.png)

resp.用作德语*beziehungsweise*误翻。可以简单理解为*or,* *or as the case may be*。

![image-20220227170950610](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227170950610.png)

![image-20220227171011372](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227171011372.png)

![image-20220227172001889](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227172001889.png)

![image-20220227215513798](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227215513798.png)

Wrong:

![image-20220227230231240](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227230231240.png)

![image-20220227231350952](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227231350952.png)

![image-20220227231437227](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220227231437227.png)

take the derivative with respect to $\theta$, set to zero, and solve for $\theta$.

https://www.probabilitycourse.com/chapter8/8_2_3_max_likelihood_estimation.php

### *multivariate statistics* 

![image-20220228095143634](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220228095143634.png)

![image-20220228095749076](C:\MyMarkDown\Courses\edX\MIT DS\Fundamental of Statistics\image-20220228095749076.png)

strictly concave.

