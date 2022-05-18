### Orthogonality

when their product is zero.
$$
v^T w=0\ \text{ and }\ ||v||^2+ ||w||^2 = ||v+w||^2
$$
The right side is $(v+w)^T(v+w)$.





# Lecture 14: Orthogonal vectors and subspaces

Orthogonal = perpendicular

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504205912035.png" alt="image-20220504205912035" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504210123284.png" alt="image-20220504210123284" style="zoom:50%;" />



Row Space is orthogonal to NullSpace



![image-20220504215640112](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504215640112.png)

What about measurement error in $b$.
$$
A^TA
$$
$n\times n$, symmetric

A good equation will be:
$$
A^TAx=A^Tb
$$
<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504220331104.png" alt="image-20220504220331104" style="zoom:50%;" />

No way we can solve three equations with two unknown variables.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504220630812.png" alt="image-20220504220630812" style="zoom:50%;" />

$A^TA$ is invertible only when A has independent columns.



### Lecture 15: Projections onto subspaces

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510101001733.png" alt="image-20220510101001733" style="zoom:50%;" />

Project Matrix:



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510100938048.png" alt="image-20220510100938048" style="zoom:50%;" />

$P\in R^{m\times m}$, but Rank(P) = 1, Sysmetric
$$
P = P^2
$$
Now $N-D$

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510101701026.png" alt="image-20220510101701026" style="zoom:50%;" />

Key : $e = b-A\hat x$ is perpendicular to the plane

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510102522926.png" alt="image-20220510102522926" style="zoom:50%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510102912125.png" alt="image-20220510102912125" style="zoom:50%;" />

![image-20220510103146409](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510103146409.png)

A is not a square matrix, doesn’t have inverse.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510104330994.png" alt="image-20220510104330994" style="zoom:50%;" />



Three equations, two unknown, no solutions. Why?

But then $A^TA$ can turn problem solvable.



### 16. Projection Matrices and Least Squares

![image-20220510104713227](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510104713227.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510105015507.png" alt="image-20220510105015507" style="zoom:50%;" />



How to find the straight line go through 1, 2, 3 that has **Least Square**.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510105233336.png" alt="image-20220510105233336" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510105511565.png" alt="image-20220510105511565" style="zoom:50%;" />

![image-20220510110925003](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510110925003.png)

This is based on calculus.

So now we have a very important equation, called normal equation

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510110113580.png" alt="image-20220510110113580" style="zoom:50%;" />

Tack on b as an extra column. Linear Algebra gives us functions two.

Take partial derivative of calculus, then we will also get below:

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220510110250217.png" alt="image-20220510110250217" style="zoom:50%;" />



### 17. Orthogonal Matrices and Gram-Schmidt

Perpendicular Vectors is definitely independent - Orthonormal

Orthogonal matrix $Q$

$Q^TQ=I, Q^T = Q^{-1}$ if $Q$ is Square

![image-20220511230809385](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220511230809385.png)

What is the good to have a $Q$?

$Q$ has orthonormal columns project onto its own column space.

![image-20220512083833351](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512083833351.png)

### **Gram-Schmidt**

How to make the matrix orthonormal?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512084807150.png" alt="image-20220512084807150" style="zoom:30%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512084738243.png" alt="image-20220512084738243" style="zoom:30%;" />

Now only $A$ and $B$, how to add $C$?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512085049952.png" alt="image-20220512085049952" style="zoom:50%;" />
$$
A=LU, A=QR
$$




