### Use TPUs:

Kaggle offers 20 hours of TPUs every week. TPUs have 8 cores, which  allow your batch_sizes to be scaled by a factor of 8. This allows for  much faster training and faster iteration. 

Note: I have recently discovered Hugging Face Accelerate which claims to give you easy workflow on TPUs with PyTorch too





### Progressive Resizing:

This idea IIRC was introduced in the Efficientnet papers and also taught in the fastai courses. 

Chris Deotte has a fantastic [post](https://www.kaggle.com/c/siim-isic-melanoma-classification/discussion/160147) talking about CNN Input image sizes. [This](https://medium.com/analytics-vidhya/novel-techniques-to-win-an-image-classification-hackathon-part-2-e33bf0ad5fe6) blog teaches you how progressive resizing works in fastai. TL;DR:

- Train model on size: small
- Save weights and re-train model on larger image size
- Save weights again and re-train on final image sizes

This process allows much faster convergence and better performance 



### Experiment: Depthwise Convs instead of Regular Convs:

I believe this [concept](https://paperswithcode.com/method/depthwise-convolution) was introduced in the MobileNet paper first and I saw it resurface in a recent discussion related to ConvNext architectures. Depthwise  Convolutions have fewer filters and hence train faster. 

[See here](https://discuss.pytorch.org/t/how-to-modify-a-conv2d-to-depthwise-separable-convolution/15843/4) for some tips on making it work in PyTorch



### Fastai LR Scheduler

There are many schedulers that allow this: I would recommend using `fastai` and its `fine_tune()` or `fit_one_cycle()` function. See [here](https://forums.fast.ai/t/fine-tune-vs-fit-one-cycle/66029) for more details. 

From the paper, ["Bag of Tricks"](https://arxiv.org/pdf/1812.01187.pdf), one of the ticks highlights using LR warmup:



### DA

Chris Deotte in his recent [CTDS interview](https://www.youtube.com/watch?v=XXmujwhjyIo) shared some secrets. Qishen Ha, whose team had won the TF GBR competition also shared [some tips](https://www.youtube.com/watch?v=8e-EIilkvL0) of making these work

Also, visualise results as you train models to make sure they're learning about the whales and not backgrounds!



### Timm or Tfimm:

[Timm](https://github.com/rwightman/pytorch-image-models) and [Tfimm](https://github.com/martinsbruveris/tensorflow-image-models), the latter being a TF-port of the former is a fantastic resource! 



### Use NGC Containers for Local training:

I understand many people are using Kaggle kernels and Colab for training. However, if you've invested in local hardware, [Ross](https://twitter.com/wightmanr) had taught in a thread on Twitter that the [NGC Containers](https://catalog.ngc.nvidia.com) for PyTorch are very optimised and offer speedups



### TTA, Transform



### Sequential Unfreezing while Transfer Learning:

I learned this trick during the fastai course. When we are performing transfer learning, our model has already captured a lot of information. 

The initial layers (Layers close to inputs) retain more info about  the structure of objects, etc and the latter layers (close to output)  learn more about the dataset. We can envision our model to be grouped in layers like so:

```
Input(Group) -> HiddenSetEarly -> HiddenSetLater -> Output(Group)
```

When performing transfer learning, its usually a good idea to just  train the last few layers and then unfreeze the earlier layers **sequentially**



### Differential Learning Rates:

Continuing with the previous point, another trick I learned via fastai:

The initial few layers need little to no re-training, so applying  differential learning rates to a different group of CNN layers is a  great idea:

Ex: 
 Output(Group): Lr = 10e-3
 HiddenSetLater: LR = 0.5 * 10e-4
 Input(Group): Lr = 10e-5

This would make minimal changes to the initial layers and more  changes to the head (output) layers making our model converge a bit  faster



### PyTorch: use LazyLayers

Note: I learned this trick thanks to Datasaurus, please see his post [here](https://www.kaggle.com/c/petfinder-pawpularity-score/discussion/279460) 

TL;DR when you perform transfer learning using a backbone, you have  to re-write the last few layers with the dimensions in mind. For lazy  folks like me, PyTorch has a LazyLayer (pun intended) to make it easier:

```
self.fc = nn.LazyLinear(self.cfg.target_size)
```

Note: This would otherwise be `self.fc = nn.Linear(self.n_features, self.cfg.target_size)`

Once again, thanks Datasaurus for sharing this in his original post



### Label Smoothing:

We have seen a lot of discussions in this competition about the funny images that exist in the dataset. This is not uncommon, ImageNet and  many datasets themselves have many "mislabeled" images. The trick to  helping here is using Label Smoothing. 

[This](https://paperswithcode.com/method/label-smoothing) is a good writeup about how it works. TL;DR: Adding noise to all labels helps our model generalize better



### PsuedoLabelling:

PsuedoLabelling involves a form of semi-supervised learning. Chris Deotte teaches this in his fantastic kernel [here](https://www.kaggle.com/cdeotte/pseudo-labeling-qda-0-969)

If you want to utilise more labels in training: You grab the most  confident predictions from your model and then add them to your training dataset and build a new model. 



### Use SSDs for image datasets

Again, I respectfully understand many kagglers use cloud hardware and don't have to worry about this step. However, if you've invested in  local setups, I was for a long time not worrying about where I store my  datasets. This would especially create IO bottlenecks for image datasets. 

Always, consider storing your datasets on an M.2 Drive or SSD when  you are reading them into a model so that you don't see a bottleneck. 



