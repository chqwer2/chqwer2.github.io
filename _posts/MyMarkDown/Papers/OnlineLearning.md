# Online Learning

2013年google的论文：Ad Click Prediction:a View from the Trenches，给出了FTRL的工程实现

用于更新在线的CTR预估模型。

腾讯的开源PS angel上已经支持

https://github.com/Angel-ML/angel/blob/master/docs/algo/ftrl_lr_spark.md

在线学习里有不少是最优化的知识，比如证明regret bounds，但我毕竟在工业界，更关心这些算法是怎么做迭代的，即权重W是怎么更新的。

online learning是基于stream的data，无法直接对目标优化，普遍会选择regret作为优化目标。
$$
Loss = \sum_{t=1}^Nf_t(w_N)-\sum_{t=1}^Nf_t(w_*)\\
Regret = \sum_{t=1}^Nf_t(\textcolor{red}{w_t})-\sum_{t=1}^Nf_t(w_*)
$$

#### **看似不相干的重要特性：稀疏解**

直观上，batch的梯度下降无法使用。所以考虑mini-batch或者SGD。

不同于 Batch，Online 中每次  的更新并不是沿着全局梯度进行下降，而是沿着某个样本的产生的梯度方向进行下降，整个寻优过程变得像是一个“随机” 查找的过程(SGD 中  Stochastic 的来历)，这样 Online 最优化求解即使采用 L1 正则化的方式， 也很难产生稀疏解。



















