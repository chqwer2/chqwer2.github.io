# MIT 18.06         

### Prof. Gilbert Strang         



#### Coefficient Matrix

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501102015194.png" alt="image-20220501102015194" style="zoom: 10%;" />

**How to see Column Picture?**

That’s a linear combination of columns.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501102510338.png" alt="image-20220501102510338" style="zoom:25%;" />

See them as a Vector: That ‘s the **Column Picture**

What is the right X and Y to produce the [0, 3] result

![image-20220501103151512](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501103151512.png)



But what are all the combinations?

TODO

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501105205630.png" alt="image-20220501105205630" style="zoom:50%;" />

We only can resolve this matrix when they lie in different planes.

 <img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501110053578.png" alt="image-20220501110053578" style="zoom:50%;" />



### Lecture 2 Elimination with Matrices

Elimination Matrices: $E's$

Augmented Matrix: The $b$ extra column.

Eliminated the matrix to a triangular one: easy to solve

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501122118432.png" alt="image-20220501122118432" style="zoom:15%;" />





Suppose we want to exchange columns in matrices?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501151519197.png" alt="image-20220501151519197" style="zoom:15%;" />





### Multiplication and inverse matrices

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501160447338.png" alt="image-20220501160447338" style="zoom:20%;" />

Also Left and Right Inverse:

For the square matrices: they are the same.

For rectangular: they are not, because their shapes aren’t allow.

**How about the cases with no inverse?**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501161316090.png" alt="image-20220501161316090" style="zoom:20%;" />

With X != 0

**How to calculate Inverse?**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501162102317.png" alt="image-20220501162102317" style="zoom:25%;" />

Add the augmented matrix, then you can do the same thing to the extra column:

![image-20220501162454654](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220501162454654.png)





### L4

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502161026566.png" alt="image-20220502161026566" style="zoom:25%;" />

The final matrix is called pivot: only has independent columns

Order of $E’s$. $L$ is for left matrix?

![image-20220502161005576](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502161005576.png)

Why do we need the inverse matrix?

Because its order keeps the element in their origins

![image-20220502153216741](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502153216741.png)



When no row exchange: the multipler go directly into $L$. The 10 in the matrix

The complexity of matrix operation on A.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502155323692.png" alt="image-20220502155323692" style="zoom: 25%;" />

What happened to B? Just $n^2$.

### L5 Transposes, permutations, spaces R^n

Subspace has to go through the origin.

#### Permutations $P$

Rearrange the row in the identity matrices.
$$
P^{-1} = P^T
$$

### Transpose $T$

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502162216383.png" alt="image-20220502162216383" style="zoom:50%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502162413011.png" alt="image-20220502162413011" style="zoom:25%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502162614440.png" alt="image-20220502162614440" style="zoom:50%;" />

### $R^n$ Vector Space

All column vectors with $n$ real component.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502163623739.png" alt="image-20220502163623739" style="zoom:50%;" />



Subspace:

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502164224697.png" alt="image-20220502164224697" style="zoom: 25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502164647422.png" alt="image-20220502164647422" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220502164729705.png" alt="image-20220502164729705" style="zoom: 25%;" />

I can do linear combination between two vectors, it will stay in the space.

### Column space and nullspace

Which $B's$ can get the system to be solved?

Pivot columns: not linear related or dependent.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220503111150227.png" alt="image-20220503111150227" style="zoom:25%;" />



**Nullspace of A:** all solutions $x$ to $Ax=0$

Consists of all combinations of special solutions.

### Solving Ax = 0: pivot variables, special solutions

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220503124525716.png" alt="image-20220503124525716" style="zoom:50%;" />



The circle row is the **pivot**.

Free columns: 2,4 

Pivot columns: 1,3

**How to solve the question:** Orderly set free column = 1

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220503131654734.png" alt="image-20220503131654734" style="zoom:25%;" />

Upper triangular form.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220503131830281.png" alt="image-20220503131830281" style="zoom:50%;" />

**How many special solutions?**

One for every free variable.

**Reduce row echelon form**

![image-20220503133232824](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220503133232824.png)