## M-estimation

**Normal MLE Strategy**

Observe $X_{1}, \ldots, X_{n} \sim \mathbb{P}_{\theta^{*}}$, i.i.d, $\theta^{*}$ unknown.

1. Ideal loss function: $\theta \mapsto \mathrm{KL}\left(\mathbb{P}_{\theta^{*}}, \mathbb{P}_{\theta}\right)$ minimized at $\theta=\theta^{*}$
2. Observe that $\mathrm{KL}\left(\mathbb{P}, \mathbb{P}_{\theta}\right)=-\mathbb{E} \log \left[p_{\theta}(X)\right]$ + constant
3. Estimate by $-\frac{1}{n} \sum_{i=1}^{n} \log \left[p_{\theta}\left(X_{i}\right)\right]$ (-log-likelihood)
4. $\hat{\theta}:=\operatorname{argmin}\left\{-\frac{1}{n} \sum_{i=1}^{n} \log \left[p_{\theta}\left(X_{i}\right)\right]\right\}$

**M-estimation**

Simplify, replacing expectations with averages and replace KL by other loss.

1. Ideal loss function: $\theta \mapsto \mathrm{loss}\left(\mathbb{P}_{\theta^{*}}, \mathbb{P}_{\theta}\right)$ minimized at $\theta=\theta^{*}$
2. Observe that $\mathrm{loss}\left(\mathbb{P}, \mathbb{P}_{\theta}\right)=-\mathbb{E} [\rho(X,\theta)]]$ + constant
3. Estimate by $-\frac{1}{n} \sum_{i=1}^{n} \log \left[\rho(X,\theta)\right]$ (-log-likelihood)
4. $\hat{\theta}:=\operatorname{argmin}\left\{-\frac{1}{n} \sum_{i=1}^{n} \log \left[\rho(X,\theta)\right]\right\}$

**Adv. of M-estimation**:

Let $X_{1}, \ldots, X_{n}$ be i.i.d. with some unknown distribution $\mathbf{P}$ and an associated parameter $\mu^{*}$ on a sample space $E$. We make no modeling assumption that $\mathbf{P}$ is from any particular family of distributions.

An M-estimator $\widehat{\mu}$ of the parameter $\mu^{*}$ is the argmin of an estimator of a function $\mathcal{Q}(\mu)$ of the parameter which satisfies the following:

- $\mathcal{Q}(\mu)=\mathbb{E}[\rho(X, \mu)]$ for some function $\rho: E \times \mathcal{M} \rightarrow \mathbb{R}$, where $\mathcal{M}$ is the set of all possible values of the unknown true parameter $\mu *$;
- $\mathcal{Q}(\mu)$ attains a unique minimum at $\mu=\mu^{*}$, in $\mathcal{M}$. That is, $\operatorname{argmin}_{\mu \in \mathcal{M}} \mathcal{Q}(\mu)=\mu^{*}$.

In general, the goal is to find the loss function $\rho$ such $\mathcal{Q}(\mu)=\mathbb{E}[\rho(X, \mu)]$ has the properties stated above.

Because $\mathcal{Q}(\mu)$ is an expectation, we can construct a (consistent) estimator of $\mathcal{Q}(\mu)$ by replacing the expectation in its definition by the sample mean. 

- Goal: estimate some parameter $\mu^{*}$ associated with $\mathbb{P}$, **e.g.** its mean, variance, median, other quantiles, the true parameter in some statistical model...

**How do I find the $\rho$?**

- If $E=\mathcal{M}=\mathbb{R}$ 
  - and $\rho(x, \mu)=(x-\mu)^{2}$, 
  - for all $x \in \mathbb{R}, \mu \in \mathbb{R}$ : $\mu^{*}=\mathbb{E}[X]$
- If $E=\mathcal{M}=\mathbb{R}^{d}$ 
  - and $\rho(x, \mu)=\|x-\mu\|_{2}^{2}$, 
  - for all $x \in \mathbb{R}^{d}, \mu \in \mathbb{R}^{d}: \mu^{*}=\mathbb{E}[X] \in \mathbb{R}^{\perp}$
- If $E=\mathcal{M}=\mathbb{R}$ 
  - and $\rho(x, \mu)=|x-\mu|$, 
  - for all $x \in \mathbb{R}, \mu \in \mathbb{R}$ : $\mu^{*}$ is a **medien** of $\mathbb{P}$.

