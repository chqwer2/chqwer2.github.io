---
layout:     post
title:      "Statistics Theoretical Derivation, MIT 18.6501x"
subtitle:   " \"Welcome to the derivation of STAT Functions!\""
date:       2022-02-08 12:00:00
author:     "Calvin Chen"
header-img: "img/post-bg-universe.jpg"
catalog: true
tags:
    - Math
    - Statistics
    - Course

---

> “Statistics is not perfect, but it is beautiful and exquisite! ”

# Theoretical Derivation

This post is heavily focused on the mathematical proof and theoretical derivation, which doesn’t be discussed much in the *“Statistics”* Post. 

Will be an appendix of it.

## Gaussian Distribution

Normally, we have Gaussian Distribution: $$X\sim\mathcal{N}(\mu, \sigma^2)$$.



We can now have $(X-\mu)\sim\mathcal{N}(0, \sigma^2)$, which is symmetric odd-function. 



As for the properties of **PDF** and **CDF**, we have:


$$
\int_{-\infty}^{\infty} \frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x=1\\

\int_{-\infty}^{\infty} \frac{x-\mu}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x=0
$$

### Means of Gaussian:

**For** $\mathbb E[x] = \mu$,


$$
\begin{aligned}
\mathbb  E(x) &=\int_{-\infty}^{+\infty} x f(x) d x=\int_{-\infty}^{+\infty} \frac{x}{\sqrt{2 \pi} \delta} e^{-\frac{(x-\mu)^{2}}{2 \delta^{2}}} d x \\

&=\int_{-\infty}^{+\infty} \frac{(x - \mu) + \mu}{\sqrt{2 \pi} \delta} e^{-\frac{(x-\mu)^{2}}{2 \delta^{2}}} d x \\

&=\underbrace{\int_{-\infty}^{+\infty} \frac{x-\mu}{\sqrt{2 \pi} \delta} e^{-\frac{(x-\mu)^{2}}{2 \delta^{2}}} d x}_{0}+ \mu \underbrace{\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi} \delta} e^{-\frac{(x-\mu)^{2}}{2 \delta^{2}}} d x}_{1} \\
&=\mu
\end{aligned}
$$



**For** $\mathbb E[x^2] = \sigma^2 +\mu^2$,


$$
\begin{array}{l}
\mathbb E(x^{2})=\int_{-\infty}^{\infty} x^{2} \cdot \frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x=\int_{-\infty}^{\infty} \frac{(x+\mu)(x-\mu)+\mu^{2}}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x \\
=\int_{-\infty}^{\infty} \frac{(x+\mu)(x-\mu)}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x+\int_{-\infty}^{\infty} \frac{\mu^{2}}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x \\
=\int_{-\infty}^{\infty} \frac{-\sigma(x+\mu)}{\sqrt{2 \pi}} d\left(e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}\right)+\mu^{2} \\
=\underbrace{\left(\frac{-\sigma(x+\mu)}{\sqrt{2 \pi}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}\right)^{\infty}}_0+\sigma^2\int_{-\infty}^{\infty} \frac{1}{\sigma\sqrt{2 \pi}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x+\mu^{2}\\
=\sigma^{2}+\mu^{2} \\
\end{array}
$$



**For** $\mathbb E[x^3] = 3\mu\sigma^2 +\mu^3$,

Patch up $x^3$ into $(x-\mu)^3$,


$$
x^3 = (x-\mu)^3 + \mu^3+3\mu x^2 - 3x\mu^2
$$


So we have, substitutes with $\mathbb E[x^2]$ and $\mathbb E[x]$ formulas:


$$
\begin{array}{l}
\mathbb E\left(x^{3}\right)=\int_{-\infty}^{\infty} x^{3} \cdot \frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x=\int_{-\infty}^{\infty} \frac{(x-\mu)^3 + \mu^3+3\mu x^2 - 3x\mu^2}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x \\
=\underbrace{\int_{-\infty}^{\infty} \frac{(x-\mu)^3}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x}_{0}+
\int_{-\infty}^{\infty} \frac{3(\mu x^2-x\mu^{2})}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x + \mu^3\\
=\small 0 + 3(\mu E(x^{2}) - \mu^2E(x)) +\mu^3\\
= \small 3\mu\sigma^2 +\mu^3
\end{array}
$$

**For** $\mathbb E[x^4] = 3\sigma^4 +6\mu^2\sigma^2 + \mu^4$,

Patch up $x^4$,


$$
x^4 = (x^2 + \mu^2)(x+\mu)(x-\mu) + \mu^4
$$


So we have,


$$
\begin{array}{l}
\mathbb E\left(x^{4}\right)=\int_{-\infty}^{\infty} x^{4} \cdot \frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x=\int_{-\infty}^{\infty} 

\frac{(x^2 + \mu^2)(x+\mu)(x-\mu)}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x  + \mu^4 \\

= \int_{-\infty}^{\infty} \frac{(x^2 + \mu^2)(x+\mu)}{2\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d (x-\mu)^2  + \mu^4 \\

= -\int_{-\infty}^{\infty} \frac{\sigma(x^2 + \mu^2)(x+\mu)}{\sqrt{2 \pi}} d e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}  + \mu^4 \\

=\underbrace{\left(- \frac{\sigma(x^2 + \mu^2)(x+\mu)}{\sqrt{2 \pi} } e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} \right)^{\infty}}_{0} +  \int_{-\infty}^{\infty} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d \frac{(x^2 + \mu^2)(x+\mu)}{2\sqrt{2 \pi} \sigma}  + \mu^4\\ 

