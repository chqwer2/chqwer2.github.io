# Dice Loss

##### A Far Better Alternative to Cross Entropy Loss for Boundary Detection Tasks in Computer Vision



### Why not CE? 

the loss is calculated as the average of the pixel-wise distribution w/o knowing the adjacent pixels are boundaries or now.

As a result, cross entropy loss only considers loss in a micro sense rather than considering it globally, which is not enough for image level prediction.

![img](https://miro.medium.com/max/788/1*VMiADFOL7x0R9U32qK-C6Q.png)



### So Dice Loss

$$
D = \frac{2\sum^N_np_ig_i}{\sum^N_ip^2_i+\sum^N_ig^2_i}
$$

p & g represent pairs of corresponding pixel values of prediction & GT

the value are either 0 or 1

![img](https://miro.medium.com/max/788/1*oK8npb1wtF-GKeHi7yIBoQ.png)

![img](https://miro.medium.com/max/788/1*jHLfALexHBtE8ugdCYKtSQ.png)
