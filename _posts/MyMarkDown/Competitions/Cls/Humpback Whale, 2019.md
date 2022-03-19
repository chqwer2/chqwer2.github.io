



# Humpback Whale Identification, 2019

Can you identify a whale by its tail?

## Content

Code: https://github.com/earhian/Humpback-Whale-Identification-1st-

Do 2-class classification for each whale class.

## Training

Senet154 model,  input size is (512, 256) + （ RGB + masks ）

Step 1: Training within all labels with >10 samples (this step helps to converge faster and easier)

Step 2: Training with all samples, and fixed all of the networks except the last two layers.

## Tricks

**- Pseudo labels (+ 0.001)**
We added around 2000 test images (with confidence > 0.96) into our training set

**- Class balance (+0.001 ~ 0.002)**
During our continuous improvements (from 0.8+ to 0.96), we found that the number of labels are correlated with scores. 

Thus: For top 5 predictions class1 to class5, if: **conf class1 – conf class 2 < 0.3**, and class 2  is not used in all top 1 predictions, and class 1 has been used in top 2 predictions for many times, we switch class1 and class2’s positions.



![image-20211012222939766](https://chqwer2.github.io/img/Typora/image-20211012222939766.png)





![image-20211012223019262](https://chqwer2.github.io/img/Typora/image-20211012223019262.png)



## 3rd Solution with Code

Code https://github.com/pudae/kaggle-humpback

**With ArcFace** (https://arxiv.org/pdf/1801.07698.pdf

DA horizontal flip to enlarge twice big

- average blur, motion blur
- add, multiply, grayscale
- scale, translate, shear, rotate
- align or no-align

Model

- Following the paper, 

  the layers after last convolution were replaced to flattening -> BN -> dropout -> FC -> BN

- densenet121

- m 0.5 (the default value of the paper)

- weight decay 0.0005, droupout 0.5

### Inference 

**getting embedding feature for identity**

- For each images, I got multiple feature vector by using 5 bounding boxes and landmarks.
- For each identities, the center of all feature vectors was used as final embedding feature.

**getting embedding feature for test image**

- For each images, multiple feature vectors were generate and the center of the feature vectors was used.

**computing similarity**

- The cosine similarity of above two feature vectors was used as the measure of similarity.

**selecting threshold**

- The threshold for new whale was selected so that the proportion of new whale is about 0.276.

### Results

**without landmark**

At first, I excluded the  identities having only one image and new whales from the training set.  For inference, the identity of the most similar image of the training  set was used as the predicted identity.

> Public LB: 0.90, Private LB: 0.90

After using the center of all feature vectors in the same identity, I got

> Public LB: 0.942 / Private LB: 0.939

After using weight decay 0.0005

> Public LB: 0.946 / Private LB: 0.946

After including the identities having one image to training set

> Public LB: 0.963 / Private LB: 0.961

**with landmark**

When I used aligned image, network was trained faster but the score was not improved.

> Public LB: 0.962 / Private LB: 0.959

The bounding boxes and landmarks of some images are very poor and it seems  to prevent improving scores. So I also used non-aligned images.

> Public LB: 0.965 / Private LB: 0.961

Finally, I doubled up identities by horizontal flip. Flipped images have  different identities but visually very similar. So I set the logit value of flipped to zero to prevent flowing gradient.

> Public LB: 0.968 ~ 0.971 / Private LB: 0.965 ~ 0.968







