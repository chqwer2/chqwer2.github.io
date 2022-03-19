### “Unbiased Teacher For Semi-Supervised Object Detection“， ICLR 2021

联合训练一个逐渐进步的teacher和一个student，其中基于class-balance loss 对那些overly confident pseudo-labels降低权值

一开始训练用标注数据（burn-in），联合训练包括两步：固定teacher产生伪标注，用以训练student，而基于exponential moving average (EMA)，学习的知识迁移给渐渐进步的teacher。

![img](https://pic3.zhimg.com/80/v2-b6ca5564dcc2cb47a682dd37e3aa298a_720w.jpg)



### “DetCo: Unsupervised Contrastive Learning for Object Detection“，arXiv 2102.04803，2，2021

完全无监督学习方法，DetCo，充分发挥全局图像和局部图像patch之间的对比来学习目标检测的鉴别性表示方法。这里contrastive learning方法设计了一个detection friendly contrastive pretext task  用于学习大规模无标注数据。

代码将开源：[http://github.com/xieenze/DetCo](https://link.zhihu.com/?target=http%3A//github.com/xieenze/DetCo) 和 [http://github.com/open-mmlab/OpenSelfSup](https://link.zhihu.com/?target=http%3A//github.com/open-mmlab/OpenSelfSup)。

整个流水线如图：和何凯明的MoCo对比（“**Momentum contrast for unsupervised visual representation learning**“）；（a）MoCo的框架，仅从全局角度考虑高级特征和learning contrast；（b）DetCo，直接附加分层的中间contrast和两个附加的局部patch视角做输入，在全局和局部表示中建立对比损失。

![img](https://pic4.zhimg.com/80/v2-76e69c1a437ee77f26072a7b80f08d9f_720w.jpg)

列出三个做法：（1）实例判别优于分类或聚类，可以作为目标检测的pretext任务。  （2）pretext任务应在目标检测时保持低级和高级特征的鉴别性。  （3）除了全局图像特征外，局部patch特征对于目标检测也很重要。由此，DetCo提高检测的迁移能力。 注：“ T”-图像变换，“  L12g”-跨局部和全局特征的对比损失。 “ Queueg/l”表示全局/局部特征的不同memory banks。

训练的Data augmentation方法和MoCo一样，代码基础是：[https://github.com/open-mmlab/OpenSelfSup](https://link.zhihu.com/?target=https%3A//github.com/open-mmlab/OpenSelfSup)。      

​         

### “Towards Open World Object Detection“，arXiv 2103.02603，3，2021

其中：1) 在没有显式监督的情况下确认未知目标； 2)  步进地学习这些确认的未知类，这些对应数据的标注渐进地收到，这样能够不会忘记之前学习的类。ORE（Open World Object  Detector）, 主要是基于一种聚类，即contrastive clustering，和基于能量的模型，即Energy based  models (EBMs)，对未知目标确认。

代码见：[https://github.com/JosephKJ/OWOD](https://link.zhihu.com/?target=https%3A//github.com/JosephKJ/OWOD)

个方法示意图如下：基于Faster-RCNN

![img](https://pic2.zhimg.com/80/v2-b8dcebc12670757feab23d4cfa17080d_720w.jpg)

关于contrastive learning的contrastive loss定义如下：

![img](https://pic4.zhimg.com/80/v2-9b3f9af0229eb16a8d62ba4cc031b813_720w.jpg)

而对应的算法如图：

![img](https://pic2.zhimg.com/80/v2-317d14b97aea07f83f80a71f22f49f21_720w.jpg)



### Consistency-based Active Learning for Object Detection“， arXiv 2103.10374，3，2021

主动学习，要找informative samples，而这里的Consistency-based Active Learning method for object  Detection (CALD)，探索原始数据和增强无标注数据之间的一致性。CALD不仅测量各个信息挑选样本，还用mutual  info达到数据分布平衡。这里还是采用faster RCNN。

代码见 [https://github.com/we1pingyu/CALD](https://link.zhihu.com/?target=https%3A//github.com/we1pingyu/CALD) 

如下表是三个方法性能比较：CALD、LL4AL 和 VAAL

![img](https://pic4.zhimg.com/80/v2-435bebfb6f976b3d6c24eaa3f01cc3a7_720w.jpg)

CALD的示意图如下：每个循环包括metric calculation, data sampling 和 model  training，其中数据分为标注池和无标注池，分两步，一是增强无标注数据，和原始数据一起给初始检测器；然后计算各自信息，选择informative sample；二是利用mutual information过滤挑选样本，减轻不平衡分布。

![img](https://pic1.zhimg.com/80/v2-96206564b971a020bae3bb05bdbb33f4_720w.jpg)

CALD具体的两步法示意图如下：采用consistency-based metric提取各自信息挑选样本，然后根据mutual info过滤样本，保持平衡。

![img](https://pic2.zhimg.com/80/v2-f87a4848b0d0daacca35c613682699fd_720w.jpg)

mutual info的计算方法如下：

![img](https://pic3.zhimg.com/80/v2-00f6522d82d870e0aa522b22897f72fa_720w.jpg)