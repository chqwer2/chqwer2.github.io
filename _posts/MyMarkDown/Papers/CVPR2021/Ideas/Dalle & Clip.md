### GPT-3

GPT-3 showed that language can be used to instruct a large neural network to perform a variety of text generation tasks. [Image GPT](https://openai.com/blog/image-gpt) showed that the same type of neural network can also be used to  generate images with high fidelity. We extend these findings to show  that manipulating visual concepts through language is now within reach.



### Clip

400M which text goes to which image that Nature Language is used to reference visual concepts

enabling zero-shot transfer of the model to downstream tasks.

Natural language is used to describe the learned visual concept enabling zero-shot learning in the downstreaming tasks

![image-20211112095953007](https://chqwer2.github.io/img/Typora/image-20211112095953007.png)

#### NL Supervision

Learn visual concept from language pairs

n-gram representations

![image-20211112103125612](https://chqwer2.github.io/img/Typora/image-20211112103125612.png)

Query

<img src="https://chqwer2.github.io/img/Typora/image-20211112104951347.png" alt="image-20211112104951347" style="zoom:50%;" />

Contrastive representation learning

Decoupled Weight Decay Regularization







### Dall.E

Like GPT-3, DALL·E is a transformer language model.

![image-20211116102001910](https://chqwer2.github.io/img/Typora/image-20211116102001910.png)

### Stage 1 

a discrete variational autoencoder (dVAE) to compress 256x256 RGB image into a 32x32 grid of image tokens.

Each element of which can assume 8192 possible values.

### Stage 2

We concatenate up to 256 BPE-encoded text
tokens with the 32 X 32 = 1024 image tokens, and train an autoregressive transformer to model the joint distribution over the text and image tokens.

### How it works?

The whole procedure can be seen as maximize the Evidence Lower Bound (ELB)

![image-20211116134025638](https://chqwer2.github.io/img/Typora/image-20211116134025638.png)

