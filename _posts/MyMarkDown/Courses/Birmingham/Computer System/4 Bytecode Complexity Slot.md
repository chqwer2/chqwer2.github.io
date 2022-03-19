# Week 4 JVM, Bytecode and Complexity

## JVM

Different of JVM, JRE and JDK?

<img src="https://chqwer2.github.io/img/Typora/image-20211102231525609.png" alt="image-20211102231525609" style="zoom:40%;" />

**JVM**: load, verify, excute and provide runtime env

**JRE**: implementation of JVM + lib and other files

**JDK**: physicly exist kit

![image-20211102230631640](https://chqwer2.github.io/img/Typora/image-20211102230631640.png)



![image-20211102230956963](https://chqwer2.github.io/img/Typora/image-20211102230956963.png)

<img src="https://chqwer2.github.io/img/Typora/image-20211102231134975.png" alt="image-20211102231134975" style="zoom: 46.5%;" />

## Stack Frames

Call a method...

![image-20211102231725740](https://chqwer2.github.io/img/Typora/image-20211102231725740.png)

![image-20211102232040507](https://chqwer2.github.io/img/Typora/image-20211102232040507.png)

![image-20211102232142696](https://chqwer2.github.io/img/Typora/image-20211102232142696.png)

Inside the Constructor.

![image-20211102232519631](https://chqwer2.github.io/img/Typora/image-20211102232519631.png)

### **Slot Number**

![image-20211102232714833](https://chqwer2.github.io/img/Typora/image-20211102232714833.png)

![image-20211103084558161](https://chqwer2.github.io/img/Typora/image-20211103084558161.png)

Include the length of the value

![image-20211103084605654](https://chqwer2.github.io/img/Typora/image-20211103084605654.png)

![image-20220109113553224](https://chqwer2.github.io/img/Typora/image-20220109113553224.png)

![image-20211103084846731](https://chqwer2.github.io/img/Typora/image-20211103084846731.png)

### Big/ Little - Endian

Big endian- high-order byte is stored on the starting address (A) 

![image-20220109113842666](https://chqwer2.github.io/img/Typora/image-20220109113842666.png)

## Bytecode Instruction

![image-20211103085201385](https://chqwer2.github.io/img/Typora/image-20211103085201385.png)

**Val1 and Val2 are the top two stack entries**

The most significant byte stored in the opposite site..

![image-20211103085529880](https://chqwer2.github.io/img/Typora/image-20211103085529880.png)

![image-20211103085945127](https://chqwer2.github.io/img/Typora/image-20211103085945127.png)

![image-20211103085956123](https://chqwer2.github.io/img/Typora/image-20211103085956123.png)

##### operand 操作数

![image-20211103090208797](https://chqwer2.github.io/img/Typora/image-20211103090208797.png)

most commonly used

![image-20211103090400624](https://chqwer2.github.io/img/Typora/image-20211103090400624.png)

![image-20211103090527316](https://chqwer2.github.io/img/Typora/image-20211103090527316.png)

**save some spaces in the bytecode**

![image-20211103091018250](https://chqwer2.github.io/img/Typora/image-20211103091018250.png)

![image-20211103091109960](https://chqwer2.github.io/img/Typora/image-20211103091109960.png)

([Week 4 Exercises.pdf](file:///C:/Users/calvchen/Downloads/Week 4 Exercises.pdf))

![image-20220109120207282](https://chqwer2.github.io/img/Typora/image-20220109120207282.png)

## Call & Return

![image-20211103091746578](https://chqwer2.github.io/img/Typora/image-20211103091746578.png)

![image-20211103091925278](https://chqwer2.github.io/img/Typora/image-20211103091925278.png)

![image-20211103092249530](https://chqwer2.github.io/img/Typora/image-20211103092249530.png)

![image-20211103092305013](https://chqwer2.github.io/img/Typora/image-20211103092305013.png)

![image-20211103092544431](https://chqwer2.github.io/img/Typora/image-20211103092544431.png)

### Runtime Constant Pool

![image-20211103092703224](https://chqwer2.github.io/img/Typora/image-20211103092703224.png)

![image-20211103092711429](https://chqwer2.github.io/img/Typora/image-20211103092711429.png)

![image-20211103092903656](https://chqwer2.github.io/img/Typora/image-20211103092903656.png)

![image-20211103092947531](https://chqwer2.github.io/img/Typora/image-20211103092947531.png)

![image-20211103093029186](https://chqwer2.github.io/img/Typora/image-20211103093029186.png)

![image-20211103093034263](https://chqwer2.github.io/img/Typora/image-20211103093034263.png)

## Recursion

![image-20211103093309467](https://chqwer2.github.io/img/Typora/image-20211103093309467.png)

![image-20211103093451593](https://chqwer2.github.io/img/Typora/image-20211103093451593.png)

![image-20211103093501830](https://chqwer2.github.io/img/Typora/image-20211103093501830.png)

### Java Disassembler (Javap)

![image-20211103093835413](https://chqwer2.github.io/img/Typora/image-20211103093835413.png)

![image-20211103093934348](https://chqwer2.github.io/img/Typora/image-20211103093934348.png)

![image-20211103093953345](https://chqwer2.github.io/img/Typora/image-20211103093953345.png)

![image-20211103094145776](https://chqwer2.github.io/img/Typora/image-20211103094145776.png)

![image-20211103094315494](https://chqwer2.github.io/img/Typora/image-20211103094315494.png)

![image-20211103094346100](https://chqwer2.github.io/img/Typora/image-20211103094346100.png)

![image-20211103094725591](https://chqwer2.github.io/img/Typora/image-20211103094725591.png)

![image-20211103094735151](https://chqwer2.github.io/img/Typora/image-20211103094735151.png)

![image-20211103095344172](https://chqwer2.github.io/img/Typora/image-20211103095344172.png)

## Complexity

About runtime?

https://stackoverflow.com/questions/4915842/difference-between-time-complexity-and-running-time

access the data... cache like that





Big O Notation

[Corrected exercises: time complexity - Complex systems and AI (complex-systems-ai.com)](https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/)

我们常用大O表示法表示时间复杂性，注意它是某一个算法的时间复杂性。大O表示只是说有上界，

以上三条单个语句的频度均为1，该程序段的执行时间是一个与问题规模n无关的常数。算法的时间复杂度为常数阶，记作T(n)=O(1)。如果算法的执行时 间不随着问题规模n的增加而增长，即使算法中有上千条语句，其执行时间也不过是一个较大的常数。此类算法的时间复杂度是O(1)。 

O(n^2)

2.1. 交换i和j的内容

```
     sum=0；                 （一次）
     for(i=1;i<=n;i++)       （n次 ）
        for(j=1;j<=n;j++) （n^2次 ）
         sum++；       （n^2次 ）1234
```

解：T(n)=2n^2+n+1 =O(n^2)

定义：如果一个问题的规模是n，解这一问题的某一算法所需要的时间为T(n)，它是n的某一函数 T(n)称为这一算法的“时间复杂性”。



![image-20220110145414341](https://chqwer2.github.io/img/Typora/image-20220110145414341.png)
