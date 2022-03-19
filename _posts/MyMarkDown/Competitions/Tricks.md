## Tricks

### Public Code

Keras SWA: https://github.com/kristpapadopoulos/keras-stochastic-weight-averaging
Pytorch SWA: https://github.com/timgaripov/swa

### Classification

1. Reg + Cls FC (Blind)

2. **CNN trained with Patchs** **(Protein)**

   After training, outputs of CNN are used as confidence (Confidence is outputs from cnn after softmax.) which tells you  how much the corresponding patch represents labels of the original  image.

   I use patches with high confidence to train a new model for better accuray. At last I apply **weighted average** on cnn outputs of image patches to predict labels of the original image.

3. Oversample uncommon classes x2 (8,9,10,15,16,17,20,24,26,27)


### Segmentation

1. clustering - cluster similar patches together. KNN neighbours can be used in pre-post processing, data augmentation/balancing etc.  clustering can be done for input or output or paired input-output
2. Train a classifier to predict kaggle metric score (LB score). This can be used for post processing.
3. combine the patches into a bigger image (jigsaw puzzle problem)
4. pesudo-labeling, semi-suervised learning, knowledge distillation, adversarial training
5. more labeling or supervisory signal (regularization by additional learning  task). e.g create distance transform regression target and train network to predict it
6. train binary classifier to predict if the mask is empty or not. Train another network for segmentation.
7. instead of single class segmentation, you can consider multiclass (e.g. treat  mask of different size, location, different image texture as different  class)
8. label train/sample as difficult or easy using  prediction confidence. break big problems into smaller ones. difficult  samples can have more post/pre processing, etc …

**CVPR 18 DeepGlobe challenge.**

"Land Cover Classification from Satellite Imagery With U-Net and Lovasz-Softmax Loss" - Alexander Rakhlin, CVPR 2018

### Test Trick

1. MMT (Mutual Mean-Teaching) trick in open code, BN adapt to target space

   Link: https://zhuanlan.zhihu.com/p/265758275

   MMT Code:  https://zhuanlan.zhihu.com/p/116074945

   ```
   source = model(source_img)
   target = model(target_img)
   loss(source, target)
   ```

   <img src="https://chqwer2.github.io/img/Typora/image-20211013144108127.png" alt="image-20211013144108127" style="zoom: 67%;" />

2. 

分类问题用dropout ，只需要最后一层softmax 前用基本就可以了，能够防止过拟合，可能对accuracy提高不大，但是dropout 前面的那层如果是之后要使用的feature的话，性能会大大提升



不同尺寸的[feature maps](https://www.zhihu.com/search?q=feature+maps&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A216788968})的concat，只用一层的feature map一把梭可能不如concat好，pspnet就是这种思想，这个思想很常用

但是在concat之前最好加个L2 Normalize?

针对于[metric learning](https://www.zhihu.com/search?q=metric+learning&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A216788968})，对feature加个classification 的约束通常可以提高性能加快收敛



检索问题来说，上个pca降维，能提升至少2个点。

ROC 曲线？ 

![image-20211201164516557](https://chqwer2.github.io/img/Typora/image-20211201164516557.png)

