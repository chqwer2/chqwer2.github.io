# Blindness Detection

## Content

5 Classes: 0 - No DR，1 - Mild，2 - Moderate，3 - Severe，4 - Proliferative DR

DA: ***Perspective Transformation***, HorizontalFlip、VerticalFlip、Randomrotate(0, 360)、 zoom(1.0, 1.35)

Train and Test distribution difference: **Remove black-edged**

![image-20211012203635026](https://chqwer2.github.io/img/Typora/image-20211012203635026.png)

## Training

1. Freeze backbone with FC trained for 5 epochs，

   ![image-20211012204025918](https://chqwer2.github.io/img/Typora/image-20211012204025918.png)

2. lrs=[5e-4, 1e-4, 1e-5, 1e-6]，lr decay in [10, 14, 18]，for 20 epochs
3. Ensemble E0 and E3

## Trick

1. With Cls FC and Reg FC, bias = False

![image2021-9-1_9-52-13](C:\MyMarkDown\Image\image2021-9-1_9-52-13.png)

2. Pesudo Label

   900 + from test

![image-20211012204153498](https://chqwer2.github.io/img/Typora/image-20211012204153498.png)