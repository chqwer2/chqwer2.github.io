# VAE (Probabilistic Encoder)

observation (x) -> latent (Z) Probabilistic
$$
Encode:\ X \to Z \\
Decode: \ Z \to X
$$


AE cannot work on unseen vacancy in feature space

VAE: Sampling from this model, able to generate new data

![image-20211126132648586](https://chqwer2.github.io/img/Typora/image-20211126132648586.png)



Prior distribution of z : p(z), maybe gaussian



Discriminative models f: Z-> X'

deterministic to variational

AE try to map input to a point

VAE try to in a space (area), predict a distribution 

two z (two neuron per dimension) of the G distribution: mean & sigma vectors       (4 neurons totally)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

![image-20211126133632863](https://chqwer2.github.io/img/Typora/image-20211126133632863.png)





![image-20211126133735767](https://chqwer2.github.io/img/Typora/image-20211126133735767.png)

### How to train?

Overlaps: how to avoid or **interrupt?**?

-> Learn parameters that predict **small** **standard deviations**.

![image-20211126133847053](https://chqwer2.github.io/img/Typora/image-20211126133847053.png)

Confuse: move the mean away from each other, and reduce the variance

If we would train a VAE only with the Reconstruction loss, its learned parameters would make it behave exactly like the basic deterministic AE!

So, the “probabilistic encoder” architecture is not sufficient! We need the **Regularizer**

![image-20211126134001219](https://chqwer2.github.io/img/Typora/image-20211126134001219.png)



![image-20211126134035773](https://chqwer2.github.io/img/Typora/image-20211126134035773.png)



Sample from the G distribution, **Decoder** try to reconstruct the input

Try to cover the prior p(z)

Strength of Regularizer, chosen from experiments



What if without regularizer? 

needed to solve the overlap
$$
D_{KL} (p(z|x)||N(0，I))
$$

why using prior distribution?

N~(0, *I*)

what is D_KL?



predict posterior distribution < D_KL > prior distribution

means around 0, Std.Dev cover the prior



### Re-parameterization trick

sampling is not differentiable ! No grads!

epsilon is sampled from distribution: now we have grads

To draw from Normal(mu, sigma) you can draw from Normal(1, 0), multiply by sigma (scale), and add mu (translate)

*AE Variational bayes, ICLR 2014*
$$
\mu_\phi(x) + \delta_\phi(x) * \epsilon
$$
![image-20211126134156403](https://chqwer2.github.io/img/Typora/image-20211126134156403.png)

### Gaps of New Data

![image-20211126132736171](https://chqwer2.github.io/img/Typora/image-20211126132736171.png)

![image-20211126132757230](https://chqwer2.github.io/img/Typora/image-20211126132757230.png)

![image-20211126132826956](https://chqwer2.github.io/img/Typora/image-20211126132826956.png)

![image-20211126132934814](https://chqwer2.github.io/img/Typora/image-20211126132934814.png)



### Tutorial

Encoder + Decoder

vectorize them, 

standard deviation, needs **log** to limit the range, must be positive, tend to be small (close to zero)

Log can curry both positive and negative value.
$$
\sigma = exp(log(\sigma))
$$
Sampler:

$mu\ \&\ logstd$  input

The re-parameterization tricks

$Z\to N(\mu, \sigma)$  <=>  $\mu + \sigma * \epsilon$ 

with $\epsilon \to N(0,I)$



Pre-train model, 

code of VAE is worse than initialization

not pure for reconstruction, and regularization



