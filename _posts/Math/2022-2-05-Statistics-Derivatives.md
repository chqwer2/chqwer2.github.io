---
layout:     post
title:      "Statistics Theoretical Derivation MIT 18.6501x"
subtitle:   " \"STAT is Fun!\""
date:       2022-01-29 12:00:00
author:     "Calvchen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Math
    - Statistics
    - Course



---

> “Statistics is not perfect, but it is beautiful. ”

# Theoretical Derivation

This post is heavily focused on the mathematical proof and theoretical derivation.





### **Mean of Gaussian:**

$X\sim\mathcal{N}(\mu, \sigma^2),\ (X-\mu)\sim\mathcal{N}(0, \sigma^2) $

**Requires:**
$$
\text { BTW: 无论如何, 也要用到: } \int_{-\infty}^{\infty} \frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x=1
$$


**For** $\mathbb E[x] = \mu$ **:**
$$
\begin{aligned}
E(x) &=\int_{-\infty}^{+\infty} x f(x) d x=\int_{-\infty}^{+\infty} \frac{x}{\sqrt{2 \pi} \delta} e^{-\frac{(x-\mu)^{2}}{2 \delta^{2}}} d x \\

&=\int_{-\infty}^{+\infty} \frac{(x - \mu) + \mu}{\sqrt{2 \pi} \delta} e^{-\frac{(x-\mu)^{2}}{2 \delta^{2}}} d x \\

&=\underbrace{\int_{-\infty}^{+\infty} \frac{x-\mu}{\sqrt{2 \pi} \delta} e^{-\frac{(x-\mu)^{2}}{2 \delta^{2}}} d x}_{0}+ \mu \underbrace{\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi} \delta} e^{-\frac{(x-\mu)^{2}}{2 \delta^{2}}} d x}_{1} \\
&=\mu
\end{aligned}
$$


**For** $\mathbb E[x^2] = \sigma^2 +\mu^2$ **:**
$$
\begin{array}{l}
E\left(X^{2}\right)=\int_{-\infty}^{\infty} x^{2} \cdot \frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x=\int_{-\infty}^{\infty} \frac{(x+\mu)(x-\mu)+\mu^{2}}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x \\
=\int_{-\infty}^{\infty} \frac{(x+\mu)(x-\mu)}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x+\int_{-\infty}^{\infty} \frac{\mu^{2}}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x \\
=\int_{-\infty}^{\infty} \frac{-\sigma(x+\mu)}{\sqrt{2 \pi}} d\left(e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}\right)+\mu^{2} \\
=\left(\frac{-\sigma(x+\mu)}{\sqrt{2 \pi}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}\right)^{\infty}+\sigma^2\int_{-\infty}^{\infty} \frac{1}{\sigma\sqrt{2 \pi}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x+\mu^{2}=0+\sigma^{2}+\mu^{2} \\
\end{array}
$$


**For** $\mathbb E[x^3] = \sigma^2 +\mu^2$ **:**
$$
\text{Same:}\\
(x-y)^3 = x^{3}-3 x^{2} y+3 x y^{2}-y^{3} \\

\begin{array}{l}
E\left(X^{2}\right)=\int_{-\infty}^{\infty} x^{2} \cdot \frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x=\int_{-\infty}^{\infty} \frac{(x+\mu)(x-\mu)+\mu^{2}}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x \\
=\int_{-\infty}^{\infty} \frac{(x+\mu)(x-\mu)}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x+\int_{-\infty}^{\infty} \frac{\mu^{2}}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x \\
=\int_{-\infty}^{\infty} \frac{-\sigma(x+\mu)}{\sqrt{2 \pi}} d\left(e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}\right)+\mu^{2} \\
=\left(\frac{-\sigma(x+\mu)}{\sqrt{2 \pi}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}\right)^{\infty}+\sigma^2\int_{-\infty}^{\infty} \frac{1}{\sigma\sqrt{2 \pi}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x+\mu^{2}=0+\sigma^{2}+\mu^{2} \\
\end{array}
$$
![image-20220205160527082](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220205160527082.png)

### Variance of Gaussian:

$$
\begin{aligned}
V &=\int_{-\infty}^{+\infty}(x-u)^{2} f(x) d x \\
&=\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi} \delta} e^{-\frac{(x-u)^{2}}{2 \delta^{2}}}(x-u)^{2} d x \\
&=\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi} \delta} e^{-\frac{x^{2}}{2 \delta^{2}}} x^{2} d x
\end{aligned}
$$

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


$$
\begin{aligned}
V(x) &=E\left((x-E(x))^{2}\right) \\
&=E\left(x^{2}-2 x E(x)+E^{2}(x)\right) \\
&=E\left(x^{2}\right)-2 E(x) E(x)+E^{2}(x) \\
&=E\left(x^{2}\right)-E^{2}(x) \\
&=E\left(x^{2}\right)-u^{2}
\end{aligned}


\\


$$




Covariance

![image-20220205160543840](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220205160543840.png)

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