Because for  $E\left[(X-\mu)^{2}\right]$:
$$
\begin{aligned}
\frac{\partial}{\partial \mu} \mathbb{E}\left[(X-\mu)^{2}\right) &=\mathbb{E}(-2 x+2 \mu) \\
&=-2 \mu^{*}+2 \mu=0
\end{aligned}
$$
But **absolute value** is not differentiable at coordinate origin 0? How do we handle it?

It is a nice simmetric function, right? We can use median as the $\rho$.

**What if we tilt it a little bit? **

We can have $C_\alpha$ and a **Quantile Estimator**

![image-20220306120905777](https://chqwer2.github.io/img/Typora/image-20220306120905777.png)

**Quantile Estimator Definition**
$$
\begin{aligned}
\mathcal{Q}(\mu) &=\mathbb{E}[\rho(X, \mu)] \\
\end{aligned}
$$
Define $\hat{\mu}_{n}$ as a minimizer of:
$$
\begin{aligned}
&\mathcal{Q}_{n}(\mu):=\frac{1}{n} \sum_{i=1}^{n} \rho\left(X_{i}, \mu\right) . \\
&\hat{\mu}_{n}=\text {M-estimetor }
\end{aligned}
$$
Examples: Empirical mean, empirical median, empirical quantiles, MLE, etc.
$$
\begin{aligned}
&\rho(X, \mu)=(X-\mu)^{2} \Rightarrow \hat{\mu}_{n}=\bar{X} \\
&\rho(X, \theta)=-\log _{\theta}(X) \Rightarrow \hat{\theta}_{n} \text { is the MLE }
\end{aligned}
$$


**Example: multivariate mean as minimizer**
Let $\mathbf{X}=\left(\begin{array}{c}X^{(1)} \\ X^{(2)}\end{array}\right)$ be a continuous random vector with density $f: \mathbb{R}^{2} \rightarrow \mathbb{R}$. Recall the mean of $\mathbf{X}$ is
$$
\mathbb{E}[\mathbf{X}]=\left(\begin{array}{l}
\mathbb{E}\left[X^{(1)}\right] \\
\mathbb{E}\left[X^{(2)}\right]
\end{array}\right)
$$
Recall the square of the Euclidean norm function on $\mathbb{R}^{2}$ :
$$
\begin{gathered}
\|\cdot\|^{2}: \mathbb{R}^{2} \rightarrow \mathbb{R} \\
\mathbf{y}=\left(\begin{array}{c}
y_{1} \\
y_{2}
\end{array}\right) \mapsto\left(y_{1}\right)^{2}+\left(y_{2}\right)^{2} .
\end{gathered}
$$
We now show that the (multivariate) mean of $\mathbf{X}$ satisfies:
$$
\mathbb{E}[\mathbf{X}]=\operatorname{argmin}_{\vec{\mu} \in \mathbb{R}^{2}} \mathbb{E}\left[\|\mathbf{X}-\vec{\mu}\|^{2}\right]
$$
First, expand $\mathcal{Q}(\vec{\mu})=\mathbb{E}\left[\|\mathbf{X}-\vec{\mu}\|^{2}\right]$ as an integral expression, and write down both partial derivatives $\frac{\partial \mathcal{Q}}{\partial \mu_{1}}(\vec{\mu})$ and $\frac{\partial \mathcal{Q}}{\partial \mu_{2}}(\vec{\mu}):$
$$
\begin{aligned}
\mathbb{E}\left[\|\mathbf{X}-\vec{\mu}\|^{2}\right] &=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty}\left(\left(x_{1}-\mu_{1}\right)^{2}+\left(x_{2}-\mu_{2}\right)^{2}\right) f\left(x_{1}, x_{2}\right) d x_{1} d x_{2} \\
\Longrightarrow \quad \frac{\partial}{\partial \mu_{1}} \mathbb{E}\left[\|\mathbf{X}-\vec{\mu}\|^{2}\right] &=-2 \int_{-\infty}^{\infty} \int_{-\infty}^{\infty}\left(x_{1}-\mu_{1}\right) f\left(x_{1}, x_{2}\right) d x_{1} d x_{2} \\
\frac{\partial}{\partial \mu_{2}} \mathbb{E}\left[\|\mathbf{X}-\vec{\mu}\|^{2}\right] &=-2 \int_{-\infty}^{\infty} \int_{-\infty}^{\infty}\left(x_{2}-\mu_{2}\right) f\left(x_{1}, x_{2}\right) d x_{1} d x_{2} .
\end{aligned}
$$
To find the argmin of $\mathbb{E}\left[\|\mathbf{X}-\vec{\mu}\|^{2}\right]$, we set both partial derivatives to 0 , and obtain:
$$
\operatorname{argmin}_{\vec{\mu} \in \mathbb{R}^{\mathbb{R}}} \mathbb{E}\left[\|\mathbf{X}-\vec{\mu}\|^{2}\right]=\left(\begin{array}{l}
\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x_{1} f\left(x_{1}, x_{2}\right) d x_{1} d x_{2} \\
\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x_{2} f\left(x_{1}, x_{2}\right) d x_{1} d x_{2}
\end{array}\right)=\left(\begin{array}{l}
\mathbb{E}\left[X^{(1)}\right] \\
\mathbb{E}\left[X^{(2)}\right]
\end{array}\right)
$$


