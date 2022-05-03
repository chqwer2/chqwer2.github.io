# Light-weight Net

1. Mediate the spatial Info
   - architecture tunes
   - multi-branch
2. Redundancy in Matrix-vector multiplication
   - conv computation - Efficient Blocks



MobileNet, ShuffleNet, Exception, IGCV3, MixNet, EfficientHRNet



**Lite-HRNet**, CVPR 2021

Task: Pose-estimation, segmentation

Apply the **Shuffle Block** v2 (heavily used pointwise ($1 \times 1$) Conv.) in**HRNet** (high resolution design pattern)

replace costly ($1 \times 1$) Conv with **conditional channel weighting**: Channel and Resolution.

w.r.t ?





Shuffle Block : $1 \times 1$ + $3 \times 3$ DWConv + $1 \times 1$, output concerted with input then shuffle.