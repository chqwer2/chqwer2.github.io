# Differential Equations and exp(At)

Eigenvalue is telling me information of the solution.

But what is the solution?

![image-20220519091044405](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519091044405.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519091117865.png" alt="image-20220519091117865" style="zoom:25%;" />

What is $C_1$ and $C_2$, comes from $u(0)$.



#### Stability

$$
u(t)\to 0
$$

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519091742816.png" alt="image-20220519091742816" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519092203713.png" alt="image-20220519092203713" style="zoom:50%;" />

![image-20220519092945572](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519092945572.png)

![image-20220519093101070](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519093101070.png)

#### What is exponential of Matrix means?

Taylor series

![image-20220519093308204](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519093308204.png)

Two beautiful Taylor series..

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519093404892.png" alt="image-20220519093404892" style="zoom:15%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519093514373.png" alt="image-20220519093514373" style="zoom:33%;" />

But the first is better because it always converges.

But why 

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519093741643.png" alt="image-20220519093741643" style="zoom:25%;" />

Because, with the assumption that $A$ can be diagonized.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519094014428.png" alt="image-20220519094014428" style="zoom:33%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519094201433.png" alt="image-20220519094201433" style="zoom:25%;" />

How to make 2nd order equation into two 1st order equation?

![image-20220519094755587](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519094755587.png)

The same, 5th order equation can be converted into 5x5 matrices.



### 24 Markov Matrices; Fourier Series

Markov Matrices is connected to probability idea, cannot be negative and column sum up to 1.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220527091540038.png" alt="image-20220527091540038" style="zoom:33%;" />

remember the steady-state is when $\lambda=0$

Linear Algebra tells us:

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220527091720994.png" alt="image-20220527091720994" style="zoom:33%;" />

Only remain $x_1$ part as steady state.

$A-I$ is singular, then $\lambda=1$ is an eigenvalue. (All columns add to zero)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220527092203881.png" alt="image-20220527092203881" style="zoom:33%;" />

because the rows are dependent, (1,1,1) is in the null space of $n(A^T)$ 

eigenvalue of $A$ and $A^T$ is the same

**What is the application of Markov Matrices?**

entries are the property that is always positive (such as the $P$ is how much people move out) 

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220527093720721.png" alt="image-20220527093720721" style="zoom:50%;" />

Solution

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220527094242283.png" alt="image-20220527094242283" style="zoom: 25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220527094436133.png" alt="image-20220527094436133" style="zoom:25%;" />

### Projection

onto with orthonormal basis

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220527095117146.png" alt="image-20220527095117146" style="zoom:40%;" />

But we want to get rid of the $x_2$ and so on.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220527095413402.png" alt="image-20220527095413402" style="zoom:50%;" />

### Fourier Series

Is infinite.

![image-20220527100350550](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220527100350550.png)

How to solve it?

Take both sides multiply $cos\ x$

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220527100426085.png" alt="image-20220527100426085" style="zoom:50%;" />



### 25. Symmetric Matrices and Positive Definiteness

What special about eigen?

For symmetric case, it can be rather simple.

![image-20220603172215519](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603172215519.png) 

Why real eigenvalue?

Conjugate: $\bar X$

![image-20220603172503386](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603172503386.png)



The length of a complex vector: $\bar  X^T X$= length

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603173237495.png" alt="image-20220603173237495" style="zoom:25%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603173414800.png" alt="image-20220603173414800" style="zoom:30%;" />

Means $A = \bar A^T$



![image-20220603173639973](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603173639973.png)

Every Symmetric Matrix is a combination of a mutually perpendicular projection matrix



Finding the eigenvalues of a big matrix (50x50) is hard, but finding pivots is easier.

Maybe 28 pivots are positive, 22 are negative?

Because the sign of pivots is the same as eigenvalues.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603174506373.png" alt="image-20220603174506373" style="zoom:40%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220603181619597.png" alt="image-20220603181619597" style="zoom:50%;" />