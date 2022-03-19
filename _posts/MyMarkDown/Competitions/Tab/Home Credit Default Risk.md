# Home Credit Default Risk

##### 1st Place Solution [link](https://www.kaggle.com/c/home-credit-default-risk/discussion/64821)

Haven't check...

**2nd Place Solution [link](https://www.kaggle.com/c/home-credit-default-risk/discussion/64722)**

*3rd Solution(alijs & Evgeny): [3rd place solution | Kaggle](https://link.zhihu.com/?target=https%3A//www.kaggle.com/c/home-credit-default-risk/discussion/64596)*

*4th Solution(Quad Machine): [4th place sharing and tips about having a good teamwork experience](https://link.zhihu.com/?target=https%3A//www.kaggle.com/c/home-credit-default-risk/discussion/64487)*

相比于3rd的简单stacking策略，该队则倾向搭建超级庞大的stacking体系，因此在生成OOF时用了很多心思。他们尝试记录贝叶斯优化调参过程中的每个OOF预测，来扩大自己的OOF队伍。当然，在特征矩阵过大后，后续也必然结合复杂的特征筛选方法，该队也对OOF特征进行了筛选，这个策略比较独特。

*5th Solution(Kraków, Lublin i Zhabinka): [Overview of the 5th solution [+0.004 to CV/Private LB of your model\]](https://link.zhihu.com/?target=https%3A//www.kaggle.com/c/home-credit-default-risk/discussion/64625)*

作为public榜单遥遥领先的队伍(0.819)，Kraków, Lublin i Zhabinka尽管最后遗憾地跌出奖金区，但在我心里他们依旧是本次比赛最值得关注的队伍之一。几名队员入场较早，也一直通过讨论影响着整个社区。

该队的方法实际上是所有队伍中最与众不同的一个，他们大量参考了很多相关领域文献，依此提取特征；将每个表当作单独的数据源，并充分利用神经网络提取交互信息。