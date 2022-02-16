---
layout:     post
title:      "Statistics MIT 18.6501x"
subtitle:   " \"STAT is Fun!\""
date:       2022-02-08 12:00:00
author:     "Calvchen"
header-img: "img/post-bg-infinity.jpg"
catalog: true
tags:
    - Math
    - Statistics
    - Course


---

> “Machine Learning, Deep Learning, Data Science, etc. are all in the same nexus – which is the bacically Probability plus Statistics. ”



# Statistics, MIT 18.6501x

A useful [book]( https://onlinestatbook.com/2/sampling_distributions/samp_dist_mean.html).

## Where will be covered:

- [Theorems and Tools](#Theorems and Tools)

  - LLN & CLT, CMT
  - Hoeffding's Inequality, Chebyshev Inequality
  - Slutsky's theorem
  - Asymptotic normality

- [Distribution Functions](#Distribution)

- Estimator

- Probability Redux

  



## Theorems and Tools

**i.i.d.**  stands for **independent and identically distributed** . 

### Law of Large Numbers (LLN)

According to the law, the average of the results obtained from performing the same experiment a large number of times should be close to the **expectation value**, and tend to be closer when n is even greater.

Let $X, X_{1}, X_{2}, \ldots, X_{n}$ be i.i.d. 
Laws (weak and strong) of large numbers (LLN):
$$
\bar{X}_{n}:=\frac{1}{n} \sum_{i=1}^{n} X_{i} \underset{n \rightarrow \infty}{\stackrel{\text { P }, \text { a.s. }}{\longrightarrow}} \mu .
$$


### Central Limit Theorem (CLT)

CLT establishes that when independent random variables summed up, their properly normalized sum tends toward a **normal distribution** even if the original variables themselves are not normally distributed. 
$$
\sqrt{n} \frac{\bar{X}_{n}-\mu}{\sigma} \frac{(d)}{n \rightarrow \infty} \mathcal{N}(0,1)
$$


where  $\stackrel{(d)}{\rightarrow}$ denotes convergence in distribution.

Standard Gaussian means that this quantity will be a number between (-3, 3) with overwhelming probability, we have $|\overline X_n - \mu|=\frac{3\sigma}{\sqrt{n}}$.

$\bar X_n$ is close to $\mu$ at some deviations that are of order 1 over square root of sample size  ($\sim \frac{1}{n}$).

**Rule of thumb to apply CLT:** normally, we require $n\geq30$.

#### Asymptotic normality

Assume the sequence $\left\{X_{n}\right\}$ is an i.i.d sequence with finite mean and variance.
Therefore, it satisfies the conditions of Central Limit Theorem.
Hence, the sample mean $\bar X_{n}$ in the above equlity is asymptotically normal.
In other words, the sample mean $X_{n}$ converges in distribution to a normal random variable with mean $\mu$ and variance $\frac{\sigma^{2}}{n}$.

### Continuous Mapping Theorem (CMT)

CMT states that continuous functions preserve limits even if their arguments are sequences of random variables. A continuous function is such a function that maps convergent sequences into another convergent sequences:
$$
\text{if\ } x_n \to x,\\ \text{then } g(x_n) \to g(x).
$$


It applies to $d,\ p$ and $a.s.$ convergence respectively.

### Hoeffding's Inequality 

What if $n$ is **not large enough** to apply CLT?

For bounded random variable, this is still **Hoeffding’s Inequality** we can say for any n.
Let $n$ be a positive integer and $X_i \in[a, b]\ $($a<b$ are given numbers)
Then this holds even for small sample sizes $n$:
$$
\mathbb{P}\left[\left|\bar{X}_{n}-\mu\right| \geq \varepsilon\right] \leq 2 e^{\large-\frac{2 n \varepsilon^{2}}{(b-a)^{2}}} . \quad \forall \varepsilon>0
$$


Here I need that my random variables are actfually **almost surely bounded**, which rules out like Gaussians and Exponential Random Variables.

**How to choose $\varepsilon$ ?**

So let's parse this for a second… 

if when $\varepsilon = \large\frac{c}{\sqrt{n}}$:
$$
X_i \overset{iid}{\sim}Ber(p)\\
\mathbb{P}(| \bar{X} - \mu| \geq \frac{c}{\sqrt{n}}) \leq 2e^{-2c^2/1}
$$


The square root of $n$ qualitative behavior happens at any n.

So the conclusion is the average is a good replacement

##### Is this tight? That's the annoying thing about inequalities.

The above inequality could actually be e to the minus exponential of n ($e^{-n}$), which could be much, much smaller than that, so it is loose.

### Chebyshev Inequality & Markov Inequality

These two inequalities guarentees that upper bounds on $\mathbf{P}(X \geq t)$ based on the mean and variance of $X$.
**Markov inequality**
For a random variable $X \geq 0$ with mean $\mu>0$, and any number $t>0$ :
$$
\mathbf{P}(X \geq t) \leq \frac{\mu}{t}
$$
Note that the Markov inequality is restricted to **non-negative random variables**.

**Chebyshev inequality**
For a random variable $X$ with (finite) mean $\mu$ and variance $\sigma^{2}$, and for any number $t>0$,
$$
\mathbf{P}(|X-\mu| \geq t) \leq \frac{\sigma^{2}}{t^{2}}
$$
Remark:
When Markov inequality is applied to $(X-\mu)^{2}$, we obtain Chebyshev's inequality. Markov inequality is also used in the proof of Hoeffding's inequality.



## Distribution

### Gaussian Distribution

Notation: $X\sim\mathcal{N}(\mu, \sigma^2) $

Mean and Variance: $\mu,\ \sigma^2$

Probability Density Function: 
$$
\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left( \frac{x-\mu}{\sigma}  \right)^2}
$$
![image-20220205100840395](https://chqwer2.github.io/img/Typora/image-20220205100840395.png)

Cumulative Distribution Function:
$$
\frac{1}{2}\left[1+ \text{erf} \left(  \frac{x-\mu}{\sqrt{2}\sigma }\right)\right]
$$
$\text{erf}(\cdot)$ is the exponential response formula.

![image-20220205100857657](https://chqwer2.github.io/img/Typora/image-20220205100857657.png)

##### Covariance of Gaussians

Recall that the **covariance** of two random variables $X$ and $Y$ denoted by $\text{Cov} (X,Y)$ is defined as:
$$
\text{Cov} (X,Y) = \text E[\ (X-\text E[X])\ (Y-\text E[Y])\ ]\\
\text{Cov} (X,Y) = \text E[XY]\cdot\text E[X]\text E[Y])\ ]
$$
 **Var[X+Y] = Var[X] + Var[Y] + 2∙Cov[X,Y]** 


$$
\begin{aligned}
\operatorname{Var}(X Y) &=\operatorname{Var}[\mathrm{E}(X Y \mid X)]+\mathrm{E}[\operatorname{Var}(X Y \mid X)] \\
&=\operatorname{Var}[X \mathrm{E}(Y \mid X)]+E\left[X^{2} \operatorname{Var}(Y \mid X)\right] \\
&=\operatorname{Var}[X \mathrm{E}(Y)]+E\left[X^{2} \operatorname{Var}(Y)\right] \\
&=E(Y)^{2} \operatorname{Var}(X)+\operatorname{Var}(Y) E\left(X^{2}\right)
\end{aligned}
$$
f the covariance,  between two random variables  is 0, then  and  are independent.??

![image-20220205160241835](https://chqwer2.github.io/img/Typora/image-20220205160241835.png)

##### Maximum of uniform random variables

$M_n$



### Poisson Distribution

The advantage of using poisson distribution is that n or p do not need to be known! This can make assumptions much easier.

Notation: $X\sim\text{Poi}(\lambda),\ \lambda \in (0, \infin)$

Mean and Variance: $\lambda,\ \lambda$
$$
E(X^2) = Var(X) + E(x)^2 =  \lambda + \lambda^2
$$
![image-20220206111006698](https://chqwer2.github.io/img/Typora/image-20220206111006698.png)

0! = 1

Probability Mass Function: 
$$
\mathbb{P}(x=k) = \frac{\lambda^k}{k!} e^{-\lambda}, \ k=0,1,2,\cdots \\
$$
![image-20220205102615493](https://chqwer2.github.io/img/Typora/image-20220205102615493.png)

Cumulative distribution function

![image-20220205102652730](https://chqwer2.github.io/img/Typora/image-20220205102652730.png)

### Exponential Distribution

sample space:  $x\in [0, \infin)$

Mean and Variance: $\frac{1}{\lambda},\frac{1}{\lambda^2} $

**PDF:** 
$$
\lambda e^{-\lambda x}
$$
![pdf](https://upload.wikimedia.org/wikipedia/commons/0/02/Exponential_probability_density.svg)

**CDF:**
$$
1-e^{-\lambda x}
$$
![cdf](https://upload.wikimedia.org/wikipedia/commons/b/ba/Exponential_cdf.svg)

![image-20220205172337486](https://chqwer2.github.io/img/Typora/image-20220205172337486.png)

![image-20220205172726369](https://chqwer2.github.io/img/Typora/image-20220205172726369.png)

### Gamma Distribution

https://zh.wikipedia.org/wiki/%E4%BC%BD%E7%8E%9B%E5%88%86%E5%B8%83



### Binomial Distribution

Notation: $B(n,p)$, n is number of trials and p is success probability of each trial

parameters: p, N

Mean: np, 

Var = $\sum^n_{k=1} \sigma^2 = np(1-p)$



$ (1-c/n)^n\rightarrow e^{-c} for \ constant\ c.$

PMF: 
$$
P(k)= \left(\begin{array}{l}

n \\
k
\end{array}\right) p^{k} q^{n-k}=\frac{n!}{k!(n-k)!}p^{k} q^{n-k}
$$

CDF:
$$
I_{q}(n-k, 1+k)
$$


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Binomial_distribution_pmf.svg/300px-Binomial_distribution_pmf.svg.png" alt="Probability mass function for the binomial distribution" style="zoom:80%;" /><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Binomial_distribution_cdf.svg/300px-Binomial_distribution_cdf.svg.png" alt="Cumulative distribution function for the binomial distribution" style="zoom:67%;" />

Probability mass function (Left), Cumulative distribution function(right)

In other words, there are a finite amount of events in a binomial distribution, but an infinite number in a normal distribution.

### Bernoulli Distribution

Variance: p(1-p) 



### Moment Generation Function (MGF)

https://en.wikipedia.org/wiki/Moment-generating_function

expectation of moment generating function

![image-20220209101247516](https://chqwer2.github.io/img/Typora/image-20220209101247516.png)

![image-20220209101551026](https://chqwer2.github.io/img/Typora/image-20220209101551026.png)

https://online.stat.psu.edu/stat414/book/export/html/676

![image-20220209101722845](https://chqwer2.github.io/img/Typora/image-20220209101722845.png)

[mixture distribution moment generating function](https://math.stackexchange.com/questions/2051583/mixture-distribution-moment-generating-function)

Useful…

https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwitz--mtvL1AhXeQEEAHSmoAI8QFnoECDwQAQ&url=https%3A%2F%2Fwww.le.ac.uk%2Fusers%2Fdsgp1%2FCOURSES%2FMATHSTAT%2F6normgf.pdf&usg=AOvVaw3QHSFjpCFrBgTFBxRwGAnK---



## 
