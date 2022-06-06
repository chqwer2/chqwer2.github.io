# Eigenvalue

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514092828589.png" alt="image-20220514092828589" style="zoom:30%;" />

Matrices is square,

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514093006245.png" alt="image-20220514093006245" style="zoom:25%;" />

We look for special vectors that for $Ax$ parallel to $x$, the same direction

Eigenvalue: $\lambda$, Eigenvector: $x$

If $A$ is singular, then $\lambda$ is 0

**Projection Matrix**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514093640757.png" alt="image-20220514093640757" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514093800833.png" alt="image-20220514093800833" style="zoom:25%;" />



How to solve $Ax=\lambda x$?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514094359126.png" alt="image-20220514094359126" style="zoom:25%;" />

The determinant of the Singular matrix is 0.
$$
det\ (A-\lambda I)=0
$$
then just find $x$ in the null space.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514095157190.png" alt="image-20220514095157190" style="zoom:33%;" />

When we add $3I$ to the matrix, the eigenvalues add 3 too, but the eigenvectors don’t change.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514095329527.png" alt="image-20220514095329527" style="zoom: 33%;" />

Cautions: they should have the same eigenvector

A **rotation** example, a rotation matrix is also an orthogonal matrix.

But we got in trouble when handling the rotation matrix.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514100154050.png" alt="image-20220514100154050" style="zoom:30%;" />

We don’t have real vectors, but complex vectors.

**Triangular Matrix**

The eigenvalue lies on the diagonal.

![image-20220514102722975](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220514102722975.png)

This example only has one eigenvector.



### Find the eigenvector

![image-20220605161834995](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220605161834995.png)
