# SETI Breakthrough Listen, 2021

Link https://www.kaggle.com/c/seti-breakthrough-listen/discussion/266385

## Content

DA: Apart from random vertical flip, we also employ mixup.

4xTTA (regular, hflip, vflip, hflip+vflip).



## Training

eca_nfnet_l2 backbone and trainable GeM pooling

we feed the full image with only concatenated **ON channels in** and do not do any resizing.

resolution wise we saw on CV that the bigger the better.

To further “enlarge” the images we **change the model stride of the first conv layer to (1,2)**, which is a common trick used in computer vision competitions to basically **further enlarge image resolution**. That allows the model to train on a higher resolution through the  backbone. Christof and Philipp used the same trick in ALASKA2  Steganalysis competition, motivated by the very similar data setup (**find hidden data in an image**). 

Training time of this “high resolution” model is about 15h on 8xV100 **using DDP**.

model for 20 epochs

We randomly mix two images with drawing from the beta distribution  with **alpha=beta=5**, so mostly equal blend. — We always take the maximum  of both labels as the final label should always be target=1 as soon as  there is some form of a signal in the data. 

What we also found helpful, is to **re-normalize the images after mixing**, to keep the nature of the data intact for inference.



## Trick

#### Magic #1

The old leaky data was still giving us a significant boost

To  reduce the impact of leakage in the training as much as possible, we cast to **float32** and subsequently applied a **channel normalization after loading an image**.

Start **investigating single predictions**, where different models with different LB scores disagree. — better LB models had much higher probabilities for images with an “s-shape” signal. 

Test data contains additional type(s) of signal.

Injected signal generator (code base adjusted from https://github.com/bbrzycki/setigen)

#### Magic #2 cleaning

Haven’t even turned our attention to further advancement like **pseudo tagging** which appeared to hold much promise in this competition.

 **Background** between train and test data is very different (visual inspection), learned the test set (whole 1??)

Focus more on background — reduce the impact of the background noise or reduce overfitting on the background noise.

significant overlap from one image to another — This means that the model could also potentially **overfit to single backgrounds** if it only sees target=0 or target=1 for that background. 

→ attempt to remove some common background artifacts from the data — It  is far from trivial to utilize this property due to image-wise channel  normalization.

One cannot just compare raw values from one image to another.

we normalized per column and calculated the mean pixel difference of the  first column of each image to all other images and columns.

We utilized the overlaps to increase **signal to noise ratio**, by replacing the original data with the difference of the normed regions between multiple matched samples.

This induces shadowing (difference is much smaller than 0) from signals that are present in the matched samples, which our models were able to  distinguish from actual signals. In the plot below, the difference of  the normalized overlapping region between two samples is shown. The  yellow needle (values > 0) originates from sample 1, and the blue  needle (values < 0) originates from the matched sample.

#### Other

we also trained models with a kind of self attention based on the OFF-channel activations.

While not yielding better scores on its own, this proved to be valuable when used in blends as it seems to add diversity.

One other thing we noticed is that **pseudo labeling** has a positive impact as it may help with the **train/test domain shift**. We also explored additional techniques and research to tackle domain shift.

#### Comment

Imagine the following simplistic use case:
You have a set of  images with certain backgrounds (white, green, striped, constant, etc.)  and then you have black dots on those images and you want your model to  identify if an image contains a black spot (anomaly). Unfortunately, you have some backgrounds that always exhibit a black spot, or maybe never  exhibit one. If you are unlucky, your model might decide to overfit on  the actual background, instead of trying to identify the raw signal of  the black spot. And here in this competition we observed quite obvious  overfit on the background, and a challenge was to steer the models to  learn the actual patterns.

One thing most people did was to do  mixup, so mixing different backgrounds together and having the signals  in different intensity. One other thing was to utilize pseudo tagging,  that then also better learns to adjust to the new background  (distribution) of the test data. But the best solution is to process the images in a way that they increase the signal to noise ratio, which we  did by cleaning common backgrounds among images. In the example above,  it would be obviously better to completely remove all background, and  just keep the actual signal.

I do personally not see how this is  necessarily only limited to this data and problem. Of course, the data  is synthetic here, so the effects are emphasized, but I have observed  similar effects before, in other problems, competitions, and projects,  but have never so thoroughly thought about it like here. There are many  use cases where this is an imminent issue, such as fault prediction in  machinery, anomaly prediction, steganalysis, or even chest x-ray  prediction where often models prefer to overfit on certain device  characteristics.

Will the same technique applied here work for all problems? Probably not, but the thought process can be the same. So I  would encourage you to see it as a learning, at least that's what I am  doing, and try to approach these issues in the future in different  projects. I can imagine, that clever modeling approaches can also  attempt to deal with these issues directly, for example via attention  like 3rd place used. There is also plenty of research in the area of  domain adaption, where I have seen little being applied on Kaggle, and I have only started to look into it:
https://paperswithcode.com/task/domain-adaptation

### 2nd Place Solution

Link: https://www.kaggle.com/c/seti-breakthrough-listen/discussion/266397