=\small 0 + \sigma^2(3*E(x^{2}) +2 \mu E(x) +\mu^2)  + \mu^4 \\
= \small 3\sigma^4 +6\mu^2\sigma^2 + \mu^4

\end{array}
$$

**For** $\mathbb E[\bar{X}_{n}] = \mathbb{E}[X_{1}]$,
$$
\mathbb{E}\left[\bar{X}_{n}\right]=\frac{1}{n} \sum_{i=1}^{n} \mathbb{E}\left[X_{i}\right]=\mathbb{E}\left[X_{1}\right]
$$
![[eq2]](https://www.statlect.com/images/mean-estimation__10.png)

EXY?

### Variance of Gaussian:

**For** $\mathbb V[x] = \sigma^2$,

With integral formulas step by step, we can get:


$$
\begin{aligned}
V &=\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi} \delta} e^{-\frac{(x-u)^{2}}{2 \delta^{2}}}(x-u)^{2} d x \\
&=\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi} \delta} e^{-\frac{x^{2}}{2 \delta^{2}}} x^{2} d x \\
&=-\frac{\delta}{\sqrt{2 \pi}} \int_{-\infty}^{+\infty} x d\left(e^{-\frac{x^{2}}{2 \delta^{2}}}\right) \\
&=-\frac{\delta}{\sqrt{2 \pi}}(\underbrace{\left.x e^{-\frac{x^{2}}{2 \delta^{2}}}\right|_{-\infty} ^{+\infty}}-\int_{-\infty}^{+\infty} e^{-\frac{x^{2}}{2 \delta^{2}}} d x) \\
&=\frac{\delta}{\sqrt{2 \pi}} \int_{-\infty}^{+\infty} e^{-\frac{x^{2}}{2 \delta^{2}}} d x \\
&=\delta^{2}
\end{aligned}
$$



Which can be simplified with expectation substitutions we concluded above:



$$
\begin{aligned}
V(x) &=E\left((x-E(x))^{2}\right) \\
&=E\left(x^{2}-2 x E(x)+E^{2}(x)\right) \\
&=E\left(x^{2}\right)-2 E(x) E(x)+E^{2}(x) \\
&=E\left(x^{2}\right)-E^{2}(x) \\
&=E\left(x^{2}\right)-\mu^{2} \\
&=\sigma^2
\end{aligned}


\\
$$



**For** $\mathbb V[x^2] = 2\sigma^4+4\sigma^2\mu^2$,

$$
\begin{aligned}
V(x^2) &=E(x^{4})-E(x^2)^{2} \\
&=3\sigma^4 +6\mu^2\sigma^2 + \mu^4 - (\sigma^2 + \mu^2)^2\\
&=2\sigma^4+4\sigma^2\mu^2
\end{aligned}


\\
$$



$V(\bar X_n)=\large\frac{\sigma^2}{n}$

![[eq3]](https://www.statlect.com/images/mean-estimation__14.png)

### Covariance

Normally, we have standard covariance formula between variable $x$ and $y$,


$$
\text{Cov}(x,y) = E\left[\ (x-E[x])\ (y-E[y])\ \right]
$$


![image-20220205160543840](https://chqwer2.github.io/img/Typora/image-20220205160543840.png)

![image-20220213171530998](https://chqwer2.github.io/img/Typora/image-20220213171530998.png)

[pdf](file:///C:/Users/calvchen/Downloads/408jointdiscrete(1).pdf)

You should have something like:
$$
\begin{array}{c}
E\left(|X-Y|^{a}\right)=\iint_{x>y}(x-y)^{a} d x d y+ \\
\iint_{y>x}(y-x)^{a} d x d y=2 \iint_{x>y}(x-y)^{a} d x d y
\end{array}
$$
Now:
$$
\begin{array}{c}
\iint_{x>y}(x-y)^{a} d x d y=\int_{y=0}^{1} \int_{x=y}^{1}(x-y)^{a} d x d y \\
=\frac{1}{(a+1)(a+2)}
\end{array}
$$

So:

$$
\begin{array}{c}
E\left(|X-Y|^{a}\right)=2 \iint_{x>y}(x-y)^{a} d x d y \\
=\frac{2}{(a+1)(a+2)}
\end{array}
$$

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


If the covariance between two random variables is 0, then they are independent?

False, the criterion for **independence** is $F(x,y)=F_X(x)F_Y(y)$

**variance of ln function**

![image-20220216223016542](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220216223016542.png)


### Limitations

$$
\lim_{n\to\infin}\left( 1-\frac{c}{n} \right)^n \to e^{-c}
$$



$$
\sum^\infin_{i=1}\alpha^i=\frac{\alpha}{1-\alpha}, iff\ |\alpha|<1
$$

*Food for thought:*



[What is the variance of the maximum of a sample?](https://stats.stackexchange.com/questions/15970/what-is-the-variance-of-the-maximum-of-a-sample)



##### Maximum of uniform random variables

$M_n$

b = - (2*barX_n + 1.6448^2/n) 

(2*barX_n + 1.6448^2/n + sqrt((2*barX_n + 1.6448^2/n) &2-4*barX_n^2) )/2
