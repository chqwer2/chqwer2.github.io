# Week 3

Write Mnemonics and machine code 

![image-20220108180239786](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220108180239786.png)



### High Level to Low Level

![image-20211102193006618](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102193006618.png)

### Compilation, Interpretation & Overview of JVM

Compiled program (Cpp) faster than interpreted Program (Java)

<img src="C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102193912972.png" alt="image-20211102193912972" style="zoom:67%;" />

ARM != MIPS

![image-20211102194141622](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102194141622.png)

#### Interpretation 

![image-20211102194400500](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102194400500.png)

![image-20211102194602492](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102194602492.png)

### Combined Compilation & Interpretation

![image-20211102195115587](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102195115587.png)

Such as Java bytecode ( a.java -> a.class ) by javap

Compiled in CPU: javac, 

Java Rruntime Environment using JVM: java

![image-20211102195409359](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102195409359.png)

![image-20211102195421326](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102195421326.png)

### JVM

![image-20211102201321289](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102201321289.png)

![image-20211102201409733](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102201409733.png)

Java is portable due to VM, 

Interger JVM (IJVM)

![image-20211102201727128](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102201727128.png)

![image-20211102202045676](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102202045676.png)

![image-20211102202805962](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102202805962.png)

![image-20211102203055169](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102203055169.png)

![image-20211102203149251](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102203149251.png)

![image-20211102203238592](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102203238592.png)

slot number -> 0x01

### Interpreting JVM and Just In Time (JIT) Compilation

![image-20211102203759776](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102203759776.png)

![image-20211102203908050](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102203908050.png)

## Subroutines 子程序

![image-20211102204628407](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102204628407.png)

![image-20211102204807608](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102204807608.png)

![image-20211102204950122](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102204950122.png)

![image-20211102205143220](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102205143220.png)

![image-20211102205818854](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102205818854.png)

### Stack the Return Address

![image-20211102211241228](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102211241228.png)

![image-20211102211357426](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102211357426.png)

![image-20211102211548247](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102211548247.png)

![image-20211102211601296](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102211601296.png)

[b] get a value

![image-20211102212029428](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102212029428.png)

![image-20211102212042824](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102212042824.png)

Tips,

![image-20211102212233177](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102212233177.png)

### Stacks for Calculation

Reverse Polish Notation

![image-20211102212435484](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102212435484.png)

![image-20211102212456179](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102212456179.png)

![image-20211102212508980](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102212508980.png)

![image-20211102212745345](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102212745345.png)

![image-20211102212953159](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102212953159.png)

opcode 操作码

![image-20211102213128371](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102213128371.png)

![image-20211102213224218](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102213224218.png)

![image-20211102213303096](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102213303096.png)

![image-20211102213343099](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102213343099.png)

### Jump

![image-20211102214310536](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102214310536.png)

![image-20211102214327035](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20211102214327035.png)





### Floating-point number

![image-20220106145412035](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220106145412035.png)

**2’s complement notation**

![image-20220106145748037](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220106145748037.png)

