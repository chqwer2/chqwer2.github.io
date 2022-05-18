---


layout:     post
title:      "Data Structures, Algorithms, and Databases"
subtitle:   " \"Data Basic\""
date:       2022-02-08 12:00:00
author:     "Calvchen"
header-img: "img/post-bg-infinity.jpg"
catalog: true
tags:
    - Algo
    - Data
    - Database
    - Course


---

> “Basic data courses. ”



# Data Structures, Algorithms, and Databases

Recommend Books:

1. [Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne (princeton.edu)](https://algs4.cs.princeton.edu/home/)
2. [Data Structures and Algorithm Analysis (vt.edu)](https://people.cs.vt.edu/~shaffer/Book/)
3. [Book (williams.edu)](http://dept.cs.williams.edu/~bailey/JavaStructures/Book.html)

- **Kinds:** Array, List, Trees, Tables, Graphs
- **Algorithms:** Sort, Insert, Delete, Find
- **Efficiency:** How fast? How mush memory?
- **Abstraction:** How to use? (abstract) How to implement? (concrete)
- **Specification:** What we want the algo to do?
  - Reason about its con-time complexity and space complexity

Preconditions is the condition that is **assumed to hold** at the beginning of the program.

Post-conditions is the condition that is guarenteed to hold at the end of the program.

**Invariants** is the condition that is **expected to hold** at the beginning of each **loop** iteration

Assertions is the condition that is **expected to hold** at the point where it is placed



### Array

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516083320820.png" alt="image-20220516083320820" style="zoom:33%;" />

How to store? **row-major or column major**: store by which

In column major, there we see that the row index is changing most rapidly,



Array is great if you want to move the end

But we have **constant time access** to them

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516083725414.png" alt="image-20220516083725414" style="zoom:25%;" />

Removing is $O(n)$cause we gotta move all those elements.

### Dynamic Array

Resizable, copy the old array in the new location (Double size)

Also serve constant-time read and write

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517135040143.png" alt="image-20220517135040143" style="zoom:25%;" />

Removing is $O(n)$cause we gotta move all those elements.

### Amortized Analysis: Aggregate Method

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517214328707.png" alt="image-20220517214328707" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517214346453.png" alt="image-20220517214346453" style="zoom:25%;" />

N operation / N

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517214652636.png" alt="image-20220517214652636" style="zoom:25%;" />

It is like amortizing loan. Why the below is true?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220518085430890.png" alt="image-20220518085430890" style="zoom:25%;" />

### Singly-Linked Lists

List elements need not be contiguous.

A key term and a pointer

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516083925643.png" alt="image-20220516083925643" style="zoom:25%;" />

Insert: first create the node, update the pointer to the first number. Then update the **head pointer**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516084316180.png" alt="image-20220516084316180" style="zoom:25%;" />

Other like remove will be the same. But getting last element is expensive.

So some times we have **tail pointer**.

It can still be **expensive** when we remove the last term because we need a pointer to *13* to update the tail (Go through the array from the top).

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516084712543.png" alt="image-20220516084712543" style="zoom:25%;" />

If before the insertion, the head and the tail were nil,

so it was an empty list so we've gotta update the tail

**Remember to:** check **empty** and **only one element?**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516084930168.png" alt="image-20220516084930168" style="zoom:25%;" />

In case there is only one element in the list, and get empty.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516085107276.png" alt="image-20220516085107276" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516085322547.png" alt="image-20220516085322547" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516085414737.png" alt="image-20220516085414737" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516085533381.png" alt="image-20220516085533381" style="zoom:25%;" />

Fast AddAfter….



### Doubly-Linked Lists

There is a way the get the pushback cheap

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516085636492.png" alt="image-20220516085636492" style="zoom:25%;" />

But we need to manage both pointer

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516085722600.png" alt="image-20220516085722600" style="zoom:25%;" />

### Stack

can be based on Array

We can Push(Key), Top() and Pop().

**Remember:** Check if **empty**.

It can used to track the **Balanced Brackets**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516090613494.png" alt="image-20220516090613494" style="zoom:25%;" />

### Queue

can be based on linked list (with max size)

It is a FIFS or FIFO situation

Enqueue (Key): Add key to collection.

Dequeue (): Remove the least recent key, which means the head from the front, not the tail.

Empty ()

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516091740057.png" alt="image-20220516091740057" style="zoom:25%;" />

Or implement with array (wrap around)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516091830473.png" alt="image-20220516091830473" style="zoom:25%;" />



## Search

Given an array $a$ of $n=a$ interges, then given $x$

Find an interge $y=i \text{ (for index)}$ if found, **-1** if not found.

**What if more than one found?**

- We can return the first one found.



**Linear search** on average the algo takes $\frac{n+1}{2}$ iterations, which is $O(n)$.

**Binary search** assume the $a$ is sorted (predcondition), normally is $O(log\ n)$.

- Does it really get faster? Significantly so?
  - Yes the worst case of perfect *BS* is $log_2\ n$.



![image-20220221213340922](https://chqwer2.github.io/img/Typora/image-20220221213340922.png)

Because of BS Invariant 



### Trees

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220516094722992.png" alt="image-20220516094722992" style="zoom:25%;" />



Post-order: we evaluate all children fully before evaluating a node itself.

### Binary Search Tree (BST)

Root, Descendant and Sibling.

**Level** = 1+ edge between itself and root

**Height** = maximum depth of subtree node and leaf

If we want to **insert** and **delete** elements efficiently, it will require using BST.

**Delete and insert from sorted array**

- Find the element takes $O(log\ n)$
- Shift left $z$ portion of the array takes $O(n)$, we don’t want this happened.
  - Delete require the left $z$ portion of the array to shift
  - Insert require the array to right $x$ portion to shift right

The solution will be: ***Sorted Tree***.

How to build it?

- Step 1: Have the empty tree, writen as *Empty* or $\Box$, represent by \*. 
- Step 2: Given label $x$, $l$ and $r$, represents root, left and right subtrees. we can build a new tree $\text {Fork}(x,l,r)$, 

```mermaid
graph TD
   x -->l
   x -->r 
```

Nodes is the number of roots, dispite the end subtrees.

Height is the max depth of the Nodes.

```mermaid
graph TD
   5 -->3
   5-->17
   3 -->7
   3 -->A[" "] 
   17 --> 20
   17 -->B[" "]  
   7 --> B1[" "] 
   7 --> B2[" "] 
   20 --> B12[" "] 
   20 --> B22[" "] 
   
```

Which Nodes = 5, Height = 3. The height grows logrithmically.

Leaf is the node with two empty tree. 

**Formulas to calculate:**

For convenience, we use abbreviation for short:
$$
\text{Use }n(\cdot)\ \&\ h(\cdot)\text{ for \#nodes}(\cdot)  \ \&\ \text{height}(\cdot) \\
\text{Use F for Fork}(x,l,r) \\
$$
So we have
$$
n(\Box) = 0,\ h(\Box) = 0\\
n(\text F) = 1 + n(l)+n(r)\\
h(\text F) = 1 + \max(\ h(l),h(r)\ )
$$
**Perfectly balanced tree** **(PBT)**

The right the left tree of any node have the same height

```mermaid
graph TD
   1 -->2
   1-->7
   2-->3-->B[" "]
   2-->5-->B1[" "]
   3-->B2[" "]
   5-->B3[" "]
   7-->8-->B4[" "]
   7-->9-->B5[" "]
   8-->B6[" "]
   9-->B7[" "]

```

**Formulas**
$$
\text{isPB}(\Box) = \text{true}\\
\text{isPB}(\text F) = (\ \text h(l)==\text h(r)\ )
$$
The number of nodes of whole PBT is $2^{\text(height)}-1$, of each layer is $2^{\text(height-1)}$.

If the tree is nearly balanced, the worst case of searching is $O(log\ n)$.

### Insert in BST

- If already exist, we can either report an error or leave it unchanged 

Define
$$
\text{isIn}(x,t) =
\left\{\begin{array}{ll}
\text {true,} & \text { if } x \text { occurs in }t\\
\text {false,} & \text{otherwise}
\end{array}\right.
$$

$$
\text{isIn}(x, \Box) = \text{false}\\
\text{isIn}(x, \text F(y,l,r)) = (\ x==y\ ) || \text{(find subtrees)}\\
\text{find subtrees} = (x<y)\ \&\&\ \text{isIn}(x, l) ||(x>y)\ \&\&\ \text{isIn}(x, r)
$$

![image-20220221230659407](https://chqwer2.github.io/img/Typora/image-20220221230659407.png)

### Deletion

- Case 1: Delete a leaf.
- Case 2: Delete a node with only one side.
  - We move up the other subtree
- Case 3: Delete a node with both sides.
  - We replace the vacant node by the *left-most* node or *smallest* node of the right subtree.

```mermaid
graph TD
   100[delete 100] -->50
   50 --> 30
   100 --> 200
   200 --> 150 --replace--> 100
   200 --> 250
```

> All cases take $O(log\ n)$ steps assuming the tree is balanced.

![image-20220221230551079](https://chqwer2.github.io/img/Typora/image-20220221230551079.png)

![image-20220221230620315](https://chqwer2.github.io/img/Typora/image-20220221230620315.png)

### Tree Traverse

**Depth-first**: completely traverse one sub-tree

Three can used a Stack:

InOrder: left-node-right

PreOrder: node-left-right

PostOrder: left-right-node

**Breath-first**: Traverse all the node at one level

used a queue

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220517133917727.png" alt="image-20220517133917727" style="zoom:25%;" />

## AVL Trees

Adelson-Velski and Lzudis Trees or called **self-balancing Binary Search Tree**

BST tend to grow unbalanced, we then lose the $O(log\ n)$ good time behavior. Can we assume extra conditions to make sure that the height of the tree is under control?

**Why we will lose it?**

The extreme case that all the nodes come in one line will perform like linear search.

<img src="https://chqwer2.github.io/img/Typora/image-20220222093407126.png" alt="image-20220222093407126" style="zoom:45%;" />

Assuming space is $O(n)$ for both. 

The worst case of BST is $O(n)$, but AVL remain still $O(log\ n)$.

**How to do it?**

- Assume additional conditions to keep the trees balanced.
- Define some concepts before we can state these conditions.

**Concept #1** Height of the node 

Length of the *longest* path from that node to the leaf node

Equal to the height of the subtree at that node.

**Concept #2** **Balance at the node**

(Height of left subtree) - (Height of right subtree) 

perfectly balanced, that is, the balance of each node is 0.

<img src="https://chqwer2.github.io/img/Typora/image-20220221232406993.png" alt="image-20220221232406993" style="zoom:50%;" />

<img src="https://chqwer2.github.io/img/Typora/image-20220221232502057.png" alt="image-20220221232502057" style="zoom:60%;" />

![image-20220225104427945](https://chqwer2.github.io/img/Typora/image-20220225104427945.png)

height of empty tree is -1, 

Then height of subtree at that node will be height of left subtree + 1 (for the node itself). Same is true if node has only right subtree.

**Concept #3** AVL tree

the balance at every node is $-1, 0 \text{ or } 1$.

Why consider this concept?

- Difficult to get perfectly balanced trees.
- Easier to keep trees AVL balanced.
- AVL balance is good enough to get fast algo.

**Concept #4** Perfectly Balanced Tree

The balance of every node is **0**.

General, we have: 
$$
n=2^h-1
$$
It is the best case of AVL Tree.

What is the **worst case**: 

>  We now use Fibonacci numbers.

Here, $F(\cdot)$ for Fibonacci function (start from 0 and 1).
$$
F(k) = \frac{\left(\frac{\sqrt(5)+1}{2}\right)^k - \left(\frac{\sqrt(5)-1}{2}\right)^k}{\sqrt 5}=O(1.61^k)
$$
And we have
$$
F(h+2)-1 = n
$$
Always, we have lower and upper bound of number of nodes:
$$
F(h+2)-1 \leq n \leq 2^h-1 \\
O(1.61^k) < n < 2^h
$$
Why we don’t specify the base of $O(log\ n)$?
$$
log_{10}(n) = O(log_2(n)) \\ 
log_{2}(n) = O(log_10(n))
$$
Only different with a constant factor, so it doesn’t work for O notation.

**Back to AVL Tree**

From the lower and upper bound, it implies $h = O(log\ n)$, which is something we didn’t have for BS trees.

- Invariant:
  - The balance of every node is -1, 0 or 1.

**Algo for AVL trees**

- Search: Now it really is $O(log\ n)$.
- Insert & Deletion: As before, but additionally no necessarily rebalacing. 
  - Fisrt BST method
  - Check AVL balance and fix it if necessary.
  - Can be done in total time $O(log\ n)$.

AVL Insertion Example

![image-20220222100555564](https://chqwer2.github.io/img/Typora/image-20220222100555564.png)

Need to fix the resulting tree…

Four Result Cases:

![image-20220225105002079](https://chqwer2.github.io/img/Typora/image-20220225105002079.png)

![image-20220222100825348](https://chqwer2.github.io/img/Typora/image-20220222100825348.png)

AVL insert Case LL:

![image-20220222101047920](https://chqwer2.github.io/img/Typora/image-20220222101047920.png)

AVL insert Case RR:

![image-20220222101124897](https://chqwer2.github.io/img/Typora/image-20220222101124897.png)

AVL insert Case LR:

![image-20220222101148103](https://chqwer2.github.io/img/Typora/image-20220222101148103.png)

AVL insert Case RL:

![image-20220222101213262](https://chqwer2.github.io/img/Typora/image-20220222101213262.png)

**AVL Tree Deletion**

- Delete using the BST algo
- Rebalance as necessary as before.

### Fibonacci Trees

$$
T_{-1},T_0, T_1,\dots
$$

T−1 is the empty tree • 

T0 is the one element tree • 

Th+2 is obtained by making Th and Th+1 children of the root node (as shown in the picture on the previous slide)

![image-20220225105231512](https://chqwer2.github.io/img/Typora/image-20220225105231512.png)



## Dataset

### Entity-relationship concepts

**What is a database?**

•It is a large collection of persistent data

•Typically stored on a **server** somewhere on the **net**

•Accessible from multiple applications on client computers

•Concurrently accessible and modifiable

•Expected to be secure and efficient

•Expected to be fault-tolerant (can recover from crashes). No data losses!

**Why we need database?**

Meant to suggest the “base of data” on which all the applications run.

Or internal data of organizations/ businesses



### Relational Databases

Built as a relational database management system (DBMS or RDBMS)

is a collection of tables (relations)

**Inside a Table**

Columns (attributes, felds)， Rows (records, tuples)

Null (marked as “-‘)

**Tables/Relations**

**Attributes/Columns/Fields**

**Records/Rows/Tuples**

**Schema** = Names of relations, attributes and their types

**Key** = Any attribute(s) that is unique across all the rows

**Primary key** = A designated key that is meant to uniquely identify the records.

### Entity-relationship (ER) modelling 

All the “things” for which data needs to be kept are **entities**.

In addition, there are also **relationships** between entities can described in one-sentence description.

We depict entities by **rectangles** and relationships by **diamond boxes**, attributes are **oval** boxes (not a must element).

<img src="https://chqwer2.github.io/img/Typora/image-20220313163303254.png" alt="image-20220313163303254" style="zoom:50%;" />

**Attributes** (for both entities and relationships)

**Book**: Author(s), Title, Publisher, Year of publication

**Member**: Membership number, Name, Address, Date of joining

**borrowed**: Date of borrowing, Due date, Return date, Fine (if any)

### Multiplicities

Number of times the entity can **participate** in the relationship

For example,

- A book may or may not be borrowed. If it is borrowed, there is only one borrowing.
- So, minimum = 0, maximum = 1.

![image-20220313163949090](https://chqwer2.github.io/img/Typora/image-20220313163949090.png)

Here the Book class is an **entity set** contains of many book **entities**.

**(1,1)** is a special case that defining a constraint.

Example:

- (0, 1) :The **instance** appears at most once in the relationship. An employee may or may not be supervised
- (1, 1) : The **instance** must and will appear exactly once in the relationship.
- (0, n) : the **instance** may appear more than once. Such as a customer may have placed many or no order in a given time interval.
- (1, n) : The **instance** appears at least once but can appear many times.

[ER Graph Example](#ER Examples)

### The design and creation

By **default,** every entity and relationship in our ER model becomes a **table** in the database, written in **schema** notation.

**Constraint**: Also we have unique identifiers for each entity, the relationship table table must necessarily occur in this field.

### Table design

The 3-table design for this model:

- Book (<u>book id</u>, authors, title, publisher, year)

- Member (<u>member id</u>, last name, first name, address, date of joining)

- Borrow (<u>book id, member id</u>, borrow date, due date, ~~return date, fine~~)

> We can also use tables for this model, if we ignore **fines**
>
> 1. We can add the Borrow fields to the Member table
>
>     (book id, borrow date, due date, return date, fine)
>
> 2. Or to the Book table 
>
>    (member num, borrow date, due date)

**The issue after optimisation 1** 

We must allow some attributes can be **null^o^**. 

And it won’t work if we permit multi-borrowing.

It is not a good idea to hard-wire business policies into the database design! 

**The issue after optimisation 2**

We must allow some attributes can be **null^o^**. 

we cannot represent the **fines** (charge) satisfactorily in this design.

- Perhaps we can add the Borrow fields to both the Book table and the Member table?
  - It would introduce redundancy in the design

**Summary:**

- If a **relationship** has (0, 1) or (1, 1) multiplicity with an entity, its table can be merged with that of the entity. 
- (0, 1) should allow null.



### Weak entities

Suppose our library has **multiple copies** of some of the books.

Suppose our library allows **family memberships**.

How do we deal with it?

> **Weak entities**: depend on some other entity for its identity.

A weak entity’s **primary key** consists of the primary key of its main entity (owner entity) and some additional attributes.

- Copy dependent on Book.
- Borrower dependent on Member.

![image-20220313171215500](https://chqwer2.github.io/img/Typora/image-20220313171215500.png)

What happen if just one copy or the member itself want to borrow books?

#### Table for weak entities

<img src="https://chqwer2.github.io/img/Typora/image-20220313171520785.png" alt="image-20220313171520785" style="zoom:50%;" />

**Other examples**

```mermaid
graph RL
  employee -->|"(0,1)"| e[\supervised by\]
  e --> employee
```

### Hierarchies

Represent **is-a** relationship.

> UG student is a student.

**Example – Customer hierarchy**

![image-20220313173544497](https://chqwer2.github.io/img/Typora/image-20220313173544497.png)

Two features need to be specified.

- Coverage (**t/p**)
  - Do subclasses **totally** cover all of the superclass? Or **partially**?
- Overlap (**o/e**)
  - Are the subclasses **overlapping**? Or **exclusive**?

### **Table for Hierarchy**

```mermaid
graph BT
B -->|"(c,x)"| A
C -->|"(c,x)"| A 
```

Three possible ways:

- Keep all three 

  - simplest and always applicable
  - superclass (common attributes) inherited by B and C subclasses (additional attributes)

- Keep A, and omit B and C (Only superclass)

  - need to add a **variant** attribute specifying the subclass type
  - the attributes corresponding to other types will be null
  - always possible

- Keep B and C, and omit A (Only subclasses)

  - respect to superclass table which is not stored 
  - some attributes are duplicated
  - only possible if the coverage is **total**, and overlap is **exclusive** (redundancy).

  

**redundancy** makes it confusing that don’t know where to find the data



### Relational DBMS (SQL)

A database management system (DBMS) is a software system (made by providers like IBM, Oracle, Postgres, MySQL).

- Creating tables.
- Querying tables for finding information.
- Adding, deleting or modifying records in tables.
- **Ensuring that constraints** continue to be satisfied during modifications.

#### SQL

**SQL command to create the entity**

<img src="https://chqwer2.github.io/img/Typora/image-20220313165405779.png" alt="image-20220313165405779" style="zoom:50%;" />

- **unique** and **“not null”** keyword. All fields can be null by default (a bad feature of SQL!)

- The **primary key** declaration says that the bookid field can be used for uniquely identying records. (It is redundant in this case.)

- **varying** defined the maximum length of attributes.

  

**SQL command to create the relationship**

<img src="https://chqwer2.github.io/img/Typora/image-20220313165631448.png" alt="image-20220313165631448" style="zoom:70%;" />

- **reference**: declare that the corresponding entity id fields, cannot be **null**

- The id fields *together* uniquely identify a **record** in this table.

  

**SQL query examples**

- This query finds the id number of Jane Austen’s *Pride and Prejudice*.

```sql
select bookid
from book
where authors = 'Jane Austen'
	and title = 'Pride and Prejudice';
```

- With a minor variation, we can ask it to tell us **whether the book is available** or it has been issued out to somebody.

```sql
select 'not available';
from book, borrow
where book.bookid = borrow.bookid
   and authors = 'Jane Austen'
   and title = 'Pride and Prejudice';
```

### Some questions you might think about

- Our table has a single field for all the authors of a book. Can we list each author individually, somehow?

- If we have multiple copies of books in the library, what can we do?

- If we want to allow a member to borrow to multiple books (say 4 books max), what changes do we need in the design?

- If membership is actually “family membership” so that anybody in the family can borrow, do we need to change the design in anyway?

- The “primary key” of the borrow table consists of two fields. Do we need two? Can we make do with one field only?

Learn some SQL!

### SQL data types

- INT (or INTEGER), DECIMAL(n, m) with length of n and m digits
- BOOLEAN, CHAR(n), VARCHAR(n)
- TEXT, DATE, TIME

### SQL commands for tables

![image-20220313203147546](https://chqwer2.github.io/img/Typora/image-20220313203147546.png)

- **not null**: not designated as possibly null in the schema
- **references**: constraint for all references into other tables (including superclass)

**How to generate ID number?**

In standard SQL, we can declare

```sql
create sequence staffid_seq;

create table Tech(staffid integer DEFAULT nextval(staffid_seq); ... )

create table Admin(staffid integer DEFAULT nextval(staffid_seq); ... )

```

This creates a sequence generator in the database and generate a new integer value each time.

**Foreign key** 

Fields with “references” constraints are called foreign keys.

The DBMS ensures that, whenever we insert a record with a foreign key value, that value is *actually present* in the **referenced table** (Synchronization)

**But what happened when deleted?**

- Then the foreign key constraint would be violated!
- So blocked by DBMS (ON DELETE NO ACTION)

### Constraint

They allow us to **detect errors** and make sure that the data in the system is consistent and valid.

- **Field constraints** – constraint on the value of a field (e.g., NOT NULL)
- **Record constraints** – constraints on an entire record (e.g., you might check that the due_date is greater than the borrow_date)
- **Table constraints** – constraints on the entire table (e.g., PRIMARY KEY or UNIQUE).
- **Database constraints** – constraints that span multiple tables (e.g., REFERENCES)
- **referential integrity constraint**





**ON DELETE constraint**

- ON DELETE NO ACTION – default, no need to declare
- ON DELETE SET NULL
  - This **sets the foreign key to null**, if possible.
  - If null is not allowed, we get an error.
- ON DELETE CASCADE (串联)
  - The record with the foreign key gets deleted automatically.

Think of what the effect of these declarations would be when a library member quits and we try to delete their record.

What should happen to a borrow record that might still be referencing that member?

### 



### Exercise

Identify entities, relations

We need to:

- Keep our model as simple as possible.

##### Exercise from notes (Paragraph 16(a)):

**Identifying entites**

![image-20220313175510455](https://chqwer2.github.io/img/Typora/image-20220313175510455.png)

**Which of them are really needed?**

<img src="https://chqwer2.github.io/img/Typora/image-20220313174827172.png" alt="image-20220313174827172" style="zoom:50%;" />

**Identifying relationship**

![image-20220313175522768](https://chqwer2.github.io/img/Typora/image-20220313175522768.png)

**Which of them are really needed?**

<img src="https://chqwer2.github.io/img/Typora/image-20220313174838683.png" alt="image-20220313174838683" style="zoom:50%;" />

Attempt exercises in Paragraph 39.

But the Exercise Sheet 1 is higher priority. We will have a quiz on it!

## Relation Algebra

Note:  that **SQL** is based on what are called "multisets" or "bags" and so does  **allow duplicates** whereas **Relational Algebra** is based on sets and so does **NOT allow duplicates**. 

**Database** = A Collection of relations (Tables)

**Relations** = Consist of **Attributes** (Columns)

Data consists of **Tuples** (Rows) and each tuple has a value associated with each attribute. 

Each Attribute has a **Domain** (Type) 

The **Schema** is the structure of the database and includes the Name, Attributes and  the Type of each Attribute associated with every relation in a  database. 

The **Instance** is the CONTENTS of the tables at a given point in time. 

All values have a type, but there is a special value that is part of all types - **NULL** (Undefined, unknown)

A **Key** is an Attribute of a relation the value of which is unique for each tuple.

Relational Algebra provides operators to **Query**:

- Filter relations
- Slice relations 
- Combine relations 



Through this session we will make use of the following tables: 

**Students:** 

| sID  | sName | sFirstDegree | sFDMarks |
| ---- | ----- | ------------ | -------- |
| 1    | Alice | English      | 77       |
| 2    | Bob   | Fine Art     | 80       |

**Modules:**

| mID  | mName       | mLecturer |
| ---- | ----------- | --------- |
| 1    | Intro to CS | BoB       |
| 2    | Databases   | Harish    |
| 3    | AI and ML   | Harish    |

**Marks**

| sID  | mID  | assignMarks | examMarks |
| ---- | ---- | ----------- | --------- |
| 1    | 1    | 15          | 80        |
| 1    | 2    | 18          | 70        |
| 2    | 1    | 12          | 81        |
| 2    | 2    | 18          | 66        |

AND operator: ∧ (Caret)  

#### Select Operator $\sigma$

ρ_\text{M1( M1.mID, M1.mName, mLecturer )}\text{(Modules)
$$
 \pi_{cid, sid}(\sigma_{year=2020}lecturing)
\\⋈\\
\pi_{cid, sid}(\sigma_{year=2021}lecturing)
$$
To pick a subset of the **rows** from a relation. 

The symbol for the Select Operator is: **σ (sigma)**
$$
\sigma_{(condition\ ∧\ condition ...)} <Table Name>
$$
For example:
$$
σ_{sFDMarks\ >\ 77\ ∧\ sID\ >\ 1} Students
$$
**SQL Equivalent**: 

```sql
SELECT * FROM Students WHERE sFDMarks > 77 AND sID > 1
```

Time complixity: *O(n)*

#### Projection Operator $\pi$

While the select operator picks a subset of rows, the project operator **picks a subset of columns**

For example:
$$
\pi_\text{A1,A2,...,An}\text R
$$

$$
π_{sID,\ examMarks}\ Marks
$$
SQL Equivalent:

```sql
SELECT sID, examMarks from Marks;
```

Time complixity: *O(n)*

**Making expressions** 

Since every operator returns a relation we can combine operators as follows:
$$
π_\text{sID,\ examMarks}\ ( σ_\text{examMarks > 70}\ \text{Marks} )
$$
SQL Equivalent:

```sql
SELECT sID, examMarks FROM ( 
    SELECT * FROM Marks WHERE examMarks > 70 ) 

SELECT sID, examMarks FROM Marks WHERE examMarks > 70
```

#### Cross-Product or Cartesian Product Operator $\times$

This is an operator that is used to combine two relations. 

As a notational requirement, when the **same column name exists in both the relations** then the columns in the result are **prefixed** by the name of the relation they come from. 
$$
\text{Student}\ \times\ \text{Marks}
$$
SQL Equivalent

```sql
SELECT 
    Students.sID, sName, sFirstDegree, sFDMarks, mID, 
    Marks.sID, assignMarks, examMarks  
FROM Students, Marks;
```

**WARNING**: sID from students is named students.sID and that from Marks  is called Marks.sID which requires explicitly stating this in SQL

 

So it is not useful in SQL, unless we filter it first (equal to **join**):
$$
\sigma_\text{(students.sID = Marks.sID)}\ \text{Student}\ \times\ \text{Marks}
$$
SQL:

```sql
SELECT 
    Students.sID, sName, sFirstDegree, sFDMarks, mID, 
    Marks.sID, assignMarks, examMarks  
FROM Students, Marks 
WHERE Students.sID = Marks.sID
```

Time complixity: *$O(n^2)$,* highly **inefficient**.

#### Natural Join  **⋈ (bowtie)**

Or just **Join**, *is the **most important** operation in the DBMS.

It can be rewritten using a combination of projection, selection and cross-product. 

Performing cross-product and additionally:

1. Enforces the **equality** on all attributes with the **same name**
2. Eliminates one copy of the duplicate attribute

Students ⋈ Marks allow us to write the following as equal: 
$$
\sigma_\text{(students.sID = Marks.sID)}\ \text{Student}\ \times\ \text{Marks}
$$
simply SQL

```sql
SELECT * FROM Students NATURAL JOIN Marks 
```

Time complixity: $O(n)$ if tables are sorted by the join column, $O(n^2)$ otherwise.

**EXERCISE**: Write the equivalent Relational Algebraic expression for the Natural Join above, without using a Natural Join. 



#### inner join

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512222656814.png" alt="image-20220512222656814" style="zoom:25%;" />

O(n^2), expensive

#### Otter Join

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512222804431.png" alt="image-20220512222804431" style="zoom:25%;" />

Doing join efficient: sort the join column

One is sorted, other is not. 

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512223038390.png" alt="image-20220512223038390" style="zoom:25%;" />

![image-20220512223119428](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512223119428.png)



#### Theta Join $⋈_\theta$

The Theta Join operator while additionally implementing a condition. 
$$
\text{Exp1} ⋈_{<condition>} \text{Exp2}
$$
SQL:

```
SELECT * FROM EXP1 JOIN EXP2 ON( <condition> );
```

is equivalent to:
$$
\sigma_{\theta}\ (\text{Exp1} \times \text{Exp2} )
$$
**Making expressions** 

List the names of the students who secured a **score of more than 80** in the final exam i**n modules taught by Bob**. 
$$
π_\text{sName} ( σ_\text{examMarks > 80 ∧ mLecturer = 'Bob'} ( (\text{Students} ⋈ \text{Marks}) ⋈ \text{Modules}) )
$$
SQL Equivalent: 

```
SELECT sName 
FROM (Students Natural Join Marks) Natural Join Modules
WHERE examMarks > 80 and mLecturer = 'Bob'
```

#### **Rename Operator** $\rho$

 Rename the Attributes but not the relation:
$$
ρ_\text{R( A1, A2, ... An)}\ (\text E)
$$
Or rename the relation:
$$
ρ_\text R (\text E)
$$
SQL Equivalent: 

```
SELECT EA1 AS A1, EA2 AS A2 ... EAn AS An 
FROM E AS R
```

#### Self Joins

While the rename operator is used for various kinds of queries, the most important is the self join which would not be possible without this. 



Example: List the pairs of modules taught by the same lecturer. 

The only way to do this is to use a **self join**. 
$$
σ_\text{( mLecturer = mLecturer)}\text{ (Modules × Modules)}
$$
Since this does not clearly tell us **which mName to equate to which**, we  must rename the two relations and the corresponding attributes. 
$$
ρ_\text{M1( M1.mID, M1.mName, mLecturer )}\text{(Modules)} \\⋈\\
ρ_\text{M2( M2.mID, M2.mName, mLecturer )}\text{(Modules)}
$$
Of course, to avoid duplicates and **A, B; B, A** we must have: 
$$
π_\text{( M1.mName , M2.mName )} (\\

σ_\text{( M1.mName < M2.mName )} (ρ_\text{M1} ⋈ ρ_\text{M2}

)\

)
$$

#### Combing Results using Set Operators

The three set operators are:

Union: $\cup$, Difference: $-$, Intersection: $\cap$

Notes: In relational Algebra these three set operators MUST be applied on the **SAME schema**. This means that if you want to find the union of lecture names and student names you MUST first **rename them**. 
$$
\text{E1} ∩ \text{E2}\ \text{  is equivalent to }
\
\text{E1 - ( E1 - E2 )}
$$

$$
\text{E1} \cap \text{E2}\ \text{  is equivalent to }
\
\text{E1}\bowtie \text{E2}
$$

### Examples

<img src="https://chqwer2.github.io/img/Typora/image-20220313220511808.png" alt="image-20220313220511808" style="zoom:67%;" />

**Outer Join**

<img src="https://chqwer2.github.io/img/Typora/image-20220313220536773.png" alt="image-20220313220536773" style="zoom: 67%;" />

**Left Outer Join**

<img src="https://chqwer2.github.io/img/Typora/image-20220313220627569.png" alt="image-20220313220627569" style="zoom:67%;" />

**Rename** operator examples:

<img src="https://chqwer2.github.io/img/Typora/image-20220313220755549.png" alt="image-20220313220755549" style="zoom:67%;" />

<img src="https://chqwer2.github.io/img/Typora/image-20220313220837487.png" alt="image-20220313220837487" style="zoom:67%;" />

**Self Join** will get same table back, but with **renaming**

<img src="https://chqwer2.github.io/img/Typora/image-20220313220936681.png" alt="image-20220313220936681" style="zoom:67%;" />

![image-20220313220953923](https://chqwer2.github.io/img/Typora/image-20220313220953923.png)

Then to get rid of the useless records
$$
σ_\text{ m1ID < m2ID}
$$
<img src="https://chqwer2.github.io/img/Typora/image-20220313221140972.png" alt="image-20220313221140972" style="zoom:67%;" />

Will be efficient if tables are sorted on the **primary key**.

#### Sortedness in databases

- To achieve sorted order, database tables are stored in a **search tree data** structure. (**B-tree**)
- Data records are stored in the **leaf nodes**. The internal nodes only have **search keys** for navigation.
- The trees can be traversed in sorted order in O(n) time.
- **Multiple sort keys** can be accommodated by building multiple B-tree indexes for the same table.

**Semi-efficiently**: If the join column is sorted in one table R (of size n), and not sorted in the other table S (also of size n)

- We can traverse the S table in linear order and search for each key value in R.
- Since searching can be done in log n time,

- The overall time complexity is $O\text{(n logn)}$.

**Inefficient:** $O\text{(n)}$

More: Efficiency also depends on doing the operations in the right order.

> For example, consider (M⋈B)⋈C versus M⋈(B⋈C).
>
> If M is a large table, but B and C are small, the second form may be better.
>
> But if we are joining on the primary key of M, it doesn’t matter because M⋈B would be of the same size as B.

The selection operator σ should be done as early as possible, because it reduces the size of the table.

### Decomposition

Split large table into small ones

efficiency?

Or neat structural table to read or more meaningful

We use decomposition to produce tables in “**normal form**”, which do have unwanted “**functional dependencies**”.

<img src="https://chqwer2.github.io/img/Typora/image-20220313222716579.png" alt="image-20220313222716579" style="zoom:50%;" />

Normally if we change the manger name, it will need to process multiple times,  but after decomposition we only need to do it once.

**How do we know to decompose this way?**

Functional dependencies:

```mermaid
graph LR
empID --> Name
empID --> Dept --> Manager
```

Since **Dept** is **not the primary key** of the table, a **functional dependency on it** is a candidate for decomposition.

**functional dependency** 

We have $A_1, A_2, \dots, A_n \to B$, read as A determine the B.

B is the functional dependency on A,

>if any two rows in the table have the same values for A1, A2,… An,
>
>then they have the same value for B.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512223532760.png" alt="image-20220512223532760" style="zoom:50%;" />

A depends on B depends on C, so we don’t need to clarify A depends on C because it is clear in the relation.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512223926368.png" alt="image-20220512223926368" style="zoom:30%;" />

Transitivity

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512225125078.png" alt="image-20220512225125078" style="zoom:33%;" />

Closure algo

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220512225507189.png" alt="image-20220512225507189" style="zoom:50%;" />

### Exercise 59 and 60 in handout.

### Candidate Keys

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513100136744.png" alt="image-20220513100136744" style="zoom:33%;" />

Here, *empID* is a candidate key that determine any other attribute in the table

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513100226348.png" alt="image-20220513100226348" style="zoom:25%;" />

#### Unwanted Key

**Redundancy**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513100554030.png" alt="image-20220513100554030" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513100507463.png" alt="image-20220513100507463" style="zoom:25%;" />

Potential problem

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513100624694.png" alt="image-20220513100624694" style="zoom:25%;" />

**Anomalies**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513100850447.png" alt="image-20220513100850447" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513101011964.png" alt="image-20220513101011964" style="zoom:25%;" />

Delete

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513101338450.png" alt="image-20220513101338450" style="zoom:25%;" />

Aggregate, See paragraph 66

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513101609888.png" alt="image-20220513101609888" style="zoom:25%;" />

Many lecturers are teaching same course this year..

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513101645392.png" alt="image-20220513101645392" style="zoom:50%;" />

### BCNF

has not unwanted dependency 

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513102326642.png" alt="image-20220513102326642" style="zoom:33%;" />

Decompose them

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513102604289.png" alt="image-20220513102604289" style="zoom:25%;" />

If we join this two sub-tables, we will get the origin table (*losslessness*)

But when we get new record?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513103049304.png" alt="image-20220513103049304" style="zoom:25%;" />

We cannot have different value $W$ accociated with $U$.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513103335525.png" alt="image-20220513103335525" style="zoom:25%;" />

How to get BCNF?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513103649455.png" alt="image-20220513103649455" style="zoom:25%;" />

ACID

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513130744030.png" alt="image-20220513130744030" style="zoom: 25%;" />

### Database Transactions

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513123857826.png" alt="image-20220513123857826" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513124129932.png" alt="image-20220513124129932" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513130138688.png" alt="image-20220513130138688" style="zoom:25%;" />

SET TRANSACTION **READ ONLY**

BEGIN TRANSACTION

•A read-only transaction can be executed in parallel with other **read-only transactions** without any worry of inconsistency.

•But they will not be executed in parallel with **read-write transactions** for the same data.

•Use this, for example, if you want to tell the user about the **availability** of all the window seats.

**READ WRITE** is default, The transaction is allowed to do both select queries and updates. 



**Dirty**

SET TRANSACTION READ WRITE
    ISOLATION LEVEL READ UNCOMMITTED
BEGIN TRANSACTION

“Dirty” data means data that is currently being modified by another transaction, but not yet committed.

If the other transactions **aborts** instead of committing, the data in our possession would have become **invalid**.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513130608147.png" alt="image-20220513130608147" style="zoom: 25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513130709312.png" alt="image-20220513130709312" style="zoom: 25%;" />





### Serializability

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513124354976.png" alt="image-20220513124354976" style="zoom: 33%;" />

•Then the first client’s booking would **get overwritten**, and that customer would have lost their seat even though they have a confirmation that their seat was booked!

•The solution is to package the two steps **into a single transaction**.

•Then the server ensures that the second client gets **delayed** if it is trying to book the same seat as the first client.

### Atomicity

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220513125931182.png" alt="image-20220513125931182" style="zoom:25%;" />







### Some SQL example

querying the database

A row is also called an entry or tuple or record

```sql
CREATE TABLE technicians (
    	tid SERIAL PRIMARY KEY UNIQUE
    		REFERENCES staff(staffid),
    	firstname VARCHAR(15) UNIQUE,
        lastname VARCHAR(20),
    	phone VARCHAR(20) Not NULL,
   		address VARCHAR(20) Not NULL,
        test VARCHAR(15) 
    		REFERENCES test(testid) 
    		ON DELETE  SET NULL,,
        expert_model VARCHAR(15) NOT NULL 
    		REFERENCES model(modelid)
    		ON DELETE  SET NULL,, 
    
);
```



```sql
CREATE TABLE airplane (
    	aid SERIAL PRIMARY KEY  UNIQUE,
      
        belong_model VARCHAR(15) NOT NULL 
    		REFERENCES model(modelid) 
    		ON DELETE  SET NULL,
        test VARCHAR(15)  
    		REFERENCES test(testid)
    		ON DELETE  SET NULL, 
    	airport VARCHAR(15) Not NULL 
    		REFERENCES airport(airportid) 
    		ON DELETE  SET NULL,
    
);
```



```sql
CREATE TABLE belongto (
    	bid SERIAL PRIMARY KEY  UNIQUE
        belong_model VARCHAR(15) NOT NULL 
    		REFERENCES model(modelid) 
        	ON DELETE CASCADE,
    		
    	airport VARCHAR(15) Not NULL 
    		REFERENCES airport(airportid) 
        	ON DELETE CASCADE,
    	
);
```



Create Table

```sql
CREATE TABLE staff (
    	sid SERIAL PRIMARY KEY,
        title VARCHAR(6) NOT NULL,
        firstname VARCHAR(15) UNIQUE,
        lastname VARCHAR(20),
        email VARCHAR(40),
        office INT,
        phone INT REFERENCES courses(cid),
);

# PRIMARY KEY (cid, sid, year)
```

Create Table 2

```sql
CREATE TABLE children (
    first_name CHAR(10) NOT NULL,
    dob DATE NOT NULL,
    employeeID INT NOT NULL
        REFERENCES employee(employeeID)
        ON DELETE CASCADE,
    PRIMARY KEY (first_name, employeeID)
);
```

Create Table 3

```sql
CREATE TABLE staff(
    salary DECIMAL(10,2) NOT NULL
   		CHECK(salary >= 0),
    ...
    CHECK(rental_start <= rental_end)
);
```



```sql
SELECT price * 1.42 AS "Price in Euros", productname FROM productlist;
```



```sql
SELECT * FROM staff WHERE phone = 44774;
```

The resulting strings can be concatenated together using the operator “||”.

```sql
SELECT ’0121 41’ || phone AS "National phone number" FROM staff;
```

<> for “not equal”, which is different from Java’s !=

Apart from the test for equality (denoted by “=”) it also offers the operator “LIKE”.

```sql
<some string> LIKE <some pattern>
```

Finally, we point out the operator “iLIKE”, which behaves like “LIKE” except that it likes to ignore case.

Below will find all Ann’s, all Anne’s, all Anna’s and all Annemarie’s.

```sql
SELECT name FROM staff WHERE firstname LIKE ’Ann%’;
```

start up: psql -h mod-fund-databses

Leave the program psql by typing \q. \? help.



How to determine relationship?

Often, relationships are expressed by *verbs*.

```sql

```



```sql

```



```sql

```

![image-20220316172359548](https://chqwer2.github.io/img/Typora/image-20220316172359548.png)

Please record these assumptions in your answer.



##### ER Examples

![image-20220317153816143](https://chqwer2.github.io/img/Typora/image-20220317153816143.png)

![image-20220317154741602](https://chqwer2.github.io/img/Typora/image-20220317154741602.png)

![image-20220317154811082](https://chqwer2.github.io/img/Typora/image-20220317154811082.png)

![image-20220317154823799](https://chqwer2.github.io/img/Typora/image-20220317154823799.png)

[Multiplicities](#Multiplicities)

### Design theory of relational databases

### Physical design and concurrency









### 

# Exam

Focus on data algorithm and analysis



1.How long? What can it do? Variables?
