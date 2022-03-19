### Cardiac Magnetic Resonance (CMR) Image Segmentation with Anatomical Knowledge 

by Jinming Duan

![image-20220207090058223](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207090058223.png)

Pathology has thicker RV wall

##### Pre-NN

![image-20220207090002872](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207090002872.png)

MRF - marcov random field

##### Instanizing

Level-set Functions

![image-20220207090343969](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207090343969.png)

region loss + edge loss

![image-20220207090650028](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207090650028.png)



![image-20220207091435837](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207091435837.png)

Affine healthy healthy images to pathology

![image-20220207091736921](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207091736921.png)

Rewrite the functions

![image-20220207092055226](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207092055226.png)



### Learning a Model for Accelerated MR Reconstruction

by Jinming Duan

Build from prior knowledge

![image-20220207092427591](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207092427591.png)

Reconstract undersampled Images to Fullsampling Images in k-space

“D-aliasing Problem”

![image-20220207092857823](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207092857823.png)

Prior term eliminate the many solutions for x…

![image-20220207094417894](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207094417894.png)

Copy-and-paste raw data to Denoised Images

FFT and IFFT iteratively… until gained a clear output

But

•What is the optimal sparsifying transform Φ?

​	Experiments Dependent… 

Low-rank methods, non-local means, dictionary learning

•What is the optimal image prior R?

For the spacity function: 

•What is the optimal trade-off λ?

##### Domain Knowledge

MR physics? Constrained solution space? Structure Similarities?

![image-20220207095921611](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207095921611.png)

##### NN with Domain Knowledge

![image-20220207101316682](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207101316682.png)

Split to two problems



![image-20220207102935088](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207102935088.png)

DC for data consistency

**iterate:**

continously pull the generation space into magnifold plausible space

![image-20220207103304605](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220207103304605.png)

##### Take Home Message

•Countless DL methods have been proposed

​	•And they are repeatedly shown to work very well

​	•More and more research start to integrate prior knowledge to DL models

•DL is becoming less and less of a black-box

​	•Many, many links with the traditional methods

​	•Uncertainty Quantification

​	•Progress in theoretical aspects too

•DL is likely to be the part of the “solution” 

​	•As long as you believe that the answer is in the data

​	•The performance can be further boosted using domain knowledge