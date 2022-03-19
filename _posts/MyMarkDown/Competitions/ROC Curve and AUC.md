### ROC Curve

Receiver Operating Characteristic

混淆矩阵 ??

roc曲线上每个点反映着对同一信号刺激的感受性。

For a binary classification,

**横轴**：负正类率(false postive rate FPR)特异度，划分实例中负例占所有负例的比例；(1-Specificity)

**纵轴**：真正类率(true postive rate TPR)灵敏度，Sensitivity(正类覆盖率)（**又是召回率recall**）

(1)真正类率(True Postive Rate)TPR: **TP/(TP+FN)**,代表分类器预测的**正类中**实际正实例占所有正实例的比例。Sensitivity

(2)负正类率(False Postive Rate)FPR: **FP/(FP+TN)**，代表分类器预测的**负类中**错误正实例占所有负实例的比例。1-Specificity 

(3)真负类率(True Negative Rate)TNR: **TN/(FP+TN)**,代表分类器预测的**负类中**实际负实例占所有负实例的比例，**TNR=1-FPR**。Specificity

![img](https://pic3.zhimg.com/80/v2-ce492c1ee86e8bf2f70fc0c2f4721996_720w.jpg)

理想目标：TPR=1，FPR=0,**即图中(0,1)点，故ROC曲线越靠拢(0,1)点，越偏离45度对角线越好，**Sensitivity、Specificity**越大效果越好**



### AUC - Area Under Curve

只能用于二分类模型的评价，使用AUC或者logloss可以避免把预测概率转换成类别。







