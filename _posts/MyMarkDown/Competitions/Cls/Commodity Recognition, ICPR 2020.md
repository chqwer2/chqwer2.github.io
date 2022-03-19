# Commodity Recognition, ICPR 2020

Fine-grained classification, classes: 10000 (<20 for each class)

Resnest + [GeM pooling](https://confluence-apps-us.asml.com:8443/display/~calvchen/Gem+Pooling) for final feature map +  + BNNeck for every classifier

Loss: CircleSoftmax + FocalLoss, CrossEntropy Loss

![image-20211012213321775](https://chqwer2.github.io/img/Typora/image-20211012213321775.png)

