# Deadlocks & Network

[Week08_Additional_Questions_Solutions_I (1).pdf](file:///C:/Users/calvchen/Downloads/Week08_Additional_Questions_Solutions_I (1).pdf)

[Week08_Additional_Questions_Solutions_II (1).pdf](file:///C:/Users/calvchen/Downloads/Week08_Additional_Questions_Solutions_II (1).pdf)

## Deadlocks 

Processes block each other

![image-20211203142435110](https://chqwer2.github.io/img/Typora/image-20211203142435110.png)

![image-20211203142524708](https://chqwer2.github.io/img/Typora/image-20211203142524708.png)

None of the process can proceed

![image-20211203142747181](https://chqwer2.github.io/img/Typora/image-20211203142747181.png)

Two process is holding one resource and ask for another one

![image-20211203143455300](https://chqwer2.github.io/img/Typora/image-20211203143455300.png)

### Reusable Resources

Used by only one process at a time and not depleted by that use...

![image-20211203144330062](https://chqwer2.github.io/img/Typora/image-20211203144330062.png)

![image-20211203144416451](https://chqwer2.github.io/img/Typora/image-20211203144416451.png)

![image-20211203150241078](https://chqwer2.github.io/img/Typora/image-20211203150241078.png)

### What is a deadlock

![image-20211203150355482](https://chqwer2.github.io/img/Typora/image-20211203150355482.png)

**No Efficient Solution!**

![image-20211203150547301](https://chqwer2.github.io/img/Typora/image-20211203150547301.png)

Not Necessary Enough now! But when happend cannot be resolved

![image-20211203150645764](https://chqwer2.github.io/img/Typora/image-20211203150645764.png)

Lead to Deadlock...

### Resource Allocation Graphs

![image-20211203150756285](https://chqwer2.github.io/img/Typora/image-20211203150756285.png)

![image-20211203150830199](https://chqwer2.github.io/img/Typora/image-20211203150830199.png)

Multi resources ??

![image-20211203151018632](https://chqwer2.github.io/img/Typora/image-20211203151018632.png)

![image-20211203151136302](https://chqwer2.github.io/img/Typora/image-20211203151136302.png)

### Deadlock Prevention

![image-20211203151944629](https://chqwer2.github.io/img/Typora/image-20211203151944629.png)

  **More details..**

![image-20211203152406682](https://chqwer2.github.io/img/Typora/image-20211203152406682.png)

???? here

![image-20211203153016768](https://chqwer2.github.io/img/Typora/image-20211203153016768.png)

Try to preempt 抢占 only with the process can be saved and restored..

Ask the first process to release the resources

Context Switching! 

 ![image-20211203153442006](https://chqwer2.github.io/img/Typora/image-20211203153442006.png)

### Deadlock Avoidance

![image-20211203153939050](https://chqwer2.github.io/img/Typora/image-20211203153939050.png)

![image-20211203153926528](https://chqwer2.github.io/img/Typora/image-20211203153926528.png)

![image-20211203154757929](https://chqwer2.github.io/img/Typora/image-20211203154757929.png)

![image-20211203155213909](https://chqwer2.github.io/img/Typora/image-20211203155213909.png)

 ![image-20211203160101600](https://chqwer2.github.io/img/Typora/image-20211203160101600.png)

![image-20211203160132637](https://chqwer2.github.io/img/Typora/image-20211203160132637.png)

P2 can be processed to finish   -- Safe State![image-20211203160704166](https://chqwer2.github.io/img/Typora/image-20211203160704166.png)

Unsafe State: **Don't grant this request**

![image-20211203161050781](https://chqwer2.github.io/img/Typora/image-20211203161050781.png)

Synchronize同步

### Deadlock Detection (Algo)

![image-20211203162451998](https://chqwer2.github.io/img/Typora/image-20211203162451998.png)

![image-20211203162547304](https://chqwer2.github.io/img/Typora/image-20211203162547304.png)

Abort all the resources involved in to the Deadlock

Or abort one by one to see if the deadlock resolved...

![image-20211203163223769](https://chqwer2.github.io/img/Typora/image-20211203163223769.png)

![image-20211203163516048](https://chqwer2.github.io/img/Typora/image-20211203163516048.png)

![image-20211203163624992](https://chqwer2.github.io/img/Typora/image-20211203163624992.png)

![image-20211203164102820](https://chqwer2.github.io/img/Typora/image-20211203164102820.png)





# Part2 Networks

**Question:** Suppose there is exactly one packet switch between a sending host and a  receiving host. The transmission rates between the sending host and the  switch and between the switch and the receiving host are R1 and R2, respectively. Assuming that the switch uses store-and-forward packet switching, what is the total end-to-end delay to send a packet of length L? (Ignore queuing, propagation delay, and processing delay). 

[Discuss it on MS Teams]

**Question:** What advantages does a circuit-switched network have over a packet-switched network?

[Discuss it on MS Teams]

**Question:** Suppose users share a 2Mbps link. Also suppose each user transmits continuously at 1 Mbps when transmitting, but each user transmits only 20 percent of the time. 

**a)** When circuit-switching is used, how many users can be supported? 

[Discuss it on MS Teams]

b) When packet-switching is used, why will there be essentially no queuing delay before the link if two of fewer users transmit at the same time?  Why will there be a queuing delay if three users transmit at the same  time?

[Discuss it on MS Teams]

**Question:** Consider an application that transmits data at a steady rate (for example, the  sender generates an N-bit unit of data every k time units, where k is  small and fixed). Also, when such an application starts, it will  continue running for a relatively long period of time. Answer the  following questions, briefly justifying your answers:
**a)** Would a packet-switched network or a circuit-switched network be more appropriate for this application? Why?

[Discuss it on MS Teams]

**b)** Suppose that a  packet-switched network is used and the only traffic in this network  comes from such applications as described above. Furthermore, assume  that the sum of the application data rates is less than the capacities  of each and every link. Is some form of congestion control needed? Why?

**Question:** Why will two ISPs at the same level of the hierarchy often peer with each other? How does an IXP earn money? 

[Discuss it on MS Teams]

**Question:** Why is a content provider considered a different Internet entity today? How does a content provider connect to other ISPs? Why?

[Discuss it on MS Teams]

 

**Solutions to the above Exercises are available [HERE](https://canvas.bham.ac.uk/courses/56091/files/12020391/download).**



**What is the Internet?**

![image-20211203172709118](https://chqwer2.github.io/img/Typora/image-20211203172709118.png)

<img src="https://chqwer2.github.io/img/Typora/image-20211203173052523.png" alt="image-20211203173052523" style="zoom:67%;" />

![image-20211203173201327](https://chqwer2.github.io/img/Typora/image-20211203173201327.png)

bandwidth: bit per second (bps)

Network core = interconnected routers

![image-20211203173739598](https://chqwer2.github.io/img/Typora/image-20211203173739598.png)

![image-20211203174304896](https://chqwer2.github.io/img/Typora/image-20211203174304896.png)

### Distributed Systems

![image-20211206212348230](https://chqwer2.github.io/img/Typora/image-20211206212348230.png)

![image-20211206212611780](https://chqwer2.github.io/img/Typora/image-20211206212611780.png)

![image-20211206212802253](https://chqwer2.github.io/img/Typora/image-20211206212802253.png)

![image-20211207221717676](https://chqwer2.github.io/img/Typora/image-20211207221717676.png)

### Network Principle

Latency = any kind of delay

Bandwidth = transmission capacity

![image-20211207232708797](https://chqwer2.github.io/img/Typora/image-20211207232708797.png)

![image-20211207232850410](https://chqwer2.github.io/img/Typora/image-20211207232850410.png)

![image-20211207233248435](https://chqwer2.github.io/img/Typora/image-20211207233248435.png)

![image-20211207233401597](https://chqwer2.github.io/img/Typora/image-20211207233401597.png)

### Network Structure

ISPs

![image-20211207233847658](https://chqwer2.github.io/img/Typora/image-20211207233847658.png)

IXP - internet change point

![image-20211207234218649](https://chqwer2.github.io/img/Typora/image-20211207234218649.png)







#### Word

appliance 电器