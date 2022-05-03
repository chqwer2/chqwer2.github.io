# Lecture 5

Discrete r.v.

![image-20220228101700086](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228101700086.png)

### Define r.v.: the formalism

A function from the sample space $\Omega$ to the real numbers

![image-20220228102412906](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228102412906.png)

Some outcomes are more likely than others:

PMF (Probability mass functions):

![image-20220228103042911](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228103042911.png)

Accross all the sample space 

### Expectation/ Mean of a random variable

![image-20220228110512639](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228110512639.png)

![image-20220228111233512](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228111233512.png)

![image-20220228111353921](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228111353921.png)

![image-20220228111429069](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228111429069.png)

### Variance:

![image-20220228112005260](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228112005260.png)

![image-20220228112012441](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228112012441.png)

![image-20220228112042661](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228112042661.png)

![image-20220228112350134](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228112350134.png)

![image-20220228112552379](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228112552379.png)

### Conditional PMFs

![image-20220228112936135](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228112936135.png)

### Total expectation theorem

An important reason why conditional probabilities are

very useful is that they allow us to divide and conquer.

![image-20220228113407992](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228113407992.png)

<img src="C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228113441075.png" alt="image-20220228113441075" style="zoom:50%;" />

### Geometric PMF, memorylessness, and expectation

usually called Memorylessness.

Ultimately, this property has to do with the fact that

independent coin tosses do not have any memory.

Past coin tosses do not affect future coin tosses.

![image-20220228113949353](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228113949353.png)

Conditional P is equal to unconditional P in Geom distribution

The mean of the geometric:

<img src="C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228114257704.png" alt="image-20220228114257704" style="zoom:33%;" />

But it is hard to calculate, so we break down the senario

![image-20220228114645405](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228114645405.png)

So we can solve this equation.

### Joint PMFs and the expected value rule

we will need information that tells us what values of X tend to occur together with what values of Y. 

![image-20220228143447380](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228143447380.png)

<img src="C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228143645988.png" alt="image-20220228143645988" style="zoom:50%;" />

![image-20220228143735550](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228143735550.png)

<img src="C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228143841049.png" alt="image-20220228143841049" style="zoom:67%;" />

<img src="C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228145450230.png" alt="image-20220228145450230" style="zoom: 67%;" />

![image-20220228145456003](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228145456003.png)

![image-20220228145613141](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228145613141.png)

# Linearity of expectations and the mean of the binomial

![image-20220228150043461](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228150043461.png)

### Conditional PMFs

![image-20220228150758504](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228150758504.png)

So what we're really dealing with in this instance is that we have a family of conditional PMFs, one conditional PMF for every possible value of little y.

![image-20220228151040442](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228151040442.png)

### Conditional expectation and the total expectation theorem

![image-20220228151641777](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228151641777.png)

![image-20220228152700706](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228152700706.png)

![image-20220228152708367](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228152708367.png)

![image-20220228153234150](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228153234150.png)

In the real world, independence models situations

where each of the random variables is generated in a

decoupled manner, in a separate probabilistic

experiment.

And these probabilistic experiments do not interact

with each other and have no common sources of uncertainty.

![image-20220228160339980](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228160339980.png)

![image-20220228160615878](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228160615878.png)

### The hat problem

![image-20220228161628762](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228161628762.png)

Calculating this quantity, the PMF of X, is difficult.

And it is difficult because there is no simple expression

that describes the k factorials.



The trick that we will use is to employ indicator variables.

![image-20220228161904317](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228161904317.png)

More generally, if I were to tell you that the first n

minus 1 people got their own hats back, then the last

remaining person will have his or her own hat

available to be picked.

That's going to be the only available hat.

And then person n we also get their hat back.

So we see that the information about some of the Xi's gives

us information about the remaining Xn.

And again, this means that the random

variables are dependent.

**To calculate variance:**

![image-20220228162546194](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228162546194.png)
$$
X^2 = \sum X_i^2 + \sum X_iX_j\ (i\neq j)
$$
And then we get cross terms, such as X1 times X2, X1 times

![image-20220228162752413](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228162752413.png)

### Solved Problem

Tail probability is just adding up probabilities in the tail:
$$
P(X\geq k)
$$
![image-20220228165142027](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228165142027.png)

<img src="C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228165358338.png" alt="image-20220228165358338" style="zoom:33%;" />

<img src="C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228165459422.png" alt="image-20220228165459422" style="zoom:33%;" />

Change the direction

![image-20220228165529771](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228165529771.png)

Why? because tail probabilities sometimes easier to compute.

![image-20220228170025873](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228170025873.png)

![image-20220228165943501](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228165943501.png)

### Coupon Collector Problem

![image-20220228170123169](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228170123169.png)

![image-20220228170208775](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228170208775.png)

$i$ will be how many kinds of grades we have seen.

![image-20220228170332088](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228170332088.png)

<img src="C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228170417640.png" alt="image-20220228170417640" style="zoom: 50%;" />

each X is a Geometric distirbution with (p=$\frac{6-i}{6}$).

### Conditioning example

![image-20220228171346142](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228171346142.png)

![image-20220228171451060](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228171451060.png)

# Joint PMF drill 1

![image-20220228171737644](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228171737644.png)

![image-20220228172107550](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228172107550.png)

![image-20220228172133078](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228172133078.png)

![image-20220228172148378](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228172148378.png)

d.

![image-20220228172358784](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228172358784.png)

![image-20220228172617862](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228172617862.png)

![image-20220228172800538](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228172800538.png)

Well, since we're drawing a uniformly random permutation,

then the chance Xi is greater than Xj is exactly the same as

the chance that Xj is greater than Xi.

And therefore, we know this number must be equal to 1/2.

![image-20220228172911986](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228172911986.png)

![image-20220228172929589](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228172929589.png)

![](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228173304646.png)

![image-20220228173326440](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228173326440.png)

### Additional Theoretical Material

![image-20220228204651660](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228204651660.png)



If we  waste the first flip.

### The inclusion-exclusion formula

![image-20220228205121092](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228205121092.png)

Using indicator function

![image-20220228205851123](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228205851123.png)

![image-20220228210920058](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228210920058.png)

Unsolved Question:

![image-20220228224609245](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228224609245.png)

https://learning.edx.org/course/course-v1:MITx+6.431x+1T2022/block-v1:MITx+6.431x+1T2022+type@sequential+block@Problem_Set_4/block-v1:MITx+6.431x+1T2022+type@vertical+block@ch6-s7-tab5

![image-20220228225209762](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228225209762.png)

![image-20220228225215634](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220228225215634.png)

https://learning.edx.org/course/course-v1:MITx+6.431x+1T2022/block-v1:MITx+6.431x+1T2022+type@sequential+block@Problem_Set_4/block-v1:MITx+6.431x+1T2022+type@vertical+block@ch6-s7-tab6

![image-20220301092054154](C:\MyMarkDown\Courses\edX\MIT DS\Probability - The Science of Uncertainty and Data\image-20220301092054154.png)
