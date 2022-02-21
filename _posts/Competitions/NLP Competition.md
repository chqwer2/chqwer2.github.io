# NLP Competiton

- Parameters
- Data Augmentation
- 数据清洗
- 对抗训练+混合精度
- 多模型融合
- 半监督训练



## Models

Bert from **transformers** library and **Huggingface**

RoBERTa, 

1. 用正则或NLTK对句子分句然后分词，另外根据需求涉及stopwords，词型还原等.
2. 用sklearn的*Tfidf*Transformer及CountVectorizer或keras的一些工具将句子向量化，再加上一些其他统计特征.
3. 使用NB,GBDT,FM,LR,NN等方法模型建模,融合.

### Head

https://www.kaggle.com/rhtsingh/utilizing-transformer-representations-efficiently

[code](./NLP Code.md/#Attention Head with multi-layer)

![preview](https://pic2.zhimg.com/v2-9ed6047c8a446a2577cdfd2a330bdf1d_r.jpg)

## Parameters

**Max Sequence Length：**文本的最大长度。需要统计数据的长度来设置，因为缩减了文本的最大长度，相当于对于单卡可以使用更大的Batch Size。

**判别学习率** 有时所有嵌入层都被冻结，头部以较高的学习率进行训练，然后所有层以较低的学习率再次进行训练。

因此，我们实现了一个定制的优化器。我们对RoBERTa基本架构上使用线性递增的学习率，对头部使用固定的1e-3或2e-4(取决于预训练的模型)学习率。学习率从第一层的1e-5开始，到最后一层的5e-5结束。

[code](./NLP Code.md/#RoBERTa-LR)



## Data Augmentation

### Exploratory Data Analysis

1. [nlpaug](https://github.com/makcedward/nlpaug) Library
2. Wikipedia pseudo label
3. 

Use augmented data with weight less than 1.0.

---

## Data Cleaning

- 基于规则：这个需要一些领域知识或者通用常识，通常用正则表达式即可完成。
- 基于模型：这是一种思路，类似于后面的半监督的做法。利用5-fold或者10-fold训练模型，预测数据，对所有数据获得一个模型打标结果，对于那些模型打标很多出现错误的数据进行过滤（过滤规则看需求），这样可以滤除很大一部分噪音数据，对结果一般有较好提升。

---

## Adversarial Training

​        对抗训练通过引入噪声来完成，和CV直接对像素点进行扰动不一样，在NLP中我们一般是通过一些embedding层添加微小扰动来进行对抗学习。根据添加的方法，一般我们使用Fast Gradient Method (FGM)和Projected Gradient Descent (PGD)。这是一篇[介绍FGM 和 PGD的景点文章](https://link.zhihu.com/?target=https%3A//fyubang.com/2019/10/15/adversarial-train/)，也有代码实现。

其实在引入对抗训练后（无论是FGM，还是PGD），都会大大的增长模型训练的时长，其实也就是变相的降低了模型的训练效率，也会影响到模型训练结果。所以**我们一般使用对抗训练的时候，会使用混合精度训练来提升训练效率**。

---

## Emsemble

Use **log-weight** to ensemble models with large differentiation.

