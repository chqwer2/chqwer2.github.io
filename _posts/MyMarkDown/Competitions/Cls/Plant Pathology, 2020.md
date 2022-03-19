# Plant Pathology, 2020

## Content

Noisy Labels: 1. same image with diff label, 2. same leaf with diff angles

DA: Flip, Blur, Brightness, Contrast, Shift, Scale, Rotate

## Training

EfficientNet worked well for multiple diseases compared to other models relatively.

Categorical Cross Entropy + Focal Loss

800*1024 inputs

CycleGAN generate larger images

## Methodology

- Pseudo Labeling
- SWA
- Label Smoothing (Improved resnet)
- 5 times TTA
- Oversampling (We tried to fit the data balance)

## Didn't Help

- Cutmix & Mixup
- Grid Mask
- Blockout

