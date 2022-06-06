# Lambda parameter

Larger lambda, 

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220602105338583.png" alt="image-20220602105338583" style="zoom:25%;" />



The larger devalued lambda is the more

we try to push the margin boundaries apart,

the smaller it is, the more emphasis

we put on minimizing the average laws on the training example.



As I increase their value of lambda further,

I start allowing some of the margin boundaries

to let the examples within the actual margin boundaries.

Allow some mistacks

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220602105605883.png" alt="image-20220602105605883" style="zoom:25%;" />

Distance of a point to the line

![image-20220602105941273](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220602105941273.png)

### Regularization and Generalization

![image-20220602110915461](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220602110915461.png)



![image-20220602111036361](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220602111036361.png)

### Quadratic program - SVM

![image-20220602193952396](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220602193952396.png)

What we get here is now a quadratic program

that there are packages for trying to solve.

And you can also generalize this to allowing these constraints

to be violated and incorporating the actual loss value.

It would be a slightly modified version

of the quadratic programming problem.







### Perceptron Algo

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220602202727357.png" alt="image-20220602202727357" style="zoom: 33%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220602202716165.png" alt="image-20220602202716165" style="zoom:50%;" />





<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603100504224.png" alt="image-20220603100504224" style="zoom:40%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603100516271.png" alt="image-20220603100516271" style="zoom:33%;" />

# Perceptron Algorithm 

![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/1*uzm-62Wq3J1JF1HwTMY4mg.png)

### Single Step Update

$$
if\ y*(x*\theta+\theta_0) <= 0 \\

\theta = \theta+ y *x \\ 
\theta_0 = \theta_0 + y
$$

### Average Perceptron Algo

![image-20220603153214612](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603153214612.png)

### Pegasos Algorithm

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603154426701.png" alt="image-20220603154426701" style="zoom:33%;" />