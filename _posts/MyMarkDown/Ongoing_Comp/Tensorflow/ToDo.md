# Tensorflow ToDo

- [x] Get to know the Data

  80% without labels

- [ ] Benchmark

- [ ] Yolov5s6

  - [x] Change SGD to Adamw

- [ ] Metric and Loss…

- [ ] Data-Centric??

- [x] mixup=0.5

- [ ] shear: 0.0  # image shear (+/- deg)

- [x] Flipud: 0.5

- [ ] Large Resolutions 3000

- [ ] Increase Recall: https://github.com/ultralytics/yolov5/issues/2449

- [ ] Auto Hyperparameters: https://github.com/ultralytics/yolov5/issues/607

  - [ ] hyp.finetune

- [x] yolov5m6.pt…

- [x] Address fitness:

  def fitness(x):
     w = [0.0, 0.0, 0.0, 0.0, 1.0]

     weights for [P, R, mAP@0.5, mAP@0.5:0.95]

     return (x[:, :4] * w).sum(1)

  ![image-20220119175541082](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220119175541082.png)

- [x] 

- [ ] Loss

  - [ ] 





#### Change of the Codes 

- [x] Shuffle = False…

![image-20220121105329821](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220121105329821.png)

- [x] Metric Fitness

```
def fitness(x):
    # Model fitness as a weighted combination of metrics
    w = [0.0, 0.3, 0.0, 0.7]  # weights for [P, R, mAP@0.5, mAP@0.5:0.95]
    return (x[:, :4] * w).sum(1)
```

- [ ] Metric F2

```
f2 = 5 * p * r / (4*p + r + eps)
```

- [ ] 
