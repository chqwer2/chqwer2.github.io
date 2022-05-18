# pRandom / Stochastic Process

### The Bernoulli Process

Can be model of incoming randomly tasks:

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220421093523776.png" alt="image-20220421093523776" style="zoom:50%;" />

Stochastic:

Infinite sequence  

Outcomes will diff each time

**Finite Defined Joint Probability**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220421094455243.png" alt="image-20220421094455243" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220421094905922.png" alt="image-20220421094905922" style="zoom:50%;" />

Some cases don’t have fresh-start properties



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220421095217150.png" alt="image-20220421095217150" style="zoom:50%;" />

### Example: The distribution of a busy period

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220422143247348.png" alt="image-20220422143247348" style="zoom:50%;" />

### The time of the kth arrival

K sucess

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220422143842721.png" alt="image-20220422143842721" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220422144158069.png" alt="image-20220422144158069" style="zoom:50%;" />

### Merging of Bernoulli processes

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220422144450126.png" alt="image-20220422144450126" style="zoom:50%;" />

Z = Ber(p+q-pq)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220422144903582.png" alt="image-20220422144903582" style="zoom:50%;" />
$$
Z = g(x, y)
$$

### Splitting a Bernoulli process

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220422145208253.png" alt="image-20220422145208253" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220422145314872.png" alt="image-20220422145314872" style="zoom:50%;" />

Ber(qp) and Ber(p(1-q))

### The Poisson approximation to the Binomial

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220422145739582.png" alt="image-20220422145739582" style="zoom:50%;" />

Binomial PMF converge to Poisson PMF when taking limitation



# Poisson Process

Numbers of incoming arrival is irrelavant,

 <img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423092718064.png" alt="image-20220423092718064" style="zoom:50%;" />

Some application

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423093013510.png" alt="image-20220423093013510" style="zoom:50%;" />

Bernoulli gets only 0 or 1 arrival at a time slot, Poisson gets arbitrary arrival.

From Bernoulli and Binomial to Poisson

![image-20220423093747588](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423093747588.png)

Mean and variance

![image-20220423094110580](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423094110580.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423094410413.png" alt="image-20220423094410413" style="zoom:50%;" />



### Time of the kth arrival

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423094603979.png" alt="image-20220423094603979" style="zoom:50%;" />

Memoryless property

K-th Arrival

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423095156570.png" alt="image-20220423095156570" style="zoom:50%;" />

### The fresh start property and its implications

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423100119630.png" alt="image-20220423100119630" style="zoom:50%;" />



# Summary of results

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423100245650.png" alt="image-20220423100245650" style="zoom:50%;" />

Sum of Exponential  is called Erlang

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423163239450.png" alt="image-20220423163239450" style="zoom:50%;" />

![image-20220423164126271](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423164126271.png)

### An example

​      ![image-20220423100711567](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423100711567.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423100829419.png" alt="image-20220423100829419" style="zoom:50%;" />

![image-20220423101123176](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423101123176.png)



### Sum of independent Poisson random variables

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423212157841.png" alt="image-20220423212157841" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423212910752.png" alt="image-20220423212910752" style="zoom:50%;" />

### The time until the first (or last) lightbulb burns out

![image-20220423213622944](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423213622944.png)

![image-20220423213637801](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423213637801.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423213909628.png" alt="image-20220423213909628" style="zoom:50%;" />

![image-20220423214028574](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423214028574.png)

![image-20220428115800645](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220428115800645.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423214350357.png" alt="image-20220423214350357" style="zoom:50%;" />

![image-20220423215134570](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423215134570.png)

**Why this bias?** 

When you show up at a certain time, like 12 noon,

you're more likely to fall inside a large interarrival

interval rather than a smaller interarrival interval.

So just the fact that you're showing up

at a certain time that's uncoordinated

with the rest of the process makes

you more likely to be biased towards longer

rather than shorter intervals.

![image-20220423215716682](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423215716682.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423215945109.png" alt="image-20220423215945109" style="zoom:50%;" />

![image-20220423220354180](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423220354180.png)



With time span, so it is a exp distribution

![image-20220424101514392](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220424101514392.png)

![image-20220424101527371](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220424101527371.png)

![image-20220428110957639](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220428110957639.png)



Waiting to be addressed

https://learning.edx.org/course/course-v1:MITx+6.431x+1T2022/block-v1:MITx+6.431x+1T2022+type@sequential+block@Problem_Set_9/block-v1:MITx+6.431x+1T2022+type@vertical+block@ch13-s7-tab3

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220428114856893.png" alt="image-20220428114856893" style="zoom:50%;" />

![image-20220428133207636](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220428133207636.png)

![image-20220428144601090](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220428144601090.png)

![image-20220428150516109](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220428150516109.png)

# Poisson process practice

![image-20220508214232248](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508214232248.png)

replace with new A/B bulb.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508214610424.png" alt="image-20220508214610424" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508214904712.png" alt="image-20220508214904712" style="zoom:50%;" />

e,f passed

![image-20220508215704525](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508215704525.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508220336367.png" alt="image-20220508220336367" style="zoom:50%;" />

![image-20220508220451851](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508220451851.png)