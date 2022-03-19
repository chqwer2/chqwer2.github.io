# Hardware and Efficient Methods

![image-20211104092903467](https://chqwer2.github.io/img/Typora/image-20211104092903467.png)

## Prune & Re-train

![image-20211104093504093](https://chqwer2.github.io/img/Typora/image-20211104093504093.png)

![image-20211104093529647](https://chqwer2.github.io/img/Typora/image-20211104093529647.png)

### Low Rank Approximation for FC:

SVD to separate the matrix

![image-20211105213252729](https://chqwer2.github.io/img/Typora/image-20211105213252729.png)?

![image-20211105213635059](https://chqwer2.github.io/img/Typora/image-20211105213635059.png)?

Winograd binary and termary

## Weight Sharing and Trained Quantization (For TPU)

# Hardware

## TPU

25x GPU, more than 100x CPU

24 Mega byte cache > 16 Mega byte in GPU

HBM GPU?

TeraOper / sec

# Efficient Training

## Parallization

Data parallel -> batch size larger

Model parallelism -> split the model

![image-20211106170421457](https://chqwer2.github.io/img/Typora/image-20211106170421457.png)

![image-20211106170611815](https://chqwer2.github.io/img/Typora/image-20211106170611815.png)

![image-20211106170819798](https://chqwer2.github.io/img/Typora/image-20211106170819798.png)

![image-20211106171234627](https://chqwer2.github.io/img/Typora/image-20211106171234627.png)
