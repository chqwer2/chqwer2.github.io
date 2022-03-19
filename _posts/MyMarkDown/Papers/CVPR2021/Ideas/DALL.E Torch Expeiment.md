## Generation

https://colab.research.google.com/drive/11V2xw1eLPfZvzW8UQyTUhqCEU71w6Pr4?usp=sharing

Method:

dalle = DALLE(vae = vae, shift_tokens = False, rotary_emb =False, **dalle_params).cuda()



L380 in attention +

out = self.attn_fn(q.half()， k.half(）)

   

```
pip installed triton-1.0.0.dev20210723
```

!pip install triton==1.1.1



\# install CUDA 11.4.2 ?

!wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin

!sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600

!sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub

!sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /"

!sudo apt-get update

!sudo apt-get -y install cuda



0.4.2 : No module named 'triton.language'

1.0.0 : CUDA: Error- invalid ptx

1.1.1 : RuntimeError: CUDA: Error- invalid image

*FP16 on Pascal GPUs is not supported.*

