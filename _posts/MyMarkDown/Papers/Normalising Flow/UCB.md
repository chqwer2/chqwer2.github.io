![image-20220504142937117](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504142937117.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504141612296.png" alt="image-20220504141612296" style="zoom:50%;" />

Jacobian Matrix

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504141812259.png" alt="image-20220504141812259" style="zoom:25%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504142135109.png" alt="image-20220504142135109" style="zoom:50%;" />



Normally ensure the Jacobian Matrix is Triangular: save computation

the determine is just the diagonal

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504142224417.png" alt="image-20220504142224417" style="zoom:25%;" />

![image-20220504142603024](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504142603024.png)



m could be neural network

![image-20220504142841853](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504142841853.png)











# CS294-158-SP20 Deep Unsupervised Learning

### L3 Flow Models

![image-20220504130709115](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504130709115.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504131140770.png" alt="image-20220504131140770" style="zoom: 33%;" />





##### Mixtures of Gaussian

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504132049792.png" alt="image-20220504132049792" style="zoom:50%;" />

![image-20220504132614540](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504132614540.png)

Derivative in the loss could be blown off? How to solve it?



what distribution should be picked for $z$?

Gaussian, Beta(5,5), Uniform

What architecture should pick for $f_\theta(\cdot)$, is it invertible and differentiable?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504132954852.png" alt="image-20220504132954852" style="zoom:50%;" />

![image-20220504134159490](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504134159490.png)

Sigmoid and Tanh works.



![image-20220504134732408](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504134732408.png)

### N-D Flows

![image-20220504135947932](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504135947932.png)





![image-20220504140235707](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504140235707.png)

Sampling is pretty slow..

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504140704338.png" alt="image-20220504140704338" style="zoom:50%;" />

![image-20220504141444384](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504141444384.png)