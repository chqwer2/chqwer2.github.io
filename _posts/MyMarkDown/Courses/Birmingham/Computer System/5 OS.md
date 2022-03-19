# Week5

**Why do we need an operating system?** 

The Need for Operating System: Operating System is a program that acts as an Interface between the system hardware and the user making the tasks easier. It is important software which runs on a computer and controls the set of instructions and wisely utilizes each part of the Computer.



**Exercise Questions:**

1. Based on the memory hierarchy diagram, what are the characteristics of memory hierarchy? Why they vary from one level to another? 

Several kinds of memory units.

Trade off between Speed and Capacity

[PDF]([Multilevel_Cache.pdf: Computer Systems (bham.ac.uk)](https://canvas.bham.ac.uk/courses/56091/files/11929478?wrap=1))

<img src="https://chqwer2.github.io/img/Typora/image-20211028205045939.png" alt="image-20211028205045939" style="zoom:50%;" />

2. What is the difference between device drivers and device controllers?

A device driver is a software  program that is used for running and operating the systems that interact with a part of a device in the computer. ... A device controller is a  hardware program that is used for attaching the OS of a computer and works in the phase by linking the device and the device driver



**Exercise Questions:**

\1. Which service is not provided by an OS?

  (a) File system manipulation                 (b) Memory management

  (c) Process scheduling                      **(d) Compilation of a program**

 **Following are the common services provided by an operating system:**

1. Program execution

2. I/O operations 

3. File system manipulation

4. Communication

5. Error detection

6. Resource allocation

7. Protection

   

\2. Why system programmers use APIs instead of system calls?

**using the API can be significantly easier than using the** actual system call.

**Portability**: Any program using that API can compile and run ,as long as the system/program supports the API.

**Ease of Use** *compared to actual system call*

**Also provides some form of **Security/Protection** *to the kernel because you are not interacting with the kernel*

***APIs provide some* **Efficiency

***It also provides a* **door/access *for services outside the system interact with the system internally.*



***3****. Explain the difference between a microkernel and a monolithic kernel,  provide one example of each of both architectures and briefly explain  the advantages and the limitations of the microkernel architecture.

Microkernel and monolithic kernel are two types of kernels. The difference between microkernel and monolithic kernel is that **the microkernel-based systems have OS services and kernel in separate  address spaces **

**while the monolithic kernel-based system has OS services and kernel in the same address space.**



### Storage Structure - Memory Hierarchy

CPU load Instructions only from memory

Memory (rewritable) includes Main memory and RAM (DRAM)

Read-only Memory (ROM),  EEPROM (Electrically Erasable Programmable)

#### How it works?

Each Byte has its own address

Disks (Programs sored and loaded from here)

![image-20211028172713267](https://chqwer2.github.io/img/Typora/image-20211028172713267.png)

<img src="https://chqwer2.github.io/img/Typora/image-20211028172736247.png" alt="image-20211028172736247" style="zoom: 50%;" />





### I/O Structure How the I/O devices function?

system BUS and I/O controller

<img src="https://chqwer2.github.io/img/Typora/image-20211028172949463.png" alt="image-20211028172949463" style="zoom:33%;" />

##### How it works?

Recall: Hardware may trigger an interrupt

SCSI Bus (Small Computer-Systems Interface)

### I/O Mechanisms

##### Programmed I/O (Polling)

![image-20211028192829716](https://chqwer2.github.io/img/Typora/image-20211028192829716.png)

### **Time wasting of CPU**

##### Interrupt Driven I/O

Fine for moving small amount of data

![image-20211028193026828](https://chqwer2.github.io/img/Typora/image-20211028193026828.png)

##### Direct Memory Access (DMA)

Deal with bulk data

![image-20211028193243174](https://chqwer2.github.io/img/Typora/image-20211028193243174.png)

Trigger only one Interrupt, CPU is freed

![image-20211028193356950](https://chqwer2.github.io/img/Typora/image-20211028193356950.png)

### Some General System Arch

#### Multiprocessor & Multicore

N (<N), not all benefit from fast execution.

Cost less - shared storage and power

Reliable: a failed processor will not stop the sys

![image-20211028193848278](https://chqwer2.github.io/img/Typora/image-20211028193848278.png)

![image-20211028193813888](https://chqwer2.github.io/img/Typora/image-20211028193813888.png)

##### Clustered System

![image-20211028194219696](https://chqwer2.github.io/img/Typora/image-20211028194219696.png)

### Operating System 

![image-20211028202416768](https://chqwer2.github.io/img/Typora/image-20211028202416768.png)

##### System Calls

![image-20211028202849904](https://chqwer2.github.io/img/Typora/image-20211028202849904.png)

Emulation 仿真

### Structure

![image-20211028203337374](https://chqwer2.github.io/img/Typora/image-20211028203337374.png)

Windows XP

![image-20211028203758681](https://chqwer2.github.io/img/Typora/image-20211028203758681.png)

![image-20211028203732126](https://chqwer2.github.io/img/Typora/image-20211028203732126.png)

Mac

![image-20211028204041576](https://chqwer2.github.io/img/Typora/image-20211028204041576.png)

![image-20211028204125178](https://chqwer2.github.io/img/Typora/image-20211028204125178.png)

### User Interfaces

Command Line Interface (CLI)

Batch Interface

Graphical User Interface (GUI)

![image-20211028204410204](https://chqwer2.github.io/img/Typora/image-20211028204410204.png)



### Additional Exercises

**Question #1:** What is an operating system?

 in 5.1

**Question #2:** Give examples of how we use an operating system in our daily routine?

Between you and hardware, make it easier to use

It's like your body. You operate everything (or mostly everything) without  really thinking about it. Without having to learn how to make a nerve  work or how to utilize energy, your body already has its operating  system to handle those low level functions for you.

**Question #3:** What are popular examples of operating systems?

 Win, Linux, Mac OS, IOS 

**Question #4:** Why do we need an operating system?

It manages the computer's memory and processes, as well as all of its software and hardware. It also allows you to  communicate with the computer without knowing how to speak the computer's language. Without an operating system, a computer is useless.

**Question #5:** How does the distinction between kernel mode and user mode function as a rudimentary form of protection (security) system?

The distinction provides a form of protection in the following manner. Certain instructions could be executed only when the CPU is in kernel mode. Similarly, hardware devices could be accessed only when the program is executing in kernel mode. Control over when interrupts could be enabled or disabled is also possible only when the CPU is in kernel mode. 

Consequently, **the CPU has very limited capability when executing in user mode**, thereby enforcing protection of critical resources.



**Question #6:** Which of the following instructions should be privileged?

**a) Set value of timer.**

b) Read the clock.

**c) Clear memory.**

d) Issue a trap instruction.

**e) Turn off interrupts.**

**f) Modify entries in device-status table.**

g) Switch from user to kernel mode.

**h) Access I/O device.**

 

**Question #7:** We have stressed the need for an operating system to make efficient use of the computing hardware. When is it appropriate for the operating system to forsake this principle and to “waste” resources? Why is such a system not really wasteful?



in single-user systems if user gets better interaction (improve the ease of use)

The other fact is single user requires less computer resources than multi-users

Single-user systems should maximize use of the system for the user. A  GUI might “waste” CPU cycles, but it optimizes the user’s interaction  with the system.

https://atisatech.wordpress.com/2015/07/06/introduction-to-operating-systems-questions-and-answers/



**Question #8:** What are the main differences between Batch operating systems and personal computers operating systems?

 The main difference between batch processing and multiprogramming is that batch processing allows multiple programs to execute with minimum human  interactions while multiprogramming allows multiple programs to execute  on a single processor system.

A computer system has an [operating system](https://pediaa.com/difference-between-operating-system-and-application-software/#Operating System) to manage the functionalities of the entire system. Moreover, different systems follow various methods to perform tasks. Batch processing and  multiprogramming are two of these methods.

**1. Batch Processing :**
A series of jobs are executed  without any human intervention in Batch processing system. In this set  of jobs with similar needs are batched together and inputted to the  computer for execution. It is also called as Simple Batch System. It is  slower in processing than Multiprogramming system.



**Question #9:** What is the difference between device drivers and device controllers?

A device driver is a software  program that is used for running and operating the systems that interact with a part of a device in the computer. ... A device controller is a  hardware program that is used for attaching the OS of a computer and works in the phase by linking the device and the device driver





 **Question #10:** Suppose that the processor has access to two levels of memory. **Level 1 contains 1000 bytes and has an access time of 0.1µs; level 2 contains 100,000 bytes and has an access time of 1µs.** Assume that if a byte to be accessed is in level 1, then the processor accesses it directly. If it is in level 2, then the byte i**s first transferred to level 1** and then accessed by the processor. For simplicity, we ignore the time required for the processor to determine whether the byte is in level 1 or level 2. Such a two-level memory can be shown as in the figure below:

![image-20211028211224738](https://chqwer2.github.io/img/Typora/image-20211028211224738.png)

We can define hit-ratio H, as the fraction of all memory **accesses that are found** in the faster memory e.g. the cache memory. T1 is the access time to level 1 (cache) and T2 is the access time to level 2 (main memory). Now **suppose 95% of the memory accesses are found in the cache (H=0.95).** Then what would be the average time to access **a byte** from such a two-level memory sub-system? Hint, the graph below shows the average access time to a two-level memory **as a function of the hit-ratio H.**





 ![image-20211028211242584](https://chqwer2.github.io/img/Typora/image-20211028211242584.png)



T1 = 0.1 mu, T2 = 1 mu + 0.1 mu

Access 1 byte of 0.95 H

T = T1 * 0.95 + 0.05 * 1.1 = 0.95 * 0.1 + 1.1 * 0.05 = 0.15 muS



**Exercise Questions: Based on what you have learnt so far:**

1. What is an operating system? Give examples of how we use an operating system in our daily routine.

2. Why do we need an operating system? 

**Exercise Question: How does the distinction between kernel mode and user mode function as a rudimentary form of protection (security) system?**

<img src="https://chqwer2.github.io/img/Typora/image-20211028211904417.png" alt="image-20211028211904417" style="zoom:40%;" />

### OS

<img src="https://chqwer2.github.io/img/Typora/image-20211028212447768.png" alt="image-20211028212447768" style="zoom:50%;" />

Monitor control the sequence of the events

Reboot computer : bootstrap program is loaded

##### Interrupts

A system call (software)

Interrupt Service Routine (ISR) : Interrupt handle



