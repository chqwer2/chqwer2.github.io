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





