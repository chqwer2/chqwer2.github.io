

# Self Supervised

![image-20220604120001002](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604120001002.png)

Question: If we can learn good latent representation, how can we leverage that for sub-stream model?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604120343707.png" alt="image-20220604120343707" style="zoom:33%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604120351789.png" alt="image-20220604120351789" style="zoom:33%;" />

### Why Self-supervised?

![image-20220604120453327](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604120453327.png)

unlabeled data on the internet.

Babies learn from experimenting without actual labels



Data provides itself own supervision

Withhold some part of the data depending on the mask, task the neural network to predict.

**What is proxy loss or pretext task here?**

![image-20220604121101438](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604121101438.png)

### Color - Depth?



### Denoising Autoencoder

![image-20220604121903835](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604121903835.png)

**Setting Up**

![image-20220604121956722](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604121956722.png)

You can think of GS as a distorted version back onto the tangent hyperplane.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604122244613.png" alt="image-20220604122244613" style="zoom:25%;" />

**Separate the pixel that has been noised.**

It can prevent the model to learn identity function

![image-20220604122319960](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604122319960.png)

MSE and BCE equally good.

Masking works well with **Sigmoid** Activation, what suitable for ReLU?

What is that means?

### Context Encoder

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604152622174.png" alt="image-20220604152622174" style="zoom:33%;" />

![image-20220604152818591](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604152818591.png)

L2 + Adversarial Discriminator Loss

Want to produce something sharper.



Seg or Depth Estimation

Predict one view from other (Grey 2 RGB)

![image-20220604153706979](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604153706979.png)

![image-20220604154012422](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604154012422.png)



HHA Depth Channels



Rotation 0, 90, 180, 270



### Skip Word2Vec Part in About 1H Time Stamp

### Contrastive Predicting Coding

![image-20220604160013317](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604160013317.png)

### Contrastive Learning

#### Momentum Contrast (MoCo)

Large BS or Memory Bank?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604160901402.png" alt="image-20220604160901402" style="zoom: 33%;" />



![image-20220604160919641](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604160919641.png)

### simCLR

Geff Hinton

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604161306077.png" alt="image-20220604161306077" style="zoom:33%;" />

DA like **GaussianBlur** 

### MoCov2

![image-20220604161833572](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604161833572.png)