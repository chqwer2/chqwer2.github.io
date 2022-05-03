# Sorting

As for many algo:

![image-20220328214629949](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328214629949.png)



### Bubble Sort

Sort a given array from smallest to largest.

**Time Complexity**: $O(n^2)$

For every number, move it if it **larger than** its right number.

**Cons:** Only sort one element at a time



### Merge Sort

A D&C algorithm, handle multi elements simultaneously. 

**Step 1** – Recursively divide an array into two subarrays, until there is only one element in these subarrays. (**Use the middle point**)

**Step 2** – Repeatedly merge two subarrays and make them sorted, until all subarrays have been merged into one array.

**Time Complexity**: Split: log(n), Merge: O(n), Overall: O(nlog(n))

The last step is iterate inside the two subarray.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328215225435.png" alt="image-20220328215225435" style="zoom:50%;" />

### Quicksort

Also D&C algo.

**Step 1** – Select an element from an array, called **Pivot**.

**Step 2** – Partition the array by moving all elements that are **smaller than the Pivot** to the left side of the Pivot, and all elements that are **bigger than** the Pivot to the right side of the Pivot.

**Step 3** – Apply Step 1 and 2 recursively until the whole array get sorted.

L & R are pointer, P is the element.

R -> P at the first time.

L try to find the first larger than P

R try to find the first smaller than P 

**Swap** recursively into two part, then again

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328220035361.png" alt="image-20220328220035361" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328221421404.png" alt="image-20220328221421404" style="zoom:50%;" />

And then apply it to the two sub-array.

**Time Complexity**:

 The pivot partition process will segregate the larger and smaller values within the array. So that we reduce the sorting of a problem of size n to two problems of size n/2 (approximately). 

  On average: O(nlog(n))

  Worst case: O(n^2 ) e.g. sort a nearly sorted array and use the first or last element as the pivot.



**Space Complexity**: O(log(n))

 

**Quick discussions**: 

§How to choose a good Pivot?

§Is it a stable algorithm?



### Heapsort

Comparison based algo, not D&C algo.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328222414051.png" alt="image-20220328222414051" style="zoom:25%;" />

**Priority Queue**

in the normal queue, we only have index.

The priority is determined by the value of the element. (smallest or largest first)

PQ must support at least **three operations**:

**is_empty**: check whether the queue is empty.

**insert**: add an element with an associated priority.

**pull**: remove the element with the highest priority from the queue and return it.



In order to build the PQ, we need a complete binary search tree (completely filled).

#### Binary Heap

**Binary Heap** is a **Complete Binary Tree** which satisfies the **heap property** (also called heap invariant).

The value of its leaf within is **either all smaller or larger** than its parent node.

•>=, Max-Heap 0-> 100

•<=, Min-Heap 100-> 0

**Binary Heap Structure**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328223433384.png" alt="image-20220328223433384" style="zoom:33%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328223421118.png" alt="image-20220328223421118" style="zoom: 33%;" />

**How to build a max heap tree?**

From a normal tree to heap tree…

Step 1: Find the “last” parent node in the tree and its children. (Means index in order of 5,4,3,2,1…)

Step 2: Within this subtree, find the largest number and swap it with the root node within this subtree (To make it heap). Then do this again on the swapped node.

Step 3: Repeating Step 1 and Step 2 until reaches the root of the original tree.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220328224022973.png" alt="image-20220328224022973" style="zoom:50%;" />

So by doing the above, we **get all left and right sub tree heaped** now looking at the root.

$\infty \checkmark$

### **Heapify**: 

Start from the root node.

If the index of the right child is smaller or equal (<=) to the size of the tree, then **compare the value of the left and right child**. Swap the larger one with the root node if the value is bigger than the root node. 

Then we get the root tree heap, but because of the swap, we need to do it on the swapped sub-tree

Repeat this process on the swapped node.

This is a top-down process, we only need to handle half of the tree.

**Why we need this**: if the index of the right child is smaller or equal (<=) to the size of the tree????  # Todo



**Remove** we also need to work out a way to remove the root and remain heap.

Step 1: Swap the root node with the last node in the tree. (the smallest 10 in the example)

Step 2: “Cut” the last node, and move it to the last empty space of the array.

Step 3: Heapify the tree.

Step 4: Repeating Step 1 to Step 3.





**Space Complexity**: O(1)

**Time Complexity:** O(nlog(n)), Why

1. Heapify is O(logn), because we only need to handle half of the tree
2. Build Max-heapfy O(n)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329100228146.png" alt="image-20220329100228146" style="zoom:50%;" />

![image-20220329102443417](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329102443417.png)

| **Name**  | **Average** | **Worst** | **Space** | **Stable** |
| --------- | ----------- | --------- | --------- | ---------- |
| MergeSort | O(nlogn)    | O(nlogn)  | O(n)      | Yes        |
| QuickSort | O(nlogn)    | O(n^2)    | O(logn)   | No         |
| HeapSort  | O(nlogn)    | O(nlogn)  | O(1)      | No         |

#### Time Complexity – MergeSort/ QuickSort (best case O(nlog⁡(n))

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329102822815.png" alt="image-20220329102822815" style="zoom:33%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220329102828423.png" alt="image-20220329102828423" style="zoom:50%;" />