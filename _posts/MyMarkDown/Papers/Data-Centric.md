### Data Boosting Technique

improve the dataset and change the training and validation data splits.

**Before getting into the crux of my solution,**

To evaluate a given dataset, we generate a spreadsheet with logged metrics about each image.



This spreadsheet contains given label, predicted label (logit), and loss for each image..

Which are very useful to isolate inaccuracies and edge cases. 

![img](https://miro.medium.com/max/737/1*9T8YG0PZWG-29ouuVeyIpg.jpeg)

Can also be used for identify incorrectly labeled and image that are not roman numerals.



**Now, on to the Data Boosting**

1. Generate a vary large set of randomly augmented images from the training data.

   ![image-20220317103458048](https://chqwer2.github.io/img/Typora/image-20220317103458048.png)

![img](https://miro.medium.com/max/737/1*1QPDr6yH0nW73FH3FOYuPQ.jpeg)

I generated~1M randomly augmented images from the training set as candidates to source from.



One visualization meth is to used [UMAP](https://umap-learn.readthedocs.io/en/latest/) in 2D

![img](https://miro.medium.com/max/737/1*gV6bNOrDKgig3Ub2tV08_Q.jpeg)