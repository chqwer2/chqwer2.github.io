# Lecture 8

### PDFs

Let us look at an interval that starts at some a and goes

up to some number a plus delta.

![image-20220311174959351](https://chqwer2.github.io/img/Typora/image-20220311174959351.png)

![image-20220311175122922](https://chqwer2.github.io/img/Typora/image-20220311175122922.png)

$\delta$ is very small.

### Conditional PDFs

![image-20220311224654734](https://chqwer2.github.io/img/Typora/image-20220311224654734.png)





### Memorylessness of the exponential PDF

![image-20220311225317011](https://chqwer2.github.io/img/Typora/image-20220311225317011.png)

So new and used light bulbs are described by the same

probabilities, and they're probabilistically

identical, the same.



And from this, we can calculate the probability that

T lies in a small interval.

![image-20220311225149739](https://chqwer2.github.io/img/Typora/image-20220311225149739.png)

![image-20220311225428609](https://chqwer2.github.io/img/Typora/image-20220311225428609.png)

### Total probability and expectation theorems

Converted into **pdf** and **cdf** version

![image-20220311230018268](https://chqwer2.github.io/img/Typora/image-20220311230018268.png)

### Joint PDFs

where we use f to indicate that we're dealing with a density. p for probability.

![image-20220311230944093](https://chqwer2.github.io/img/Typora/image-20220311230944093.png)

![image-20220311231314671](https://chqwer2.github.io/img/Typora/image-20220311231314671.png)

Special case:

Now, let's think of a particular situation.

Suppose that X is a continuous random variable, and let Y be

another random variable, which is identically equal to X.

Since X is a continuous random variable, Y is also a

continuous random variable.

However, in this situation, we are certain that the outcome

of the experiment is going to fall on the line

where x equals y.

All the probability lies on top of a line, and

a line has 0 area.

So we have positive probability on the set of 0

area, which contradicts what we discussed before.

Well, this simply means that X and Y are not jointly

continuous.



Joint density

![image-20220311231837590](https://chqwer2.github.io/img/Typora/image-20220311231837590.png)





Joint CDFs

![image-20220312113057554](https://chqwer2.github.io/img/Typora/image-20220312113057554.png)

### Conditional PDFs

this is problematic, because this

event does not have positive probability.

![image-20220312114229282](https://chqwer2.github.io/img/Typora/image-20220312114229282.png)

However, because we are conditioning on Y being

approximately equal to a certain value, we end up using

a corresponding conditional PDF, where the conditional PDF

is defined this way.

![image-20220312114709851](https://chqwer2.github.io/img/Typora/image-20220312114709851.png)

### Total probability and total expectation theorems

![image-20220312140912470](https://chqwer2.github.io/img/Typora/image-20220312140912470.png)



<img src="https://chqwer2.github.io/img/Typora/image-20220312151502909.png" alt="image-20220312151502909" style="zoom:50%;" />

<img src="https://chqwer2.github.io/img/Typora/image-20220312151518505.png" alt="image-20220312151518505" style="zoom:50%;" />

7 False. Given that Y, we need to somehow take into account the **conditional distribution of X,** whereas the right-hand side **is determined by the unconditional PDF of** **X** .

The difference is random variable Y can take any value defined in the sample domain, while y is a constant. [solution removed]

### Independence

![image-20220312141313858](https://chqwer2.github.io/img/Typora/image-20220312141313858.png)

### Stick-breaking example

![image-20220312141507667](https://chqwer2.github.io/img/Typora/image-20220312141507667.png)

Not independece…

Another way to see it is that if I tell you that x is 0.5,

this gives you lots of information about Y. It tells

you that Y has to be less than or equal to 0.5.

![image-20220312141803956](https://chqwer2.github.io/img/Typora/image-20220312141803956.png)

![image-20220312142136489](https://chqwer2.github.io/img/Typora/image-20220312142136489.png)

Finally we can break it makes it easier.

But the calculation is a bit tedious.

So let us look for an alternative

and more clever approach.

The idea is to divide and conquer.

We're going to use the total expectation theorem, where

we're going to condition on X. The total expectation theorem

tells us that the expected value of Y is the integral

over all possible values of the random variable X, which

is from 0 to l.

Independence of normal distribution

![image-20220312144255597](https://chqwer2.github.io/img/Typora/image-20220312144255597.png)

On each contour the joint PDF is a constant.

![image-20220312144643983](https://chqwer2.github.io/img/Typora/image-20220312144643983.png)

If you wanted a bell that stretches in some diagonal

direction, or if you have contours that are ellipses but

with some different kinds of axes, then you will have

dependence between the two random variables.

In that case, we will be dealing with a so-called

bivariate normal distribution, but we will not pursue this

# Bayes rule variations

marginal PMF.
$$
P_Y(y)
$$
![image-20220312160048952](https://chqwer2.github.io/img/Typora/image-20220312160048952.png)

### Mixed Bayes rule

![image-20220312161757900](https://chqwer2.github.io/img/Typora/image-20220312161757900.png)

The final is total probability theory

### Detection of a binary signal

![image-20220312162740107](https://chqwer2.github.io/img/Typora/image-20220312162740107.png)

### Inference of the bias of a coin

![image-20220312164036173](https://chqwer2.github.io/img/Typora/image-20220312164036173.png)

### **Buffon's needle and Monte Carlo simulation.** 

A surface is ruled with parallel lines, which are at distance  from each other. Suppose that we throw a needle of length  on the surface at random. What is the probability that the needle will intersect one of the lines? 

the length of needle $l$ is less than $d$:

<img src="https://chqwer2.github.io/img/Typora/image-20220314210902016.png" alt="image-20220314210902016" style="zoom:33%;" />

Model:

![image-20220314211340090](https://chqwer2.github.io/img/Typora/image-20220314211340090.png)

![image-20220314211456036](https://chqwer2.github.io/img/Typora/image-20220314211456036.png)

Monte Carlo simulation:

Some hyper-space volume cannot be calculated by integral etc. so we can uniformly sample the space and get the volume (with probability)

![image-20220314221502114](https://chqwer2.github.io/img/Typora/image-20220314221502114.png)

??
