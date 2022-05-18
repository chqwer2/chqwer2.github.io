# 18. Properties of Determinants

is associated with every square matrix
$$
det\ A = |A|
$$
one number that can tell you what whole matrix is?

Matrix is singular: det = 0, so det would be a test for invertibility

**Property 1**
$$
det\ I = 1
$$
**Property 2**

Exchange rows reverse the sign of the Determinant

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512133330289.png" alt="image-20220512133330289" style="zoom:50%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512133346129.png" alt="image-20220512133346129" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512164917552.png" alt="image-20220512164917552" style="zoom:33%;" />

multi one row by $t$:

**Property 3A**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512133530994.png" alt="image-20220512133530994" style="zoom:25%;" />

**Property 3B**

Only true requests linear for each row
$$
Det\ (A+A') = Det\ A + Det\ A'
$$
<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512133626935.png" alt="image-20220512133626935" style="zoom:25%;" />

If I have a triangular matrix, the triangular is the only thing we should work with

So first elimination, makes it triangular: Product of Pivots

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512163150650.png" alt="image-20220512163150650" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512163413953.png" alt="image-20220512163413953" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512164012895.png" alt="image-20220512164012895" style="zoom:30%;" />



### 19. Determinant Formulas and Cofactors



![image-20220512165207502](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512165207502.png)

The survivers will have one value in each column and row.

**Big Formula**

Will be a sum of fact(n) terms

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512170056662.png" alt="image-20220512170056662" style="zoom:50%;" />





#### Cofactors of $a_{ij}$

Strick out $a_{ij}$

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512171826128.png" alt="image-20220512171826128" style="zoom:50%;" />

Easy calculation

an example of tri-diagonal matrix

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512172758745.png" alt="image-20220512172758745" style="zoom:50%;" />



### Let 20 Determine Application

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514082332349.png" alt="image-20220514082332349" style="zoom:33%;" />

1. **Formula for $A^{-1}$**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513215303499.png" alt="image-20220513215303499" style="zoom:25%;" />

The right side is a matrix of cofactors $C$

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513215448121.png" alt="image-20220513215448121" style="zoom:50%;" />



Why it is true?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514075729406.png" alt="image-20220514075729406" style="zoom:33%;" />



Why $a$ times cofactors from another row equal to 0?

They has row identical to $a$, so the determinant is 0



### Cramer’s Rule

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514082438078.png" alt="image-20220514082438078" style="zoom:50%;" />

But matlab won’t do it, it is nice but slow.



### Volumn

det Q = 1

The box of I and Q is a cube with volumn equal to 1

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514083852221.png" alt="image-20220514083852221" style="zoom:33%;" />

Area equal determinant (parallelogram)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514092348973.png" alt="image-20220514092348973" style="zoom:33%;" />

**Triangle**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514092713312.png" alt="image-20220514092713312" style="zoom:50%;" />



# 22. Diagonalization and Powers of A

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517091620516.png" alt="image-20220517091620516" style="zoom:50%;" />

suppose $n$ indep eigenvectors of $A$

Put them in columns of $S$



![image-20220517092734186](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517092734186.png)
$$
AS = S\Lambda \\
S^{-1}AS = \Lambda\\
A=S\Lambda S^{-1}
$$
S is invertible, because each column is indeed.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517093214656.png" alt="image-20220517093214656" style="zoom:50%;" />

So the below formula tells me the same thing, the eigenvector squared of $A^2$

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517093345430.png" alt="image-20220517093345430" style="zoom:33%;" /> 

It tells us the property of power of matrix

if we handle $A^{n}=(LU)^n$, we could not do any thing

But with the above formula, we get $\Lambda$ to the $n$, it tell you about the power of matrix.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517094035354.png" alt="image-20220517094035354" style="zoom:50%;" />



A is surely have $n$ indep columns (and be diagonalisable) if all $\lambda$‘s are different.

If we have repeated $\lambda$, we may or may not have $n$ indep eigenvectors.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517101830585.png" alt="image-20220517101830585" style="zoom:50%;" />

#### Fibonacci Sequence

![image-20220517103034511](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517103034511.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517102755515.png" alt="image-20220517102755515" style="zoom: 25%;" />



So to calculate it quick, we now have eigenvalue for A: $\frac{1\pm \sqrt(5)}{2}$

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517103915797.png" alt="image-20220517103915797" style="zoom:33%;" />

why we only care about the first term, 

because the second eigenvalue (0.618) to the power is extremely **small**…





