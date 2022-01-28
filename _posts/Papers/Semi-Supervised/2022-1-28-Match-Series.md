---
layout:     post
title:      "Match Series for SSL"
subtitle:   " \"Pseudo-Label Theory\""
date:       2022-01-28 21:50:00
author:     "Calvchen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Semi-supervised
    - Pseudo-Label
    - Paper




---

> “Follow the sequence of MixMatch (NIPS 2019), ReMixMatch (ICLR 2020), FixMatch (NIPS 2020) and FeatMatch (ECCV 2020) ”

## A Starter

Passed few days I went to Liverpool and Manchester, where I found are very historical and relaxing cities to visit. So I am slacking for some days… 

Anyway, for the starter, I am now engaging in the reef-saving competition, which is an object detection based comp with nearly 80% given data unlabeled. So the accuracy of how pseudo labeling is done will be so much influencial and can cause huge PB shaking.

For better implementation, I try to read the papers given above to give me a fast overview of how Match result in better accuracy in **Pseudo-Labeling**.

  

## FixMatch

**FixMatch**: Simplifying Semi-Supervised Learning with Consistency and Confidence

**Contribution**：利用一致性正则化（ Consistency  regularization）和伪标签（pseudo-labeling）技术进行无监督训练。SOTA  精度，其中CIFAR-10有250个标注，准确率为94.93%。甚至仅使用10张带有标注的图在CIFAR-10上达到78％精度。

[[Paper]](https://arxiv.org/abs/2001.07685), [[Code]](https://github.com/google-research/fixmatch)

#### Methods

A combination of **Consistency Regularization** and **Pseudo-labeling**.

![img](https://pic3.zhimg.com/80/v2-21388836987e72bff390f7f4a3ade136_720w.jpg)

The workflow is training in two stages: Supervised (route above) and Un-supervised (route below). 



##### **Consistency Regularization** 

**自洽正则化**

Based on the **hypothesis** that Same image going through different disturbance (Enhancement) will yield same result by the network.

Thus, we can calc the differences between them for semi-supervision:
$$
\text{Minimize } || P_{m}(y| \alpha_1(x);\theta) - P_{m}(y| \alpha_2(x);\theta)   ||^2_2
$$
where $\alpha$ represents for augmentation.

##### Pseudo-Labeling

Given confidence threshold $\tau$, $\hat q_b = argmax(q_b)$:
$$
\frac{1}{\mu B}\sum^{\mu B}_{b=1}\mathbb{1}(max(q_b)>\tau)\text{H}(\hat q_b,q_b)
$$
For generating on-hot possibility distribution.

##### **Algorithm Details**

![preview](https://pic3.zhimg.com/v2-bd6c08f88ed0a8f11c1eb2c445b78a2a_r.jpg)

##### Losses

$\alpha $ represents weak data augmentation, including flip, shift,etc.

$\mathcal{A}$ represents strong data augmentation, including color transformation, contrast enhancement, rotation, etc.
$$
\ell_s = \frac{1}{B}\sum^B_{b=1}\text{H}(p_b,p_m(y|\alpha(x_b)))
$$

$$
\ell_u=\frac{1}{\mu B}\sum^{\mu B}_{b=1}\mathbb{1}(max(q_b)>\tau) \text{H}(\hat q_b,p_m(y|\mathcal{A}(u_b)))
$$

##### Strong Augmentation

Apply **RandAugment** and **CTAugment** strategies. Chose $N$ aug with $p=50\%$ and magnitude $M=50\%$ each.

Table of **RandAugment**.

![img](https://pic4.zhimg.com/80/v2-108d1a4c84bc45c1ed7ce93ecfa228ab_720w.jpg)

##### Summary

Weak aug can not driven model to learn intrinsic features that may result in overfiting. However, strong sug can result in severe image distort while keeping important features…



### MixMatch

just started..

##### Entropy Minimization

**最小化熵**

discussed in the MixMatch Paper. 