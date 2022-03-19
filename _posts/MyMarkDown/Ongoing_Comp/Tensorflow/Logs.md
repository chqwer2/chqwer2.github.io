**Yolo v5m **1280*8, epoch = 10

Adamw with LR 1e-3

mixup = 0.2, mosaic = 0.2, scale = 0.1, 

conf 0.15@1280 PB = 0.342 ,        1280*2PB 

conf 0.3@0.397

conf 0.4@0.414



**Yolo v5m **1280*8, epoch = 10

Adamw with LR 1e-3

mixup = 0.2, mosaic = 1.0, scale = 0.3, 

![image-20220119223206193](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220119223206193.png)



**Yolo v5m6 **1280*8, epoch = 10

Adamw with LR 1e-3

mixup = 0.2, mosaic = 1.0, scale = 0.5， 

P, R, mAP@.5, mAP@.5:.95

0.908 0.701 0.791 0.414

With Fitness

 0.892   0.748   0.821   0.414



**Yolo v5m6 **1280*8, epoch = 10

Adamw with LR 1e-3

mixup = 0.2, mosaic = 1.0, scale: 0.750  

flipud = 0.25， degrees: 0.00-0.3 

 0.902      0.744      0.826      0.437

PB@conf 0.4 = 0.449, TTA > 0.460

PB@conf 0.5 = 0.430

![image-20220121154713301](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220121154713301.png)

epoch = 15

PB@conf 0.4 = 0.490



Video - Sequence

Shuffle = False

![image-20220122094235336](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220122094235336.png)

PB@conf 0.4 = 0.524



**Yolo v5m6   yolov5-mu5-up5-431 ** 1280*8, epoch = 15

Adamw with LR 1e-3

mixup = 0.5, mosaic = 1.0, scale: 0.750  

flipud = 0.5， degrees: 0.00

Video Yes.



**yolov5-mu25-up5-431 ** 

shear: 2.0 -> 0.0
