

# Apex Mixed Precision Training

Apex + Optuna

https://zhuanlan.zhihu.com/p/84219777

![preview](https://pic1.zhimg.com/v2-3f3cf64ec7c1777343fd74a3db9efa70_r.jpg)

![preview](https://pic4.zhimg.com/v2-bef81be5ed6dc2766f1c757f70f3f70b_r.jpg)

显存占用一直在增加 (Gradually)，跑了几个超参之后就报OOM的错误了

1. 加入torch.cuda.empty_cache()，仍然出现以上的问题

**小batch场景下混合精度并不能带来速度提升，甚至会更慢。因为小batch下的计算已经很快了，速度瓶颈在IO（在GPU和GPU间传送数据）。而混合精度需要进行FP16与FP32的转换，会消耗更多时间。**

![img](https://pic3.zhimg.com/80/v2-3b81fa8af962c682b9c55ee48014af0e_720w.jpg)

Why混合精度加速

FP16 : 半精度减少显存占用，加快推断

溢出错误和舍入误差

动态范围太小会发现上下溢出： Nan





/Z{}_pred_target.npy



### 为每个权重保留一份FP32的副本



#### Prob1: apex memory leak problem

opt_level选择半精度或者混合精度之后，optimizers中的参数再训练结束后不会被正确释放，造成了内存泄露

##### Answer: 

放弃nvidia, 直接使用pytorch1.6以上原生支持的apex

https://github.com/NVIDIA/apex/issues/439#issuecomment-522360104
I believe the increase in memory might not be related to amp, but is probably caused by storing the internal parameters of the optimizers

If you leave the default settings as use_amp = False, clean_opt = False, you will see a constant memory usage during the training and an increase after switching to the next optimizer.
Setting clean_opt=True will delete the optimizers and thus clean the additional memory.
However, this cleanup doesn’t seem to work properly using amp at the moment.
![image-20211015090955329](https://chqwer2.github.io/img/Typora/image-20211015090955329.png)

![image-20211015091127262](https://chqwer2.github.io/img/Typora/image-20211015091127262.png)















