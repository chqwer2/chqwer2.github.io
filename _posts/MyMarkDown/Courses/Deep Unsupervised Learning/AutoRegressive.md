### P2 AutoRegressive Model

Learn only histogram -> resulting in smoother (poor generation)

So better we should **parameterize** the distribution.

![image-20220603072809982](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603072809982.png)



So we introduce **function approximation:** to learn $\theta$ of $P_\theta$

It is like a search problem

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603073018255.png" alt="image-20220603073018255" style="zoom:30%;" />



Loss Function:

![image-20220603073057220](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603073057220.png)

Min KL = Max MLE

MLE + SGD = Works well with large dataset, is compitable with NN.

NN allows it to be very expressive

### Design the NN (BayesNet)

![image-20220603073724587](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603073724587.png)



#### Chain Rule

Always possible, break probability into parts

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603073907797.png" alt="image-20220603073907797" style="zoom:33%;" />

But it is problematic when $n$ is large, the table will be fairly big.

So we want to make strong assumption that makes it sparse, make it representable:
$$
P(M|JAEB) \to P(M|A)
$$
That’s what bayes do. 

Now we have NN, we can represent the conditioning as NN.

### AutoRegressive Model

Or it can be called chain rule model.

![image-20220603074420333](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603074420333.png)



#### A Toy Model

![image-20220603074547627](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603074547627.png)

Here we see each layer a processing.



![image-20220603074923529](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603074923529.png)

It is simpler than BayesNet, but still we can shared info into next regressive using **RNN** or **Masking**.



### Masked 

1. Masked MLP (MADE)
2. Masked Conv & Self-attention

### MADE

MAE for distribution estimation

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603104209130.png" alt="image-20220603104209130" style="zoom:33%;" />



You can mask out any variable that comes after you

![image-20220603105129179](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603105129179.png)



**How About Energy-based Model**



Pixel conditio on pixel. So the training time, output is a probability, we want to maximize of what the actual value is there.

So at test time, all we get is a probability distribution. We sample from it, whatsoever the sample is, we bring a specific sample instance down.

We really want to capture the full distribution, rather than the sample mean.

### WaveNet

In unsupervised learning, Usually use 1D conv and dilated conv

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604093211028.png" alt="image-20220604093211028" style="zoom:50%;" />





Now we can have two output, multiply together. Sig and Tan: Sig perform like gating function.

Tanh in some sense propogating signal that you are trying to get through it, a sigmoid can let thing through.

### PixelCNN (+variations)

Masked Spatial Conv

You can have a filter like this.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604104855627.png" alt="image-20220604104855627" style="zoom:33%;" />

Can also work as **Blind Spot**

#### **Gated Pixel CNN**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604105834079.png" alt="image-20220604105834079" style="zoom:30%;" />

### **PixelCNN++**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604110150594.png" alt="image-20220604110150594" style="zoom25%;" />

**Mixture of Logstirc Distribution**, easier than Mixture Gaussian

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604110246552.png" alt="image-20220604110246552" style="zoom:33%;" />

But we need to make it discrete: into bins

**Second is DownSampling** 

![image-20220604110610339](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604110610339.png)

### Masked Attention

Attention is all you need

O(1) params scaling w.r.t data dimension, parallel computation.

Also unlimited receptive field

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604111229236.png" alt="image-20220604111229236" style="zoom:30%;" />

Make it sparse.

##### PixelSNAIL

![image-20220604111650775](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604111650775.png)

But this undergo vanishing gradient?

And saying you want to generate a number, you can feed in a one-hot vector (auxiliary decoder). All generation in condition on that vector.

![image-20220604112213170](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604112213170.png)



### Pixel Recursive

How about grey-scale then cooler, because color is three times far away than greyscale

![image-20220604112600625](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604112600625.png)

### The bad

very slow: takes 11 mins to generate 16 img on Tesle K40

**How to speed it up?** 

Hierarchy: from-course-to-fine

8x8 -> 16x16

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604112833942.png" alt="image-20220604112833942" style="zoom:20%;" />

Cut into many toy boxes runing parallel… 

performing **devide and conquer**.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604112907128.png" alt="image-20220604112907128" style="zoom:33%;" />

### Multi-scale PixelCNN

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604113116763.png" alt="image-20220604113116763" style="zoom:33%;" />



But it is more limited modeling capacity because of the edges, but improve the speed.

![image-20220604113315700](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604113315700.png)

Running coarsely generate the first frame and fifth frame at the same time, to capture long term dependency on the sequence.



### FastPixelCNN

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604113538794.png" alt="image-20220604113538794" style="zoom:50%;" />

Caching..

### Use Fisher Score to capture Latent $z$

![image-20220604114441281](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604114441281.png)

![image-20220604114432173](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604114432173.png)

After training, you can use ***grad log probability score***

Just forward and backward pass. The result of backward pass that the gradient vector is your feature vector now.