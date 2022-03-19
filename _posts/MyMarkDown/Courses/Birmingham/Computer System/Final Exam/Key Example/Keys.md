### Paralleling

![image-20220104145135839](https://chqwer2.github.io/img/Typora/image-20220104145135839.png)

### CS 162

2021 Md1

**Registers** can only be modified by the kernel to ensure isolation and protection. If user can modify it, it would be able to access any physical address.

Each client connects to the same server **socket**, but reads/writes to a separate connection socket after the connection is accepted.

**Write** is buffered in the kernel. When write returns, the data may still be buffered in the kernel and the file may be unmodified

In **FIFO**, one thread can starve all other threads by running in an infinite loop. In **SRTF** and **MLFQS** w/ Fixed Priority Scheduling, short jobs can starve long jobs. In Round Robin, every thread is guaranteed an equal quantum.

**[Priority Inversion](https://www.digikey.co.uk/en/maker/projects/introduction-to-rtos-solution-to-part-11-priority-inversion/abf4b8f7cd4a4c70bece35678d178321)**, is a bug that occurs when a high priority task is indirectly preempted by a low priority task. For example, the low priority task holds a mutex that the high priority task must wait for to continue executing.

![Bounded priority inversion timing diagram](https://www.digikey.co.uk/maker-media/e2e5ff51-f966-42c5-93d8-b77590e2c10b)

**Unbounded priority inversion**

occurs when a **medium** priority task (Task M) interrupts Task L while it holds the lock. It’s called “unbounded” because Task M can now effectively block Task H for any amount of time, as Task M is preempting Task L (which still holds the lock).

![Unbounded priority inversion timing diagram](https://www.digikey.co.uk/maker-media/92b5e015-d9fc-4940-9a48-f814d06c5f31)

##### Thread

**Why Thread?**

3 points for each of two reasons. Many reasons, including:
?  More efficient operation: overlap I/O and computation
?  **Easier to share data** between threads in the same address
space than between processes
?  **Modularity**: A complex task can be decomposed into smaller
pieces
?  Reduced latency on multiprocessors
?  Faster to switch between threads than between processes
We did not give credit for saying that threads give you concurrency, since processes also provide concurrency.

**Changing State **\ref(cs162_fa99_mt1_sol)

![image-20220111223447097](https://chqwer2.github.io/img/Typora/image-20220111223447097.png)



List two reasons why **overuse of threads** is bad (i.e., using too many threads for different tasks). Be explicit in your answers.
![image-20220111222001350](https://chqwer2.github.io/img/Typora/image-20220111222001350.png)

![image-20220111222045484](https://chqwer2.github.io/img/Typora/image-20220111222045484.png)





**Kernel**:

The MMU is always active(Memory Management Unit) and used to translate virtual addresses to physical addresses. Interrupts may be selectively disabled in kernel mode

Whenever **Thread** A enters a “**waiting” state** (because, for example, it is blocked on I/O), the OS must schedule the idle thread since there are no other threads that are ready to run

David makes sure to correctly validate that every argument on the stack is in the user process’s virtual address space.,In addition, when a buffer pointer is passed in as a syscall argument, he makes sure to check that the first byte and last byte of the buffer are valid. :  You can cause the kernel to crash. This is because the kernel will attempt to access addresses in between the **heap** and the stack, which are not allocated.

**Overhead of multithreading** (e.g. context switching, thread creation) synchronization can cause a **multithreaded program to run slower** than a single threaded program, especially on a single core machine where the threads would concurrently instead of in parallel. If the multithreaded program requires synchronization, a large critical section may result in threads being run sequentially instead of in parallel.

**Connections**:

Each connection is uniquely identified by a 5-tuple: Source IP, Destination IP, **Source Port,** Destination Port, and Protocol.

**Process**

(i) Waiting for data to be read from a disk. Blocked
(ii) Spin-waiting for a lock to be released. Running
(iii) Having just called wait() on a condition variable in a monitor. Blocked
(iv) Having just completed an I/O and waiting to get scheduled again on the CPU. Ready



Fall21 MT2

**Deadlock**:

An unsafe state mean that there is an order of requests that leads to deadlock,  but there can be orders of requests that don't lead to deadlock.

A deadlock can occur with resources such as memory or sockets.

Deadlock is a form of starvation with a stronger condition where threads fail to make progress due to cyclical waiting.

In most modern operating systems, the number of processes is not fixed and total amount of resources used for each process is unknown, making implementing **Banker’s algorithm** impossible.

This **routine** is (iii) dangerous (correct answer worth 3 points) for three reasons
(each reason is worth 3 points):

1. Deadlock could occur because there is no resource ordering during lock acquisition.
2. The routine fails to release the locks if either stack is empty.
3. The routine does not leave stack1 unchanged if stack two is empty (it fails to repush thing1). ?????..
4. Some code example in [fa99](C:\MyMarkDown\Courses\Birmingham\Computer System\Final Exam\Key Example/cs162_fa99_mt1_sol.pdf)

##### Concurrency







**Process Trashes**

The main reason performance degrades when a process trashes is due to frequent page faults, as the process’ working set does not fit in the memory.

SRTF can starve if many small jobs run, preventing large jobs from running.

![image-20220111155543301](https://chqwer2.github.io/img/Typora/image-20220111155543301.png)

**I/O**

Direct memory access (DMA) programs the device controller to transfer directly to memory via the bus.

PCI Express (bus) can handle multiple requests at at time. PCI can only handle one single request at a time.

A blocking I/O operation leads to the process being suspended until the operation completes.

Port mapped I/O uses in/out instructions to read/write to ports

With a memory-mapped display controller a process can write directly to the display buffer (also called frame buffer)

The time it takes for the desired sector to move under the disk head. is the **rotation time**. **Seek time** is the time it takes to locate the correct track.

Copy-on-write enable SSDs to reduce the write overhead. (开销)

Copy-on-write avoids the overhead of the **erasure operation** which is much more expensive than a write operation, by writing the updates to an empty page.

**Schedule**

RR is the fairest scheduler with regards to wait time for CPU.

FCFS has throughput at least as good as RR.

![image-20220111170034525](https://chqwer2.github.io/img/Typora/image-20220111170034525.png)

Questions:

What is **context switching**?
Sample Answer:
Context switching is when the kernel switches the CPU from one process to another. This requires the
kernel to save the state of the currently running process in the PCB.



What is the **timer interrupt**? And how does the OS use it for **scheduling**?
Sample Answer:
Most computers have hardwre clocks (or timers) that generate periodic interrupts. These interrupts are
known as the timer interrupts. The OS uses the timer interrupt to measure the passage of time and
determine when the quantum of a running process has expired, at which point the process is preempted.
The timer interrupt also ensures that the kernel will get the CPU back from a running process so that it
can make scheduling decisions.



Why is **Least Recently Used (LRU)** considered to be impractical for use as a replacement policy in virtual memory systems?
Sample Answer:
Because it requires an LRU list or a per-page last access time stamp to be updated by the MMU with every memory access. This is prohibitively expensive.



In **virtual memory systems**, why is replacing a clean page faster than replacing a dirty page?
Sample Answer:
When the OS replaces a dirty page, it has to write this page to the swap disk. A clean page can be
replaced without writing it to the swap disk.

List one factor that favours having larger **virtual memory pages** and one factor that favours having smaller
pages.
Sample Answer:
Factors favouring large pages: smaller page tables, fewer entries in the TLB needed to cover the same
amount of memory, more ecient I/O to swap pages in.
Factors favouring small pages: reduced internal fragmentation, less likely to page in unnecessary data.



Brie
y describe how the operating system gets loaded into memory and starts executing when the machine is powered up (also known as \booting" the operating system).
Sample Answer:

1. CPU starts executing instructions from a known location in memory when it is powered up.
2. That location is in ROM, and it has a simple program that loads a \bootstrap program" from a xed
location on disk and starts executing this bootstrap program.
3. The bootstrap program initializing the system (registers, memory, devices), and loads the full operating
system into memory and start executing it.

Kernel runtime and User Runtime

![image-20220111173505398](https://chqwer2.github.io/img/Typora/image-20220111173505398.png)

Process waiting for a **lock** to be released, busy waiting better than blocking

![image-20220111173918324](https://chqwer2.github.io/img/Typora/image-20220111173918324.png)

**CPU efficiency** and Speedup

Program B is best because its sequential overhead is not growing, and therefore going to larger numbers of processors it will have better speedups.



Question 5. A parallel program is run on 1, 2, 4, 8, 16 and 32 cores, and we get the following speedups
and efficiency.
![image-20220111182515318](https://chqwer2.github.io/img/Typora/image-20220111182515318.png)
The speedup for 4 processors is greater than 4, and the efficiency is greater than 1. The amount of
computation is the same as in the sequential version. We can conclude that the super-linear speedup is
the result of (circle the correct answer.)
(a) More cache misses because of poor locality
(b) Fewer cache misses because of good locality
(c) Fewer cache misses because of more cache available on four cores than two, and
sufficiently good locality to take advantage of this.
(d) Good programming, and the progra

**expected speedup on 20 processors?**

Speedup = P + (1-P) s
= 20 ? 19 * 0.01 = 19.81
Full credit was given for setting up the problem.

![image-20220111212229085](https://chqwer2.github.io/img/Typora/image-20220111212229085.png)

CPU executes, multiple **Processors**



**Lack of Speed Up of multi-processors**

The lack of speedup is entirely caused by inherently parallel portions of the algorithm
The lack of speedup is caused, at least in part, by overheads that increase with the
machine size
Karp-Flatt analysis is not useful for diagnosing the cause of performance issues when
executing on increasing numbers of processors.

The program still has a race and the race slows down the program.
The program does not get any speedup because the critical pragma only allows one
iteration to execute the body of the loop at a time.
The program could have used an OpenMP reduction to achieve the same result and
have been faster.



**TTL, Isoefficiency**

![image-20220111181559146](https://chqwer2.github.io/img/Typora/image-20220111181559146.png)

![image-20220111182226819](https://chqwer2.github.io/img/Typora/image-20220111182226819.png)

its sequential **overhead**  == time



