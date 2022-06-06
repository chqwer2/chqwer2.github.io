### Hypothesis Test

![image-20220519173550521](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519173550521.png)

![image-20220519173600772](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220519173600772.png)



And so the significance level is how willing

we are to make a particular error,

namely the error of rejecting the null

hypothesis when the null hypothesis is true.



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521094154017.png" alt="image-20220521094154017" style="zoom:30%;" />

One-sided is usually more powerful than two-sided test:

![image-20220521094504059](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521094504059.png)

![image-20220521094640917](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521094640917.png)

##### There is a trade-off between type-I and type-2 error

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521094654521.png" alt="image-20220521094654521" style="zoom:33%;" />

****



### Fisher's Exact Test

ADV: Do not need to assume knowledge about the true **death proportion** among people

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521102309622.png" alt="image-20220521102309622" style="zoom:33%;" />



![image-20220521102454610](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521102454610.png)



### T Test and Z Test

Assume it is normality!

**Z test**

![image-20220521111812886](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521111812886.png)



![image-20220521111756101](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521111756101.png)

**T test** 

![image-20220521112824368](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521112824368.png)

Only difference we substitute the unknown variance with **empirical variance.**

with $n-1$ freedom.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521113833277.png" alt="image-20220521113833277" style="zoom:40%;" />

![image-20220521113751060](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521113751060.png)

This follow **T-distribution**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521113001984.png" alt="image-20220521113001984" style="zoom:25%;" />

![image-20220521113028357](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521113028357.png)

![image-20220521141805513](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521141805513.png)

### Confidence Interval

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521142008593.png" alt="image-20220521142008593" style="zoom:33%;" />

![image-20220521142041036](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521142041036.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521142050081.png" alt="image-20220521142050081" style="zoom:33%;" />

### Likelihood Ratio Test 

![image-20220521143336225](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521143336225.png)

**Distribution of Likelihood Ratio Test**

![image-20220521144237348](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521144237348.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521150703119.png" alt="image-20220521150703119" style="zoom:30%;" />

![image-20220521151641559](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220521151641559.png)

### Multiple testing issues

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220522153712081.png" alt="image-20220522153712081" style="zoom:40%;" />

5% significant level matters that we can expect 5 false significant results out of 100.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220522152333749.png" alt="image-20220522152333749" style="zoom:33%;" />

At least one false significant result

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220522152446615.png" alt="image-20220522152446615" style="zoom:33%;" />

FDR is less strict.

### Correction for Multiple Testing

**Bonferroni Correction**

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220522152807003.png" alt="image-20220522152807003" style="zoom:33%;" />

Too strong

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220522153135307.png" alt="image-20220522153135307" style="zoom:30%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220522153356107.png" alt="image-20220522153356107" style="zoom:33%;" />

### 