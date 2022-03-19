# TGS Salt Segmentation

## Content

Code1: https://github.com/ybabakhin/kaggle_salt_bes_phalanx

Code2: https://github.com/liaopeiyuan/ml-arsenal-public

Classification+Segmentation;

scSE+Unet+hypercolumn?

lovasz+cosine annealing+snapshots

DA：

- HorizontalFlip(p=0.5)
- RandomBrightness(p=0.2, limit=0.2)
- RandomContrast(p=0.1, limit=0.2)
- ShiftScaleRotate(shift_limit=0.1625, scale_limit=0.6, rotate_limit=0, p=0.7)

TTA: Horizontal Flip 

### Training

#### Stage 1

Encoder: ResNeXt50 pretrained on ImageNet

Decoder: conv3x3 + BN, Upsampling, scSE

Input: 101 -> resize to 192 -> pad to 224

Optimizer: RMSprop. Batch size: 24

1. Loss: BCE+Dice. Reduce LR on plateau starting from 0.0001
2. Loss: Lovasz. Reduce LR on plateau starting from 0.00005
3. Loss: Lovasz. 4 snapshots with cosine annealing LR, 80 epochs each, LR starting from 0.0001

##### Other model

It was ResNet34 (architecture is similar to resnet_34_pad_128  described below) with input: 101 -> resize to 202 -> pad to 256

Ensemble these two

#### 2nd Stage

**resnet_34_pad_128**

*Input:* 101 -> pad to 128

*Encoder:* ResNet34 + scSE (conv7x7 -> conv3x3 and remove first max pooling)

*Center Block:* [Feature Pyramid Attention](https://arxiv.org/abs/1805.10180) (remove 7x7)

*Decoder:* conv3x3, transposed convolution, scSE + hyper columns

*Loss:* Lovasz

**resnet_34_resize_128**

*Input:* 101 -> resize to 128

*Encoder:* ResNet34 + scSE (remove first max pooling)

*Center Block:* conv3x3, [Global Convolutional Network](https://arxiv.org/abs/1703.02719)

*Decoder:* [Global Attention Upsample](https://arxiv.org/abs/1805.10180) (implemented like senet -> like scSE, conv3x3 -> GCN) + deep supervision

*Loss:* BCE for classification and Lovasz for segmentation

Cosine Annealing LR, 50 epochs each, LR 0.01 -> 0.001



### Tricks

pseudo-labels: Based on the ensemble from the 1st stage, we created a set of confident pseudo-labels

( probability < 0.2 or probability > 0.8 )

Post-processing, jigsaw mosaics:

1. Find all vertical and half-vertical (bottom half of the image is vertical) images in train data
2. All test images below them in mosaics get the same mask
3. Only one test image above them get the same mask, and only if its depth in mosaic >= 3

**Unfortunately, it gave huge boost on Public LB and no boost on Private:**

