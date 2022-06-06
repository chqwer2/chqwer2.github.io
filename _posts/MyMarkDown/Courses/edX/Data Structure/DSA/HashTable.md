# Hash Tables

Efficient search way

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512174501587.png" alt="image-20220512174501587" style="zoom:25%;" />

Key can be **String** in Python, but need to converted with hash table in Java

Hash Function: String to Number


$$
hash('bham') = 7
$$
Here 7 is the length of Student ID

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512174704000.png" alt="image-20220512174704000" style="zoom:50%;" />

It requires to 3 operations, but proportion to 1.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512175059228.png" alt="image-20220512175059228" style="zoom: 25%;" />

But memory usage is not efficient

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512210509958.png" alt="image-20220512210509958" style="zoom:30%;" />

### Two types of Collisions



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512211215216.png" alt="image-20220512211215216" style="zoom:30%;" />

1. Have same hash value: stored in linked list
2. Tucked: Linear Probing and secondary hash function



An example

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512211526541.png" alt="image-20220512211526541" style="zoom:33%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512211632835.png" alt="image-20220512211632835" style="zoom:27%;" />

How to find a better hash function?

A Good hash is to assign keys uniformly in probability

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512211920403.png" alt="image-20220512211920403" style="zoom:50%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512212124156.png" alt="image-20220512212124156" style="zoom:50%;" />

in percentage

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512212226302.png" alt="image-20220512212226302" style="zoom:30%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512212247788.png" alt="image-20220512212247788" style="zoom: 33%;" />

Expected: 1/2

So use **Maximal Load Factor** (Only $\lambda$ will be used )

So the time used for search will be faster

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512212320015.png" alt="image-20220512212320015" style="zoom:33%;" />



### Insert

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512212910504.png" alt="image-20220512212910504" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512213035272.png" alt="image-20220512213035272" style="zoom:50%;" />

**Disadvantage of “Sticking Out Strategies”**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512213100976.png" alt="image-20220512213100976" style="zoom:50%;" />

### Linear Probing

We search for the first position available to the right

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512213247833.png" alt="image-20220512213247833" style="zoom:33%;" />

#### Deletion

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512213648325.png" alt="image-20220512213648325" style="zoom:33%;" />

We have add a mark **tombstone** (instead of empty) as a mark that indicates they are deleted.

**tombstone** can be used for insert.

So the linear relation will still exist, leading to next location.

Otherwise, the link will be broken.

**Wrapped around**:

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512214250541.png" alt="image-20220512214250541" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512214334273.png" alt="image-20220512214334273" style="zoom:40%;" />

Time complexity will be Constant $O(1)$

Disadvantage: We can often see clustering, leading to same hash code (linear search).

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512215439793.png" alt="image-20220512215439793" style="zoom: 33%;" />

Thus we need double hashing



### Double Hashing (Secondary)

How to avoid cluster

hash2 strategy to deal with collisions: wrapping around (mod T)



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512220452010.png" alt="image-20220512220452010" style="zoom:33%;" />

Avoid Short Circle:

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512220645389.png" alt="image-20220512220645389" style="zoom:25%;" />

Solutions

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512220735140.png" alt="image-20220512220735140" style="zoom:30%;" />



### What to do if the table is full?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512221136463.png" alt="image-20220512221136463" style="zoom:33%;" />

What is amortized time?? 

Amortized time is **the way  to express the time complexity when an algorithm has the very bad time complexity only once in a while besides the time complexity that happens most of time**. 



### Comparison with Tree

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512221518677.png" alt="image-20220512221518677" style="zoom:50%;" />

Hash tables need more space (need to keep factor low)



### What can go wrong?

 Not terminate" is often described as go into an infinite loop."


i. A lookup operation may not terminate.
ii. A lookup operation may not find a value that is actually in the table





**Dijkstra’s algorithm** for computing lowest-cost paths from a single source node is always
correct for graphs without negative-cost edges. If a graph has negative-cost edges, the algorithm might
or might not give the right answer.

**the algorithm found the shortest path to it**, and will never have to develop this node again 

