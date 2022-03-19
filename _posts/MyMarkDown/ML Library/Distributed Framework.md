

# Distributed Framework

## 1. 分布式训练策略

1. 模型并行：用于模型过大的情况，需要把模型的不同层放在不同节点orGPU上，计算效率不高，不常用。
2. 数据并行：把数据分成多份，每份数据单独进行前向计算和梯度更新，效率高，较常用。

## 2. 分布式并行模式

1. 同步训练：所有进程前向完成后统一计算梯度，统一反向更新。
2. 异步训练：每个进程计算自己的梯度，并拷贝主节点的参数进行更新，容易造成错乱，陷入次优解。

## 3. 分布式训练架构

1. Parameter Server：集群中有一个parameter server和多个worker，server需要等待所有节点计算完毕统一计算梯度，在server上更新参数，之后把新的参数广播给worker。
2. Ring AllReduce：只有worker，所有worker形成一个闭环，接受上家的梯度，再把累加好的梯度传给下家，最终计算完成后更新整个环上worker的梯度（这样所有worker上的梯度就相等了），然后求梯度反向传播。比PS架构要高效。

## 4. Tensorflow分布式框架

1. [Horovod](https://link.zhihu.com/?target=https%3A//github.com/horovod/horovod)
2. TF>=1.11中官方提供了AllReduce策略，支持Estimator API：[CollectiveAllReduceStrategy](https://link.zhihu.com/?target=https%3A//github.com/logicalclocks/hops-examples/tree/master/tensorflow/notebooks/Distributed_Training/collective_allreduce_strategy)

## 5. Pytorch分布式框架

1. torch.nn.DataParallel：数据并行，PS架构，不建议
2. torch.distributed.DistributedDataParallel：数据并行，优于DataParallel，好像仍是PS架构，建议
3. [NVIDIA/apex](https://link.zhihu.com/?target=https%3A//github.com/nvidia/apex)：封装了DistributedDataParallel，AllReduce架构，建议

