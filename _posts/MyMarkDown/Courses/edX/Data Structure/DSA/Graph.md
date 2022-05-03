### Graph

A graph is formed of a (finite) set of vertices/nodes and a set of edges between them. We distinguish four types of graphs:

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328134912995.png" alt="image-20220328134912995" style="zoom:37%;" />



**Element:** Nodes, Weights, Edges and Directions

**Undirected** - can be bidirectionally equal

### How to Implement it in Computer

**Adjacent Matrix** $G \in N^2$   

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328142756252.png" alt="image-20220328142756252" style="zoom:50%;" />

Reading Complexity: $O(1)$

Space Complexity: $O(n^2)$

Traversing Neighbor: $O(n)$

**Adjacent List**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328143308142.png" alt="image-20220328143308142" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328143419870.png" alt="image-20220328143419870" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328143539707.png" alt="image-20220328143539707" style="zoom:50%;" />

How to store it in Data?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328143712994.png" alt="image-20220328143712994" style="zoom:40%;" />

Reading complexity: $O(m)$ in the worst

Space Complexity: $O(n\times m)$, m is the number of edges

Traversing Neighbor: $O(m)$

 

### Paths

Path Graph

**Dijkstra’s algo**: compute the shortest path from $v$ to every other nods

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328145405540.png" alt="image-20220328145405540" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328151933714.png" alt="image-20220328151933714" style="zoom:50%;" />



The time complexity is $O(n^2)$ with matrix: Update every neighbor of it (take $n$ steps).

The time complexity is $O(m)$ with list.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328152836511.png" alt="image-20220328152836511" style="zoom:50%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328152713579.png" alt="image-20220328152713579" style="zoom:40%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328152908618.png" alt="image-20220328152908618" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328153004157.png" alt="image-20220328153004157" style="zoom:50%;" />





### Spanning Tree

Assumption: Consider only undirected and connected graphs!

**Connected**: if you can reach any node from any node.

**Spanning tree** is a minimal possible selection of edges which connects all vertices.

**Minimum spanning tree** is a spanning tree such that the sum of weights of its edges is the minimal such.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328153510094.png" alt="image-20220328153510094" style="zoom:50%;" />

**Jarnik-Prim Algo** for finding the Minimum spanning tree.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328153629678.png" alt="image-20220328153629678" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328153813666.png" alt="image-20220328153813666" style="zoom:50%;" />



Jarn ́ık-Prim’s algorithm works similarly to Dijkstra’s algorithm. **The differences are marked by red.** And the weight can be negative.

The time complexity is the same as for Dijkstra’s algorithm!

[Self-study, part 1 (The algorithm in pseudocode (Links to an external site.)](https://bham.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=bfad9752-d311-4f89-8af4-ad1401294991) with adjacency matrix) (12m:53s)

[Self study, part 2 (The algorithm in pseudocode (Links to an external site.)](https://bham.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=75dc8cd5-41d7-461e-8ba2-ad1401295fe9) with adjacency lists) (7m:51s)





<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328162642723.png" alt="image-20220328162642723" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328162651061.png" alt="image-20220328162651061" style="zoom:50%;" />

![image-20220328163454214](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328163454214.png)