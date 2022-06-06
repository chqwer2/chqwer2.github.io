A specification can be formulated as if the precondition holds, then the postcondition
holds".



Invariant: If the user gives truthful answers, the secret number s is in the range

Postcondition: If the user gives truthful answers, the printed guess is correct



First convert the given array into a heap tree using heapify, i.e. load the array items in
order into a binary tree (left to right in each level from top to bottom) and bubble down each
non-leaf item starting from the bottom:





### quicksort

![image-20220521204708133](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521204708133.png)



### Hash

Taking just **one letter as the basis of the hash function** means that words with the same first
letter will be mapped to the same position, and since the letters in words are far from equally
distributed, that will result in many collisions and a clustered table. This will be made worse
because several consecutive positions correspond to two letters, and the rest only to one.

![image-20220521205121137](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521205121137.png)



What size hash table would you suggest?
About two or three times the number of entries would be appropriate, i.e. 10 to 15 million



**The performance of the hash table has degraded. Why might this have happened?**
Since markers need to be left after an entry is deleted, it can become very costly to search for
keys after a number of deletions. In this case, the rate of deletions will be similar to the
number of transactions, and there could be as many deletion markers as real entries in the
table, and that will have a large negative effect on the performance when searching for
entries. In the worst case, the whole table may have to be checked to find if an entry exists.
This is particularly likely if the table was set up to be smaller than is optimal now because the
number of entries was much smaller then.

Solution: Copy to a new Table. The current build up of deletions would be removed, and the size of
the table could be increased. So, it would probably be a very sensible thing to do.



### depth-first traversal of the graph

Start with the initial vertex 1 in a stack. Then repeatedly remove the first vertex in the stack
and add it to the list of vertices visited if it is not already in it, replacing it in the stack by the
set of vertices connected to it. There is no need to add vertices to the stack that have already
been visited. This gives the series of stages:

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521211309693.png" alt="image-20220521211309693" style="zoom:25%;" />

![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/ezgif.com-gif-maker61.gif)

这种算法不会根据图的结构等信息调整执行策略

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220522103455587.png" alt="image-20220522103455587" style="zoom:20%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220522103950263.png" alt="image-20220522103950263" style="zoom:25%;" />

DFS can be applied to a wide number of  applications. Here are a few examples with a short description. This is  an excellent opportunity for mindset growth if you think about how DFS  might be used to solve these problems. The problems marked with an  asterisk  are more difficult than the others.

- DFS can be used to detect if a graph is connected; moreover, if the  graph is connected, then DFS can find if there exists a path from one  vertex to another.
- DFS can be used for cycle detection. Mixed with the first  application, it can be used to detect whether or not the graph is a  tree.
- DFS can be used to obtain a **spanning tree** of the  graph. As discussed earlier, a tree can be thought of as a graph with  the minimal number of edges without disconnecting the graph. A spanning  tree is a subgraph of the original graph for which all vertices are  connected with the smallest number of edges.
- DFS can be used to detect if a graph is **bipartite**. A graph is bipartite if we can partition the vertices into two sets where there are no edges between vertices in the same set. This is equivalent to finding if the graph contains an odd cycle.
- DFS can be used to simulate decisions for an artificial intelligence (AI), particularly in games with structure. For example, you can have  an AI simulate what will happen if it makes a move in Checkers or Chess, and cap it off once it gets to a certain depth. Usually, the algorithm  will be a more involved variation of DFS because we'd want our search to be motivated by heuristics or cost/performance functions to help our AI make its choices.
- DFS can be used to do topological sorting on **directed acyclic graphs (DAGs)**. In a DAG, the entire graph can be thought of as oriented based on the  orientations of the edges (for theory students, you can think of this as a **poset**). DFS can be used to obtain from the graph an ordering of the vertices in sorted order based on the edge orientations.
- DFS can be used to obtain a meta-graph of strongly connected  components in a digraph. In a digraph, it is not generally the case that a weakly-connected graph will be strongly-connected. However, we can  find clusters of components in the graph that are strongly connected.  Treating each of these strongly-connected components as a single vertex  of a new meta-graph, we obtain a new graph all together.



### Breath-first

epeatedly remove the first vertex in the queue
and add it to the list of vertices visited if it is not already in it, and add the set of vertices
connected to it to **the end of the queue**.

The **complexity** of both forms of traversal is O(v2) because every entry in the v × v adjacency
matrix must be checked, regardless of whether a link exists.

How do those computational complexities change if the graph is instead represented as an
**adjacency linked list**?
In this case, the complexity of both forms of traversal will be O(v + e) because there are v
linked lists and e links to follow.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521213131668.png" alt="image-20220521213131668" style="zoom:50%;" />

One-edge away vertices, then two-edge away

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220522104131475.png" alt="image-20220522104131475" style="zoom:33%;" />



## **BFS v. DFS: Which is better?**

We've now covered both general search  strategies for graphs, DFS and BFS. From a time complexity perspective,  both algorithms are equivalent in the worst case with both  achieving linear, 

, efficiency (assuming HashSets are efficient). Some wonder which  traversal is better? Being at module 13 in the course sequence, it will  be no surprise to you that the answer is "It depends on context!" Let's  discuss some concerns that may factor into the decision when to use DFS  or BFS. Here are four questions to ask yourself:

1. Begin with an easy question. Do we have any prior knowledge of  what vertex that is being searched for and its location in the graph  relative to the starting point? If it is known that the vertex is  relatively close by compared to the size of the graph, then we may  prefer to use BFS.
2. How "deep" is the graph? For example, if we are doing a traversal of a tree from some root node and the depth of the tree is large, then we  may want to use BFS to avoid staying on a single path for a long time.  Or we could impose some sort of depth limit on DFS traversal if the  graph is infinitely large.
3. How "wide" is the graph / how large is the branch factor? If each  node has many neighbors, then a BFS will quickly blow up in space usage  since we need to store all of these neighbors in a queue. This is  particularly important in areas like AI where the graph we're  considering is essentially infinitely large because our agent's decision space is very large.
4. Do we have any heuristics or any information about the structure of  the graph we can take advantage of? The heuristics we have, may tell us  where to search, in which case we may switch between the two strategies  depending on the graph's structure.
5. 









### Pivot is set the median.







### Time complexity 

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220522114438052.png" alt="image-20220522114438052" style="zoom:33%;" />

### Spanning tree

is a subgraph that is a tree which includes all of the vertices of *G*.



### Sort

(a) What is the worst-case asymptotic running time of heap-sort?
(b) What is the worst-case asymptotic running time of merge-sort?
(c) What is the worst-case asymptotic running time of quick-sort?

(a) O(n log n)
(b) O(n log n)
(c) O(n2)

### Successor

A Successor Graph is **a directed graph in which each vertex has outdegree one**,



### Insertion

![image-20220524112919918](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220524112919918.png)

### Same sorting

![image-20220524113152848](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220524113152848.png)

### Natural Join

Match all the column	..	

### SQL to relational algebra

**Sample 1**

![image-20220524155922333](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220524155922333.png)

**Sample 2**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220524160210436.png" alt="image-20220524160210436" style="zoom: 33%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220524160223265.png" alt="image-20220524160223265" style="zoom:33%;" />

![image-20220524160156374](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220524160156374.png)

### Out Join

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220524161538705.png" alt="image-20220524161538705" style="zoom: 50%;" />

remove de 时候考虑closure



### ER Diagram

