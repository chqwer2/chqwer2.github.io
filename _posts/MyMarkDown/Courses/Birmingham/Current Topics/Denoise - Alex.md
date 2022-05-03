# Denoising in Medical Imaging

In some medical Imaging, high exposure resulting in clean image but can cause some damages, thus we use low exposure (which contains huge noise.)



![image-20220322145653670](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322145653670.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322163748529.png" alt="image-20220322163748529" style="zoom:25%;" />

Because photon is discrete that we decrese certain amount of photon which will result in noise.

**What is the ditribution of the photon that we really receive in reality?**

It is a Poisson.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322164220151.png" alt="image-20220322164220151" style="zoom:25%;" />



Where $s_i$ is the average amount of photons that should be received (the light we put on it), $x_i$ is the photons we really detected.

Given a certain exposure time,  detector receive the photons follows the poisson.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322165321577.png" alt="image-20220322165321577" style="zoom:30%;" />

If we increase the light intensity, the $\sigma$ will spread.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322165301728.png" alt="image-20220322165301728" style="zoom:25%;" />







How to present acceptable quality?

### What is Fluorescence Microscopy?

![image-20220322150122006](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322150122006.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322151335629.png" alt="image-20220322151335629" style="zoom:33%;" />



The disadvantage is this method is that you only can process one plane at a time and some background to the image.

You only have straight light in the image (can not form 3D structure)

Now we change the light resources to focus on one point to get 3D example..

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322151931223.png" alt="image-20220322151931223" style="zoom:25%;" /><img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322151952928.png" alt="image-20220322151952928" style="zoom:25%;" />



Now we have a photodiode which treat each pixel evenly?



### Why is too much light harmful?

- Living cells do not like the light, which prevent them from deviding, even can damage or kill the cell.
- Photobleaching: more light you put into it, the more damage you cause. The image will become darker and darker.. 

Photons per pixel..





### How to quantify the Noise?

PSNR

![image-20220322165448417](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322165448417.png)



### Denoising in Supervised Learning

![image-20220322170455587](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322170455587.png)

**What is that mean?**



![image-20220322171019017](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322171019017.png)







![image-20220322171231480](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322171231480.png)

The problem is we cannot describe $p(s)$.

![image-20220322171256179](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322171256179.png)



### Noise2Noise

![image-20220322172527495](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322172527495.png)

Deep Learning trully output the best compromise.

![image-20220322171721894](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322171721894.png)

The reason to drop the $x$ in the right is that the noisy images are independent

The noise is zero arround the signal.

So it can be replaced by clean image $s_i$.

![image-20220322172340744](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322172340744.png)

##### The downside is still require image pairs?

do not need clean image. 





![image-20220322172950679](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322172950679.png)





### Self-supervised Noise2Void

Make some assumption about the nature of the data:

1. Additive Noise and zero-centered
2. You can predict the pixel by looking at its surrounding.

![image-20220322173611010](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322173611010.png)



But when happen we input the image and take it as the target in the same time? We remove the center pixel to prevent it learns the identical mapping.

Why Does it work?

We cannot predict the noise but the signal

![image-20220322174542345](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322174542345.png)



Why it really works?

![image-20220322175009817](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322175009817.png)



![image-20220322175205041](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322175205041.png)

![image-20220322175307893](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322175307893.png)

Some artifacts in the data we cannot see it, but it is preserved.



### Rooms for Improvement

![image-20220322175620737](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220322175620737.png)