### 







###  Preparations for the Asymptotic Normality of M-estimators

$J$ and $K$.

![image-20220306144636267](https://chqwer2.github.io/img/Typora/image-20220306144636267.png)



![image-20220306144746389](https://chqwer2.github.io/img/Typora/image-20220306144746389.png)

![image-20220306144910145](https://chqwer2.github.io/img/Typora/image-20220306144910145.png)

![image-20220308132836777](https://chqwer2.github.io/img/Typora/image-20220308132836777.png)

### Asymptotic Normality of M-estimators



![image-20220306145227499](https://chqwer2.github.io/img/Typora/image-20220306145227499.png)

should be mu star

![image-20220306145252685](https://chqwer2.github.io/img/Typora/image-20220306145252685.png)

So if I want to build a confidence interval,

I'm actually stuck in this problem,

just like I was with the kiss example.

I would have this asymptotic variance that depends

on my unknown parameter.

So what do I do?

So I have a bunch of methods, and one

is to just use plug-in and rely on Slutsky.



### Robust Statistics

Robust Statistics, Cauchy Distribution

a bunch of data, may corrupted…

So **Cauchy distribution**

So the Cauchy distribution is statisticians' favorite example

of a heavy tail distribution.

![image-20220307164607958](https://chqwer2.github.io/img/Typora/image-20220307164607958.png)

Of course it cannot be 1 over x, because I want this function

to actually be integrable.

So 1 over x squared is basically the first exponent

I can have so that when I integrate--

so the integral of fm of x dx is well-defined, nothing blows up.

It's actually equal to 1.





This guy not have bounded support.

All I can say is, well, expectation is not defined.

I don't even have a first moment.

So the median will be a consistent estimator of m.

Just because-- just looking at this function,

it's symmetric about m.



So location and scale are common terminology in statistics.

We talk about a location/scale family,

which is basically a family which

is indexed by m and sigma.





## Moment of Variables

Let $X$ be a random variable with distribution $\mathbb{P}_{\theta}$ (write $\mathbb{E}_{\theta}$ for its expectation).
**Definition**
For $k=1,2, \ldots$, the moment of order $k$ of $X$ is given by
$$
m_{k}=m_{k}(\theta)=\mathbb{E}_{\theta}\left[X^{k}\right]
$$
Example 1: $X \sim \mathcal{N}\left(\mu, \sigma^{2}\right) \quad$    Example 2: $X \sim \operatorname{Ber}(p)$
$$
\begin{array}{llll}
m_{1}(\vartheta)=\mathbb{E}[X] & =\mu & & m_{1}(\rho)=\mathbb{E}[X]=p \\
m_{2}(\theta)=\mathbb{E}_{\theta}\left[X^{2}\right] & =\sigma^{2}+(\mathbb{E}[X])^{2} & & m_{k}(p)={\mathbb{E}}_{p}\left[X^{k}\right]=\mathbb E_{p}[X]=p \\
& =\sigma^{2}+\mu^{2} & & X \in\{0,1\} \Rightarrow X^{k}=X
\end{array}
$$

### **Moment Generating Function (MGF)**

For many distributions (e.g. some $t$ of Cauchy no included),  all the moments of $X \sim \mathbb{P}$ are contained in a single function called Moment Generating Function, or simply MGF:
$$
M_{X}(t)=\mathbb{E}\left[e^{t x}\right] \quad, t \in \mathbb{R}
$$
The moments are given by successive  derivatives of $M_{X}(\cdot)$ at

For $t=0$ :
$$
\begin{array}{}

M_{X}^{(1)}(t)=\mathbb{E}\left[\frac{d}{d t} e^{t X}\right] \quad=\mathbb{E}\left[X e^{t X}\right]=\mathbb{E}[X]  \\

M_{X}^{(2)}(t)=\mathbb{E}\left[\frac{d^{2}}{d t^{2}} e^{t X}\right]=\mathbb{E}\left[X^{2} e^{t X}\right]=\mathbb{E}\left[X^{2}\right] \\
\vdots \\
M_{X}^{(k)}(t)=\mathbb{E}\left[\frac{d^{k}}{d t^{k}} e^{t X}\right]=\mathbb{E}\left[X^{k} e^{t x}\right]=\mathbb{E}\left[X^{k}\right]

\end{array}
$$
**MGF of a Standard Gaussian**
Consider the Standard Gaussian r.v. $Z \sim \mathcal{N}(0,1)$. We compute its MGF:
$$
M_{Z}(t)=\mathbb{E}\left[e^{t Z}\right]=\frac{1}{\sqrt{2 \pi}} \int e^{t z} e^{-\frac{z^{2}}{2}} d z
$$
To compute it, we use a standard **trick** when manipulating:
$$
\frac{(Z-t)^2}{2}=\frac{Z^2}{2}-Zt+\frac{t^2}{2}
$$
So:
$$
\frac{1}{\sqrt{2 \pi}} \int e^{tz} e^{-\frac{z^{2}}{2}} d z = \frac{1}{\sqrt{2 \pi}} \int e^{-(t-z)^2} d z+\frac{t^2}{2}
$$
Therefore
$$
M_{Z}(t)=e^{\frac{t^{2}}{2}}
$$
We have seen that for any r.v. $X$, 
$$
m_{k}=M_{X}^{(k)}(0), \quad k=1,2, \ldots
$$
If $X=Z \sim \mathcal{N}(0,1)$, compute
$$
\mathbb E \left[X^{k}\right]=M_{Z}^{(k)}(0)=\left.\frac{d^{k}}{d t^{k}} e^{\frac{t^{2}}{2}}\right|_{t=0}.
$$
It yields
$$
\begin{aligned}
&M_{Z}^{(1)}(t)=t e^{t^{2} / 2} \Rightarrow m_{1}=\mathbb{E}[X]=M_x(0)=0 \\
&M_{Z}^{(2)}(t)=e^{t^{2} / 2}+t^{2} \cdot e^{t t^{2} / 2} \Rightarrow m_{2}=M_{x}^{(2)}(0)=1 \\
&M_{Z}^{(3)}(0)=0 \\
&M_{Z}^{(4)}(0)=3
\end{aligned}
$$
**Sample Moments**

The $k^{th}$ sample moment is:
$$
\hat m_k = \mathbb E[X^k]=\sum_{i=1}^nX_i^k
$$
By LLN, we have:
$$
\hat{m}_{k} \underset{n \rightarrow \infty}{\stackrel{\mathbb{P} / a.s}{\longrightarrow}} m_{k}
$$


![image-20220307171254426](https://chqwer2.github.io/img/Typora/image-20220307171254426.png)



### Generalized Method of Moments Estimator: Statistical Analysis

I just try to find relationships between my parameter

and my moments.

![image-20220307171652695](https://chqwer2.github.io/img/Typora/image-20220307171652695.png)

### Asymptotic Normality of the Method of Moments Estimator

When I apply my delta method, this

will have an impact on my asymptotic covariance matrix.

And once it has an impact on my asymptotic covariance matrix,

I want it to be as small as possible.

![image-20220311151325346](https://chqwer2.github.io/img/Typora/image-20220311151325346.png)

![image-20220311152001442](https://chqwer2.github.io/img/Typora/image-20220311152001442.png)

![image-20220311152011312](https://chqwer2.github.io/img/Typora/image-20220311152011312.png)



Wavelets are such functions.

They're functions that are nice, and contain a lot

of information about the image.

And if you actually compute-- if you think of image x as being

some random thing--

an image as being a random x--

and you want to compute the expectation

of this image against some wavelet function,

you could actually replace this cosine by a wavelet function.

That's what JPEG 2000 is doing for you.

The actual JPEG is using cosine and a few extra tricks.

![image-20220307172132951](https://chqwer2.github.io/img/Typora/image-20220307172132951.png)

![image-20220307172409582](https://chqwer2.github.io/img/Typora/image-20220307172409582.png)

Cov..

![image-20220307172436186](https://chqwer2.github.io/img/Typora/image-20220307172436186.png)

So as you can see here, we may not

have the nice cancellation that arises

from the maximum likelihood estimator, right?

It's the same thing that sort of happened

for the maximum likelihood estimator, right?

We had the Fisher information here,

and 1 over the-- the inverse Fisher information here,

the inverse Fisher information there.

And they basically sort of all cancel,

and we ended up with only one inverse Fisher information

somewhere.

But here this is not very likely to happen.



### Conclusions

![image-20220307172741591](https://chqwer2.github.io/img/Typora/image-20220307172741591.png)







### Recitation M-Estimation



# Method of Moments

![image-20220304232655126](https://chqwer2.github.io/img/Typora/image-20220304232655126.png)



Moment Generating Fun

![image-20220304233247913](https://chqwer2.github.io/img/Typora/image-20220304233247913.png)



![image-20220304235157190](https://chqwer2.github.io/img/Typora/image-20220304235157190.png)

Finally plug-in.

![image-20220305001319289](https://chqwer2.github.io/img/Typora/image-20220305001319289.png)

M-estimation is the process of estimating

a parameter for a distribution using

some form of minimization.



So in this framework we want to minimize some loss function

to spit out an estimator of a parameter.



So with this sort of setup, what we want to do

is we want to look at M-estimators

for a couple of different distributions

and just sort of show how you can

get maybe desirable properties by choosing different loss

functions for rho.

avar for **asymtotic variance**

### sample median to the asymptotic variance

![image-20220306091826948](https://chqwer2.github.io/img/Typora/image-20220306091826948.png)



And we know sums of Bernoullis actually

do converge in distribution to a normal.

The only issue here is that the parameter in this Bernoulli

distribution will depend on the parameter n.



![image-20220306092556112](https://chqwer2.github.io/img/Typora/image-20220306092556112.png)



And you'll notice that this is actually just the definition

of the derivative of f, right?

![image-20220306093445838](https://chqwer2.github.io/img/Typora/image-20220306093445838.png)

In the next part, let's compare

that asymptotic variance that we just

found for the sample median to the asymptotic variance we would get for the sample mean.

### sample mean to the asymptotic variance

$m_n$ is the median

![image-20220306094734777](https://chqwer2.github.io/img/Typora/image-20220306094734777.png)

And this would give you some evidence

that using the sample median, at least for the Laplace

distribution, would give you better performance,

at least asymptotically, right?



We're going to do this again in the next one

and actually compare the median and mean as well as the Huber

estimator for the Cauchy distribution.

I do that by plugging in f of mu and showing that it equals 1/2.



So we note that f of mu actually does equal 1/2

because arc tangent of 0 is 0.

Right, so the true median of this distribution

is actually 1/2.



median = mean in this situation

![image-20220306095538235](https://chqwer2.github.io/img/Typora/image-20220306095538235.png)

whereas the asymptotic variance of the sample mean,

it just doesn't exist, right?

It doesn't even have a variance for one sample, or a mean.

Those integrals diverge.

So we've seen, at least, that the median's a better

estimator.

### Huber estimator 

![image-20220306095659568](https://chqwer2.github.io/img/Typora/image-20220306095659568.png)

differentiable



![image-20220306100353894](https://chqwer2.github.io/img/Typora/image-20220306100353894.png)

secant squared of x.



![image-20220306100847499](https://chqwer2.github.io/img/Typora/image-20220306100847499.png)

you think, OK, let's try to use a little b L'Hopital's rule, which you can actually do. 



So the asymptotic variance of the Huber M-estimator diverges.

And this corresponds to the case where

we're minimizing sums of squares, which is, again,

going back to the mean estimator, which

we showed earlier.



![image-20220306101616570](https://chqwer2.github.io/img/Typora/image-20220306101616570.png)

Sometimes the M-estimators have asymptotic variance

that doesn't exist, as is the case, when we look at the mean

under the kosher distribution.

But when they do exist, they give us

a good way of at least doing a simple calculation to see maybe

which estimate we should use in a given situation.

