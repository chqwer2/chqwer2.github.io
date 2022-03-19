# Human Protein Atlas, 2019

## Content

Link: https://www.kaggle.com/c/human-protein-atlas-image-classification/discussion/78109

Challenge: Extreme **Imbalance**, rare classes hard to train and predict but play an important role in the score.

Solution: Participants may find it helpful to balance distributions of multilabel data across splits for cross validation (i.e., stratify the data).  Earlier this year I created a Python package called  iterative-stratification that aims to accomplish this task for  multilabel data: https://github.com/trent-b/iterative-stratification. I hope the package may find some utility in this competition.

**DA**: Rotate 90,flip and randomly  Image Patches cropped 512x512 patches from 768x768 images(or crop 1024x1024 patches from 1536x1536 images)

Data Processing: *Calculate mean and std using train+test,and used them before feeding images to the model.*

## Training

1. **Focal Loss** of the whole val set is a relative good **metric** to the model capability

   F1 is not a good metric as it’s sensitive to the threshold  and the threshold is depend on the distribution of the train and val  set.

   I tried to evaluate the capability of a model by set the ratio of each class to the same as train set.

2. Loss Functions: Focal Loss + Lovasz (IoU) to balance recall and precision

   *not use macro F1 soft loss, Cuz batch size is small and some classes are rare*

   I used lovasz loss to let the network balance the precision and  recall. 

   Since we use sigmoid and binary classification on every pixel on **mask prediction tasks**, we can treat 28 labels as 28 pixels and then we  can use lovasz loss on it.

3. lrs=[30e-5, 15e-5, 7.5e-5, 3e-5, 1e-5]，lr decay in [25, 30, 35, 40]

4. **Densenet121 model + head below**

   GAP + GMP, BN(affine=True), Dropout(0.5), FC(1024, True), BN,DO,FC 

5. *Remove about 6000 duplicates samples from v18 external data, using hash method which been used to find test set leak*

   

   

## Trick

1. We predicted the test set by using best focal loss epoch with 4 seeds to random crop 512x512 patches from 768x768 images

2. **Post-processing**: Generate two submission. 

   **keep the ratio of the labels to the public test set**,since we did not know the ratio of the rare classes,I set them to the ratio of the train set.
   The second one was keep the ratio of the labels to the average ratio of train set and public test set.

   Why? Although I tried to add or reduce the count of rare classes by 2-5  samples,the public LB can improve, but this was a dangerous way. I just  only used it to evaluate the possible shakeup.

# Metric Learning

Next step move

Network: resnet50
DA: Rotate 90,flip
Loss Functions: ArcFaceLoss
Scheduler: lr = 10e-5, 50 epochs.

ArcFace: Additive Angular Margin Loss for Deep Face Recognition 
https://arxiv.org/pdf/1801.07698v1.pdf
Deep Face Recognition: A Survey 
https://arxiv.org/pdf/1804.06655.pdf

### Model Details

![image-20211013080831793](https://chqwer2.github.io/img/Typora/image-20211013080831793.png)

```
class ArcFaceLoss(nn.modules.Module):
    def __init__(self,s=30.0,m=0.5):
        super(ArcFaceLoss, self).__init__()
        self.classify_loss = nn.CrossEntropyLoss()
        self.s = s
        self.easy_margin = False
        self.cos_m = math.cos(m)
        self.sin_m = math.sin(m)
        self.th = math.cos(math.pi - m)
        self.mm = math.sin(math.pi - m) * m

    def forward(self, logits, labels, epoch=0):
        cosine = logits
        sine = torch.sqrt(1.0 - torch.pow(cosine, 2))
        phi = cosine * self.cos_m - sine * self.sin_m
        if self.easy_margin:
            phi = torch.where(cosine > 0, phi, cosine)
        else:
            phi = torch.where(cosine > self.th, phi, cosine - self.mm)

        one_hot = torch.zeros(cosine.size(), device='cuda')
        one_hot.scatter_(1, labels.view(-1, 1).long(), 1)
        # -------------torch.where(out_i = {x_i if condition_i else y_i) -------------
        output = (one_hot * phi) + ((1.0 - one_hot) * cosine)
        output *= self.s
        loss1 = self.classify_loss(output, labels)
        loss2 = self.classify_loss(cosine, labels)
        gamma=1
        loss=(loss1+gamma*loss2)/(1+gamma)
        return loss

class ArcMarginProduct(nn.Module):
    r"""Implement of large margin arc distance: :
        Args:
            in_features: size of each input sample
            out_features: size of each output sample
            s: norm of input feature
            m: margin
            cos(theta + m)
        """
    def __init__(self, in_features, out_features):
        super(ArcMarginProduct, self).__init__()
        self.weight = Parameter(torch.FloatTensor(out_features, in_features))
        # nn.init.xavier_uniform_(self.weight)
        self.reset_parameters()

    def reset_parameters(self):
        stdv = 1. / math.sqrt(self.weight.size(1))
        self.weight.data.uniform_(-stdv, stdv)

    def forward(self, features):
        cosine = F.linear(F.normalize(features), F.normalize(self.weight.cuda()))
        return cosine

 def __init__(self,....
     ... ...
    self.avgpool = nn.AdaptiveAvgPool2d(1)
    self.arc_margin_product=ArcMarginProduct(512, num_classes)
    self.bn1 = nn.BatchNorm1d(1024 * self.EX)
    self.fc1 = nn.Linear(1024 * self.EX, 512 * self.EX)
    self.bn2 = nn.BatchNorm1d(512 * self.EX)
    self.relu = nn.ReLU(inplace=True)
    self.fc2 = nn.Linear(512 * self.EX, 512)
    self.bn3 = nn.BatchNorm1d(512)

def forward(self, x):
    ... ...
    x = torch.cat((nn.AdaptiveAvgPool2d(1)(e5), nn.AdaptiveMaxPool2d(1)(e5)), dim=1)
    x = x.view(x.size(0), -1)
    x = self.bn1(x)
    x = F.dropout(x, p=0.25)
    x = self.fc1(x)
    x = self.relu(x)
    x = self.bn2(x)
    x = F.dropout(x, p=0.5)

    x = x.view(x.size(0), -1)

    x = self.fc2(x)
    feature = self.bn3(x)

    cosine=self.arc_margin_product(feature)
    if self.extract_feature:
        return cosine, feature
    else:
        return cosine
```



## 3rd Solutions

Search suitable data augmentation as following [AutoAugment](https://arxiv.org/pdf/1805.09501.pdf). ( Random search instead of RL. )

Focal loss with gamma 2.

For each classes, I choose the thresholds that make the proportion of  positive predictions in validation set are closed to the proportion of  positive examples.