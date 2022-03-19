### APTOS 2019 Blindness Detection

设计了⼀个[损失函数](https://www.zhihu.com/search?q=损失函数&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A341961145})，用分类的⽅法也可以达到⽤回归处理的性能。

分享一下我的比赛思路吧，主要有三点：

⼀是“数据 决定了[模型算法](https://www.zhihu.com/search?q=模型算法&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A341961145})的天花板。我当时纯⼿⼯地从⼏万张⽐赛数据集和额外数据集图⽚中筛选出3000多张完全看不清眼球的图⽚，去掉它们后训练的模型在测试集上有明显的提⾼；

⼆是集成尽可能差异性⼤的多个模型的预测结果。模型集成是⽐赛中常⽤的⼿段，所以我训练了多个不同backbone的模型来做集成，涨点很快。

SGD+Nesterov+OneCycleLR 组合

GMM可以将这些特征聚类

#### 模型融合

Average



Stacking OOF

各个OOF预测结果就可以形成新的[特征矩阵](https://www.zhihu.com/search?q=特征矩阵&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A43472504})。新的特征可以继续训练

如果各单一模型的预测结果相关性较低，更容易提升模型表现。当然也有很多高分队伍，几乎是把自己的每一次训练都记录下来，最后第二层里甚至有上百个模型，搭建一个很复杂的模型融合体系。





**数据质量分析**

所谓数据质量分析，就是分析数据的**缺失值、重复值、异常值、歧义值、正负样本比例**（样本不平衡）等特性。

第一，对单个变量的统计分析。比如考察单个变量的均值、中位数、众数、分位数、方差、变异系数等。常用的工具有：直方图、箱线图、小提琴图等。

第二，对两个变量的统计分析。这里主要考察的是两个变量统计分布之间的关系。常用的工具包括散点图、相关性分析图、热力图等。

第三，对多个变量的统计分析。可以使用彩色的散点图，或者RadViz（详见[https://www.scikit-yb.org/en/latest/api/features/radviz.html](https://link.zhihu.com/?target=https%3A//www.scikit-yb.org/en/latest/api/features/radviz.html)）

![img](https://pic2.zhimg.com/80/v2-15edb0362926b36dc0a8907ed8d66981_720w.jpg)

数据分布分析指的是考察某个字段或某些字段的统计分布。包括频数、时间、空间三个方面。

**[频数统计](https://www.zhihu.com/search?q=频数统计&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A149769029})**

。用概率论的语言讲叫累积分布函数CDF。比如在IJCAI2018阿里妈妈国际广告算法大赛中，我们就统计了不同点击次数下各有多少用户。基于类似的累积分布函数图我们就可以知道用户行为的分布情况，进而可以帮助我们充分理解数据。

**时间维度上的统计分布。**我们可以观察事件发生的趋势和周期性，这里会涉及不少时间序列的知识。比如下图所示的“每天的[点击数](https://www.zhihu.com/search?q=点击数&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A149769029})

趋势”，就是在时间维度上考察点击数的变化情况。 

**空间维度上的统计分布**，我们可以寻找某个变量在地理位置上的相关关系。比如2020年以来我们十分熟悉的疫情地图，就是一种空间上的分布分析。

另外，以上三种分析常常结合**分组**or**聚类**方法，对细分的业务场景进行考察，为后面的数据建模做铺垫。

**数据规范化**

- Min-Max
- Z-score
- MaxAbs

**特征构造举例**

[https://t.zsxq.com/IMfe2vB](https://link.zhihu.com/?target=https%3A//t.zsxq.com/IMfe2vB)

**特征选择**

前面你构造了很多特征，但这些特征不一定都是有用的，需要用特征选择的办法把有用的特征选出来。Feature selection is a process that chooses an optimal subset of  features。特征选择可以帮你筛选有效特征，消除冗余信息，提高训练效率，避免模型发生过拟合。

![img](https://pic2.zhimg.com/80/v2-0fe592f7a6d9b49558d231b1d3e3f529_720w.jpg)

我一直觉得特征选择是那种烂大街的知识。可问题是，这些方法都要用吗？哪个好用？哪个效率最高？[https://t.zsxq.com/IMfe2vB](https://link.zhihu.com/?target=https%3A//t.zsxq.com/IMfe2vB)

![image-20211201104038018](https://chqwer2.github.io/img/Typora/image-20211201104038018.png)

![img](https://pic2.zhimg.com/80/v2-dae4b683311800c0722e8a81aa6526d9_720w.jpg)

https://link.zhihu.com/?target=https%3A//t.zsxq.com/IMfe2vB

![preview](https://pic1.zhimg.com/v2-f88bc85b8dc00e7ba608822bc3733d44_r.jpg)

大卫的知识星球： https://link.zhihu.com/?target=https%3A//t.zsxq.com/IMfe2vB



[Andrew Lukyanenko](https://www.zhihu.com/search?q=Andrew+Lukyanenko&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A80787886})：

此外，追踪当前一些最新的Kaggle Kernels和论坛观点也非常重要。

领域专业知识将为团队带来很大优势，因此我寻找每一条这样的信息。当然，我关注了几个活跃的专家并拜读了他们撰写的文章以及创建的kernels。

[towardsdatascience](https://link.zhihu.com/?target=https%3A//towardsdatascience.com/a-story-of-my-first-gold-medal-in-one-kaggle-competition-things-done-and-lessons-learned-c269d9c233d1)

