### Bayes

https://canvas.bham.ac.uk/courses/56073/quizzes/143097



### Clustering Local Minima

K-means and EM rely on cluster initialisation, and EM also relies on  gradient descent. Therefore, they are non-deterministic algorithms and  may get struck at local optima. 



GMM and K-means may also produce a decision boundary that can produce  such clustering result, but depending on initialization it might  converge to a different set of clusters (left half vs. right half).



### KMeans

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220529154011260.png" alt="image-20220529154011260" style="zoom:33%;" />



### MLP

It is very unlikely that an MLP would do better here, because any subset of the 3
points that it trains on lacks information about the non-linear nature of the problem.
So, despite the fact the MLP has capacity to represent nonlinear boundaries, it will
not be able to guess it from the data it sees at the training stage.







Machine learning aims not only at
performing well on the given training set, but also on unseen examples. Formulating
the optimisation problem in this way could lead to overfitting, which may result in
poor performance on unseen examples. This is an example of key potential weakness
of this problem formulation.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220529164911355.png" alt="image-20220529164911355" style="zoom:33%;" />



### EM

Each iteration of the EM algorithm increases to likelihood of the data, unless you happen to be exactly at a local optimum.



This data is clearly not linearly separable

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220529172049871.png" alt="image-20220529172049871" style="zoom:50%;" />

F= X1+X2

In order to use SVM for classifying this data, introduce another feature Z = X2 + Y2 into the dataset. Thus, projecting the 2-dimensional data into 3-dimensional space. The first dimension representing the feature X, second representing Y and third representing Z (which, mathematically, is equal to the radius of the circle of which the point (x, y) is a part of). Now, clearly, for the data shown above, the yellow data points belong to a circle of smaller radius and the purple data points belong to a circle of larger radius. Thus, the data becomes linearly separable along the Z-axis.

Core Function

### Linear Regression

![image-20220528171107330](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220528171107330.png)

![image-20220528171609000](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220528171609000.png)

![image-20220528173259804](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220528173259804.png)





### NN

Supervised learning is a better way to solve this case, we will be using perceptrons. Uni layered perceptrons can only work with linearly separable data. But in the following diagram drawn in accordance with the truth table of the XOr loical operator, we can see that the data is NOT linearly separable.

To solve this problem, create a Multi Layered Perceptron (or MLP). These extra layer’s are called as the Hidden layer. To build a perceptron, we first need to understand that the XOr gate can be written as a combination of AND gates, NOT gates and OR gates in the following way:



1. 怎么Norm图像，Discussion/322602
2. RASNSAC v2， 324805
3. DKM，321177
4. Descriptor，MAGSAC++， dengensac， GC-RANSAC？
5. QuadTree 调整
6. Config内容





### BFS

https://canvas.bham.ac.uk/courses/56073/quizzes/143213



### A star

https://canvas.bham.ac.uk/courses/56073/quizzes/143397

A* is only complete, optimal and optimally efficient when the heuristic is consistent.



### Design 

https://canvas.bham.ac.uk/courses/56073/quizzes/143245



### TSP

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220529105356329.png" alt="image-20220529105356329" style="zoom:25%;" />



### Annealing

https://canvas.bham.ac.uk/courses/56073/quizzes/143396



### Discussion

https://canvas.bham.ac.uk/courses/56073/quizzes/143477