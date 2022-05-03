

**Depthwise Conv**

1. **Split** the input and filter into channels.
2. We convolve each input with the respective filter.
3. We stack the convolved outputs together.

<img src="https://production-media.paperswithcode.com/methods/1_yG6z6ESzsRW-9q5F_neOsg_eaJuoa5.png" style="zoom: 33%;" />



**Pointwise Conv**

1. use a $1\times 1$ conv, usually with more channel 

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/1_37sVdBZZ9VK50pcAklh8AQ_KE6C7Yb.png" alt="img" style="zoom: 33%;" />

**Depthwise Separable Convolution**



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/Screen_Shot_2020-05-31_at_10.30.20_PM.png" alt="img" style="zoom: 33%;" />

paper: https://paperswithcode.com/paper/depthwise-convolution-is-all-you-need-for

N_std = 4 × 3 × 3 × 3 = 108
N_depthwise = 3 × 3 × 3 = 27 
N_pointwise = 1 × 1 × 3 × 4 = 12 
N_separable = N_depthwise + N_pointwise = 39



**Shuffle Block** V2

1. PW has much computation
2. split channel into two partitions, finally the concatted are shuffle

![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/shufflenet-6.jpg)

**c** will be fine..



**Efficient-HRNet**

1. HRNet

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220330174135802.png" alt="image-20220330174135802" style="zoom:50%;" />



**GhostNet**

1x1 remains still bottle neck

1. Few small filters to generate more feature maps
2. 





**Lite-HRNet**

1. Multiple resolutions — parallel branch
2. $1\times 1$ conv too much computation, 
   - replaced with efficient conditional channel weighting unit

**Normal DWSConv**

```mermaid
graph LR

A[1x1 Conv] --> B[3x3 DWConv] -->C[1x1 Conv]
```

**Ours**

```mermaid
graph LR

A[1x1 Conv] -->H--> B[3x3 DWConv] -->F --> C[1x1 Conv]
```

$\mathcal H$ is cross-resolution weighting function. $\mathcal F$ is spatial weighting function.







**EfficientUNet++**