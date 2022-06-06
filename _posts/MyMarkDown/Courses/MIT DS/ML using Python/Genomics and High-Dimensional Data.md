# Linear Algebra

![image-20220604174404654](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604174404654.png)

### Empirical Mean

![image-20220604174931026](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604174931026.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604174949268.png" alt="image-20220604174949268" style="zoom:33%;" />

### Covariance Matrix

![image-20220604175240237](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604175240237.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604211405332.png" alt="image-20220604211405332" style="zoom:50%;" />

### Orthogonal Matrix

![image-20220604181438032](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604181438032.png)

![image-20220604181605409](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604181605409.png)

![image-20220604181854775](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604181854775.png)



### PCA

![image-20220604211535039](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604211535039.png)



Goal: Dimensions reduction to a few dimensions.

Find low-dimension projection with large spread.



**Definition 1: Maximize Projection Variance **

**Definition 2: Minimize Projection Residual**

losing as little info as possible

![image-20220604220205930](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604220205930.png)

**Definition 3: Spectral Decomposition**

V is matrix of eigenvectors, A is diagonal matrix of eigenvalues

![image-20220604220512224](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604220512224.png)

You can minimize the signal loss,

or you can just directly compute the eigenvector corresponding

to the largest eigenvalue and the covariance matrix.

This actually always gives you the same.



1. Projection (Image that projection triangle)

   X split into residual and projected vector

2. Unit vector $w$, 

   Length of projection of $x$ onto $w$: $w^T x$

3. Residual:

   $x-(w^Tx)w  $

4. Residual Square is:

   $||x-(w^Tx)w  ||^2 = ||x||^2-(w^Tx)^2$ 

   ![image-20220604234125107](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604234125107.png)

We just have to remember some linear algebra.

So if I'm trying to find the vector

such that the inner product with a covariance matrix

and the product from both sides where the covariance matrix is

maximized, well, the solution to this

is exactly the eigenvector corresponding

to the largest eigenvalue.

### Example

![image-20220604234354706](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604234354706.png)

So this case we don’t want to do PCA on covariance matrix, but on the correlation matrix.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220604234503904.png" alt="image-20220604234503904" style="zoom:40%;" />

**One example of Covariance Matrix**

for example, get rid of noise

so that you only keep things that actually

contain quite a bit of signal.

So what can you do, or what do people then often do

is you have some cut off.

So say you keep as many principal components

that you explain, say, for example, 80% of the variance--

80% of all of the variability in your data.



**One example of Correlation Matrix**

Now, if you're doing it based on correlations,

then there is also another interesting interpretation,

like here where we're doing it based on correlation.

Well, then you could also just keep

all the principal components, or the eigenvalue--

eigenvectors that-- or the directions that

have above average variance.

So how do you see directly what does it mean

to have above average variance?

Well, with a correlation matrix--

so what is interesting there is, of course, your eigenvalues--

if you look at sum of the eigenvalues--

so the sum of the eigenvalues of the lambda i's. Well,

this is, of course, the same as the trace, right?

The trace of your matrix.

### Covariance versus Correlation

![image-20220605162325289](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220605162325289.png)

Sometimes, It is better to first rescale each covariate into a dimensionless quantity before performing dimensional reduction.



### Multidimensional Scaling (MDS)

![image-20220605164911444](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220605164911444.png)

### Classical MDS

![image-20220605165539196](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220605165539196.png)

![image-20220605165722177](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220605165722177.png)

![image-20220605165850644](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220605165850644.png)

![image-20220605170220409](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220605170220409.png)

**Solution to MDS**

![image-20220605215340866](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220605215340866.png)

Center Matrix

Distance Matrix

**Gram matrix B**
$$
B = XX^T
$$


![image-20220605220614494](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220605220614494.png)



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220605220739479.png" alt="image-20220605220739479" style="zoom: 50%;" />

# Stochastic Neighbor Embedding (SNE) 

# and t-distributed SNE (t-SNE)

Plot every point a little Gaussian

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220606083433915.png" alt="image-20220606083433915" style="zoom:40%;" />

**How to Calculate**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220606083830412.png" alt="image-20220606083830412" style="zoom:40%;" />

Then you can merge neighbors

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220606083956157.png" alt="image-20220606083956157" style="zoom:40%;" />

$p_{ij}$ is with $k>l$, $q_{ij}$ is with $k \neq l$

### tSNE

t stand for t-distribution.

Sometimes medium-distance points might actually

just become closeby points.

So we replace gaussian with t-distribution with 1 degree of freedom for y’s

Which has fatter tail



SO we use 1/(1+D^2)

![image-20220606084309808](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220606084309808.png)

Moderate distance.

![image-20220606103616770](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220606103616770.png)



Distance 越大， $p$ 或 $q$ 越小



### 

### Quadratic Discriminant Analysis (QDA) 

### and Linear Discriminant Analysis (LDA)

Based on Bayesian Inference

![image-20220606142052743](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220606142052743.png)

Decision Boundry is Quadratic.

Assumption

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220606142437312.png" alt="image-20220606142437312" style="zoom:33%;" />

If we don’t have that much of data to estimate the variance,

Then we can simplify the model by assuming variance of all classes is the same.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220606142557218.png" alt="image-20220606142557218" style="zoom:33%;" />

But now the variance is a constant, then it becomes linear:

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220606142644359.png" alt="image-20220606142644359" style="zoom:33%;" />

Because the covariance = $\sigma I$, so we will always have a circle to fit the data.

So the new data comes in, we just calculate the distance between it and class centres.

 



And now we would like to know what

is the operation to make it into an identity matrix.

So again, we're going to do always the same trick.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220606143131010.png" alt="image-20220606143131010" style="zoom: 33%;" />

Well, what you want to take is just this operation.

So x goes to x times V items lambda to the minus 1/2.

And if you do it, then you get into the space

where this covariance matrix is nice and round.



So that's the whole idea behind QDA and then--

which is Quadratic Discriminant Analysis,

where you have a general covariance matrix,

no additional restrictions on it, then LDA--

so Linear Discriminant Analysis, where

you make additional restrictions on your covariance matrix--

namely, that they are all the same.



And that can always be solved using even the simpler problem,

where you're just assuming that each one

of the covariance matrices is actually round.



But it is a strong assumption.

We made assumptions on, actually,

the shape of this conditional distribution and, of course,

also the class distributions.