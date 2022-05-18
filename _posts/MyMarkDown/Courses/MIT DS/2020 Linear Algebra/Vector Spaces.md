# Vector Space

Pivots

**rank** is how much pivots we have.

Free matrix and Indentity Matrix: Let one free variable = 0 at a time to obtain special solution.

**Reduced Row-Echelon Matrix Form**: stair-like  $R$

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

**Reduce row echelon form $R$**





### L8: Solving Ax = b: row reduced form R

Every matrix has full rank ($r=n$) must:

1. All columns of $A$ are pivot columns
2. Not free variables or special solutions
3. null space $N(A)$ only contain $x=0$
4. $Ax=b$ only has one solution



We now have a matrix $R^{n\times m}$ with $m<n$, 

then the equation $Ax=b$ is **underdetermined**. Called **Full Row Rank ($r=m$)**

There exist $n-r=n-m$ special solutions in the nullspace of $A$.

Has $\infin$ solutions



**Full Column Rank ($r=n$)**: only has 0 or 1 solution



### Independence, basis, and dimension

**Independence:** Only one solution to $Ax=0$ is $x=0$.

**Basis:** Not too many or too few.

**Dimension:** The number of vectors on a basis.

**Full column rank:** When independent, the rank is $r=n$. 



Rank(A) = Pivot Columns = Dimension of C(A)

 



### Four Subspaces

The **rank** of a matrix is the number of pivots.

The **dimension** of a subspace is the number of vectors in a basis (They span the space).

Row space $C(A^T)\in R^n$, has dimension $r$

Column space $C(A)\in R^m$, has dimension $r$

Nullspace $N(A)\in R^n$, has dimension $n-r$. The same space of free variables.

Left null space  $N(A^T)\in R^m$, has dimension $m-r$.



![image-20220504155738742](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504155738742.png)

I do row operation, so same row space but different column space

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504160551031.png" alt="image-20220504160551031" style="zoom:50%;" />
$$
EA = R
$$

# Lecture 11: Matrix spaces; rank 1; small world graphs

Symmetric Matrix $S$, Upper Triangular $U$



# Lecture 12: Graphs, networks, incidence matrices

Linear Algebra comes from real application

Tree: Graph with no loop.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220504204932069.png" alt="image-20220504204932069" style="zoom:50%;" />





