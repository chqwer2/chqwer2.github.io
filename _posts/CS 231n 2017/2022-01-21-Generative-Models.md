---
layout:     post
title:      "Generative Models"
subtitle:   " \"Gans\""
date:       2022-01-21 17:00:00
author:     "Calvchen"
header-img: "img/about-bg-walle.jpg"
catalog: true
tags:
    - GANs
    - ML



---

> “Generative Models is the Next Generation of Models ”

## Gernerative Models

#### Unsupervised Learning

**Data:** Just x, no labels!

**Goal:** Learn some underlying hidden structure of the data

**Examples:** Clustering, Dimensionality Reduction, Feature Learning, Density Estimation, etc. 



#### How Can Model Generate?

Models learn data distribution or latent representations from the inputs…

![GAN-Data](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\in-post\CS231n\GAN-Data.png)



#### History of Gans

![GAN-Data](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\in-post\CS231n\Taxonomy.png)



##### Pixel RNN / CNN

Is a **Fully Visible Belief Network** (Explicit density model)

Use chain rule to decompose likelihood of an image $x$ into production of 1-d distributions, then maximize it:
$$
p(x)=\prod\limits^n_{i=1} p(x_i|x_1,...x_{i-1})
$$
$p(x)$ is the Likelyhood of Image $x$,  

$p(x_i|x_1,...x_{i-1})$ is the Probability of $i^{th}$ pixel value given all previous pixels

**Pre-steps:**

1. We need to define the ordering of “previous pixels”
2. Complex distribution over pixel values $\to$ Express using a NN!



#### Variational AutoEncoders (VAEs)

VAEs define intractable density function with latent $z$, which can be seen as the most representitive features:
$$
p_\theta(x)=\int p_\theta(z) p_\theta(x|z)dz
$$
**Cons**: Cannot optime directly, derive and optimize lower bound on likelihood instead!



#### GANs

**So far…**



