# Concurrency & Threads

[Week#7 Exercises.pdf](file:///C:/Users/calvchen/Documents/Week%237 Exercises.pdf)

[Week 7 - Concurrency & Threads (1).pdf](file:///C:/Users/calvchen/Downloads/Week 7 - Concurrency & Threads (1).pdf)

Useful Quiz: [bk.dvi (os-book.com)](https://www.os-book.com/OS9/practice-exer-dir/7-web.pdf)

Token System: 

Some Quizs: http://wiki.dreamrunner.org/public_html/Misc/Train/InterviewPreparation/Multi-ThreadingQuestions.html

![image-20211111151621484](https://chqwer2.github.io/img/Typora/image-20211111151621484.png)

[**Concurrency Problems:**](http://www.myreadingroom.co.in/notes-and-studymaterial/65-dbms/532-concurrency-problems.html)

Concurrency control is  important because the simultaneous execution of transactions over a  shared database can create several data integrity and consistency  problems. The three main problems are **lost updates, uncommitted data, and inconsistent retrievals**.

and Solutions

https://www.geeksforgeeks.org/concurrency-problems-in-dbms-transactions/

There are many techniques that can be used to **prevent** multiuser concurrency problems

https://www.informit.com/articles/article.aspx?p=22681&seqNum=3

such as **Timestamping**



# Exercises 

##### Process vs. thread: which one can handle tasks better?

There are two types of concurrent programming in computing: multithreading and multiprocessing [page]([Process vs. thread: which one can handle tasks better? | by Jaime Dantas | Reverse Engineering | Medium](https://medium.com/reverse-engineering/process-vs-thread-which-one-can-handle-tasks-better-264fc1188fb6))

Process: costly of time creating one and connot share memory

However, not everything about threads is perfect. Whenever you’re dealing with threads, you’ll need to pay special attention not to step on each other, which can lead to all sorts of problems like a [race condition](https://en.wikipedia.org/wiki/Race_condition).



1. Do you think there will be any performance difference in creating a new thread compared to creating a new process? Explain what the difference is.

   **overhead time** is any combination of excess or indirect computation time, memory, bandwidth, or other resources that are required to perform a specific [task](https://en.wikipedia.org/wiki/Task_(computing)).

2. Give three example applications where using threads will be more efficient than using processes.

   small tasks

3. Can a deadlock arise when you only have a single, single threaded process? Explain

   **No, it is not possible** to have a deadlock in a single-threaded process. 

4. A supermarket has sensors on each entrance that detect when a customer enters or leaves. These sensors send a signal to a central  computer whenever a **customer enters or leaves**. This computer, amongst  other things, keeps a **running count** of how many people are in the shop  at any one time. This is used to **control a traffic light system** that only allows customers to enter the store when the number of customers is below a safe limit. Last week, **the store was empty** - but the system  refused to let anyone in. What went wrong? How would you fix it?

   Sensor connection problem:

   The blocking problem: one-thread process. sensors attempted to send signals to 

   The initialization problem...

   use an uint type to store the number...

   我们可以通过一个标识synchronized来解决这类问题,具体怎么用如下：

   ![image-20220109165448757](https://chqwer2.github.io/img/Typora/image-20220109165448757.png)

   那么什么是synchronized标识呢？synchronized标识的是一代码段或者方法，即为“对象互斥锁”锁住的部分，那到底通过这个标识是怎么使得上述代码不再出现-1呢？其实是这样，上述代码中t1和t2两个线程启动后不断run，那么通过这个标识后，就会使得同一时间只能由一个线程来执行该代码段或者方法，通过如此，就能解决线程中的冲突问题了。
   

   **Other Case**

   不论是要从这个超市拿走水果，还是要送来水果，都需要通过一个**操作台**来控制，而这个操作台，同一时刻只能有一个人进行操作。

   小张和小明做着完全相同的操作，但小张操作太慢了，刚刚点击完了苹果商品的图标，系统就显示了下一个人的号码5号。-- Multi-threading

   至于选择什么号码，老师学生或是宿管阿姨都无法决定和干预，只能任凭这个操作台来决策（**操作系统决定线程的切换和时间的分配**）。但好在，每个人在操作台上都有自己的账号（**线程的工作内存**），操作一半被中断的数据并不会丢失。

   

   一个比较经典的例子是，用一个全局变量做计数器，然后开N个线程去完成某个任务，每个线程完成一次任务就将计数器加一，直到完成100次任务。如果不考虑线程冲突问题，用类似下面的代码去做，则很可能会**超额**完成任务，线程越多，完成任务次数超出100次的可能性就越大。

​		

​		线程安全的资源

如果大家经常看MSDN或者VS帮助中的.NET类库参考的话，就不难发现几乎所有的类型都有这么一句话的描述：“此类型的任何公共 static

![image-20220109164432593](https://chqwer2.github.io/img/Typora/image-20220109164432593.png)

如果现在有两个线程t1、t2，并且这两个线程中的run方法同时操作同一数据

看到，在最后出现了一个-1



1. Given the following sequences for two processes; What could go wrong? Explain what the effect would be and how it could occur **???????**
   1. Process 1:
      1. getLock A
      2. getLock C
      3. getLock B

   2. Process 2
      1. getLock C
      2. getLock B
      3. getLock A

      

The **GETLOCK** command is used when a user wants to perform a series of I/O operation commands without interruption. You may need to enter the **GETLOCK** command if another user ID has the **lock** and will not, or cannot, release it. Such a situation could arise, for example, if the other user’s terminal is inactive.



1. Suppose that two long-running processes, **P1 and P2**, are running in a system. Neither program performs any system calls that might cause it  to block, and there are no other processes in the system. P1 has 3  threads and P2 has 2 threads. The system may use either kernel or user  threads.
   1. What **percentage of CPU time will P1 get** if the threads are kernel threads? Briefly Explain.

      50 %

   2. What percentage of CPU time will P1 get if the threads are user threads? Briefly Explain.

      3/ 5

      A *kernel thread* is a thread object maintained by the operating  system. 

      It is an actual thread that is capable of being scheduled and  executed by the processor. 

      ![image-20220109172911256](https://chqwer2.github.io/img/Typora/image-20220109172911256.png)

      

      

2. Your friend Jane needs to run a simulation for her thesis and her  adviser wants her to run it for a fixed problem size. Jane can make 90%  of the program parallel, with 10% of it being sequential.
   1. What speedup can Jane expect on 10 processors?
   2. What would be the maximum speedup on an infinite number of processors?
   2. ![image-20211209173141384](https://chqwer2.github.io/img/Typora/image-20211209173141384.png)

![image-20211109150826677](https://chqwer2.github.io/img/Typora/image-20211109150826677.png)

## Concurrency

Deadlock

![image-20211109153302756](https://chqwer2.github.io/img/Typora/image-20211109153302756.png)

![image-20211109153522650](https://chqwer2.github.io/img/Typora/image-20211109153522650.png)

![image-20211109153641473](https://chqwer2.github.io/img/Typora/image-20211109153641473.png)

![image-20211109154116331](https://chqwer2.github.io/img/Typora/image-20211109154116331.png)

### Limited Resources

![image-20211111133153523](https://chqwer2.github.io/img/Typora/image-20211111133153523.png)

**Race condition**: muti-process or threads compete to write and write shared data items

How to avoid?

![image-20211209173926186](https://chqwer2.github.io/img/Typora/image-20211209173926186.png) 快速单元运算

![image-20220110194414569](https://chqwer2.github.io/img/Typora/image-20220110194414569.png)

Wrong when running concurrently

![image-20220110194445237](https://chqwer2.github.io/img/Typora/image-20220110194445237.png)

**Context switches may occur at any time....**

![image-20220110194546055](https://chqwer2.github.io/img/Typora/image-20220110194546055.png)

![image-20220110194622176](https://chqwer2.github.io/img/Typora/image-20220110194622176.png)

##### How to avoid?

We need to control the concurrent execution of the **critical sections** (Do the same writing or reading) or **critical code**(should be as small as possible)

Strict Serialization : **Mutual Exclusion**  

![image-20220110195037796](https://chqwer2.github.io/img/Typora/image-20220110195037796.png)

Mutual : Do now interact each other, not longer correct

![image-20211111134121875](https://chqwer2.github.io/img/Typora/image-20211111134121875.png)

![image-20211111135006771](https://chqwer2.github.io/img/Typora/image-20211111135006771.png)

Problems .... 

![image-20220110195903848](https://chqwer2.github.io/img/Typora/image-20220110195903848.png)

Both of them think they have got access to the logs, will still compete the lock

what we have to do is to use **atomic operations**? 

Atomic operations in concurrent programming are **program operations that run completely independently of any other processes**. Atomic operations are used in many modern operating systems and parallel processing systems.

![image-20220109171351480](https://chqwer2.github.io/img/Typora/image-20220109171351480.png)

![image-20220110195114274](https://chqwer2.github.io/img/Typora/image-20220110195114274.png)

Process A has X, Process B has Y, unable to complete this tasks - Deadlock

Process spending a long time fininsh the critical section - Starvation

![image-20220110195628563](https://chqwer2.github.io/img/Typora/image-20220110195628563.png)

`



### Use a token

![image-20211111135423434](https://chqwer2.github.io/img/Typora/image-20211111135423434.png)

![image-20211111135841128](https://chqwer2.github.io/img/Typora/image-20211111135841128.png)

### Hardware

![image-20211111135955174](https://chqwer2.github.io/img/Typora/image-20211111135955174.png)

![image-20211111141150811](https://chqwer2.github.io/img/Typora/image-20211111141150811.png)

If interuppted in Critical Zone, undo anything just done in critical area.

![image-20211111140945677](https://chqwer2.github.io/img/Typora/image-20211111140945677.png)

## Threads

![image-20211111145925723](https://chqwer2.github.io/img/Typora/image-20211111145925723.png)

![image-20211111150050979](https://chqwer2.github.io/img/Typora/image-20211111150050979.png)

![image-20211111150250948](https://chqwer2.github.io/img/Typora/image-20211111150250948.png)

##### Difference between User Level thread and Kernel Level thread

![image-20211209172530465](https://chqwer2.github.io/img/Typora/image-20211209172530465.png)

Benefits of Threads

![image-20211111150741855](https://chqwer2.github.io/img/Typora/image-20211111150741855.png)

![image-20211111151332705](https://chqwer2.github.io/img/Typora/image-20211111151332705.png)

![image-20211111151514022](https://chqwer2.github.io/img/Typora/image-20211111151514022.png)

![image-20211111151621484](https://chqwer2.github.io/img/Typora/image-20211111151621484.png)

N, f: parallel co

Parallel Challenges of Threads

A *kernel thread* is a thread object maintained by the operating  system. 

It is an actual thread that is capable of being scheduled and  executed by the processor. 

![image-20211111152750019](https://chqwer2.github.io/img/Typora/image-20211111152750019.png)

### Multithreading Models

[ref](https://cs.brown.edu/research/thmon/thmon2a.html)

![image-20211111153143617](https://chqwer2.github.io/img/Typora/image-20211111153143617.png)

One process has more than one threads

Cuz the threads mapping into one kernel thread

**One kernel thread will only run on one processor**

For kernels that do not support multiple threads of control, multithreading can be implemented entirely as a user-level library. These libraries, without the kernel's knowledge, schedule multiple threads of control onto the process's single kernel thread. Thus, just as a uniprocessor provides the illusion of parallelism by multiplexing multiple processes on a single CPU, user-level threads packages provide the illusion of parallelism by multiplexing multiple user threads on a single kernel thread; this is referred to as the *many-to-one* model [Kleiman et al. 1996].

![image-20211111153229845](https://chqwer2.github.io/img/Typora/image-20211111153229845.png)

For multi-core or processors for run in parallel

![image-20220104155902224](https://chqwer2.github.io/img/Typora/image-20220104155902224.png)

Costly and too heavy for the system

kernel is associated with the cores

![image-20211111153315920](https://chqwer2.github.io/img/Typora/image-20211111153315920.png)



![image-20211111153619628](https://chqwer2.github.io/img/Typora/image-20211111153619628.png)

**Locking** Machanism![image-20211111154609121](https://chqwer2.github.io/img/Typora/image-20211111154609121.png)

![image-20211111154634981](https://chqwer2.github.io/img/Typora/image-20211111154634981.png)
