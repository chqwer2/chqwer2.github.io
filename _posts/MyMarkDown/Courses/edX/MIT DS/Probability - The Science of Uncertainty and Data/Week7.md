# Unit 6

unconditional (or prior) probability

conditional (or posterior)

## Derived Distribution

Given the distribution of $X, Y$, find the distribution of $Z=g(X, Y)$.

**Discrete:**

![image-20220315144454365](https://chqwer2.github.io/img/Typora/image-20220315144454365.png)

**Continuous:**

![image-20220315144739282](https://chqwer2.github.io/img/Typora/image-20220315144739282.png)

**How to find a PDF of r.v.?**

<img src="https://chqwer2.github.io/img/Typora/image-20220315145620969.png" alt="image-20220315145620969" style="zoom: 67%;" />

Example 1

![image-20220315150012454](https://chqwer2.github.io/img/Typora/image-20220315150012454.png)

Example 2

![image-20220315150159819](https://chqwer2.github.io/img/Typora/image-20220315150159819.png)

### The monotonic case

Monotonic function is $g(\cdot)$ = $x^3, a/x$ etc., we have if $x < x' \to g(x)<g(x')$ or vise. 

inverse function we call $h(\cdot) = g'(\cdot)$, when g increase, h also increase

<img src="https://chqwer2.github.io/img/Typora/image-20220315155433045.png" alt="image-20220315155433045" style="zoom:50%;" />

<img src="https://chqwer2.github.io/img/Typora/image-20220315155510279.png" alt="image-20220315155510279" style="zoom:67%;" />

It is simpler because we only do $h(\cdot)$ function

General Method for Nonmonotonic Case

![image-20220315160814139](https://chqwer2.github.io/img/Typora/image-20220315160814139.png)

![image-20220315164126318](https://chqwer2.github.io/img/Typora/image-20220315164126318.png)

### Sum of independent continuous r.v.'s

<img src="https://chqwer2.github.io/img/Typora/image-20220315171314982.png" alt="image-20220315171314982" style="zoom:67%;" />

Proof:

![image-20220315171924290](https://chqwer2.github.io/img/Typora/image-20220315171924290.png)

![image-20220315211020632](https://chqwer2.github.io/img/Typora/image-20220315211020632.png)



### Covariance

![image-20220315211310011](https://chqwer2.github.io/img/Typora/image-20220315211310011.png)

Independent = $Conv(X,Y) = 0$ (converse is not true)

Or simply:

![image-20220315212340858](https://chqwer2.github.io/img/Typora/image-20220315212340858.png)

**The variance of the sum of r.v.'s**

![image-20220315212752501](https://chqwer2.github.io/img/Typora/image-20220315212752501.png)

All possible covariance between all pairs

### correlation coefficient

![image-20220315213838229](https://chqwer2.github.io/img/Typora/image-20220315213838229.png)

is dimensionless

### Interpreting the correlation coefficient

![image-20220315214755006](https://chqwer2.github.io/img/Typora/image-20220315214755006.png)

### Correlations matter

![image-20220315220028095](https://chqwer2.github.io/img/Typora/image-20220315220028095.png)

## Conditional Expectation and Variance

In this segment we revisit the concept of conditional expectation and view it as an abstract object

of a special r.v. $g(y)$.

![image-20220316102554732](https://chqwer2.github.io/img/Typora/image-20220316102554732.png)

The Law of iterated expectations

![image-20220316103541185](https://chqwer2.github.io/img/Typora/image-20220316103541185.png)

![image-20220317200226259](https://chqwer2.github.io/img/Typora/image-20220317200226259.png)

![image-20220317200739986](https://chqwer2.github.io/img/Typora/image-20220317200739986.png)

**Stick-breaking revisited**

![image-20220316104118244](https://chqwer2.github.io/img/Typora/image-20220316104118244.png)

### The conditional variance

as a random variable

![image-20220317175043901](https://chqwer2.github.io/img/Typora/image-20220317175043901.png)

proof of this equality:

>  Derivation of the law of total variance

![image-20220317175559717](https://chqwer2.github.io/img/Typora/image-20220317175559717.png)

And according to the law of iterated expectations, it is

the same as the unconditional expectation.

![image-20220317175744268](https://chqwer2.github.io/img/Typora/image-20220317175744268.png)

![image-20220317201936918](https://chqwer2.github.io/img/Typora/image-20220317201936918.png)

**A simple example**

![image-20220317180319094](https://chqwer2.github.io/img/Typora/image-20220317180319094.png)

### Section means and variances

We will now go through another example to consolidate our

intuition about the content of the law of iterated

expectations and the law of the total variance.

![image-20220317180714804](https://chqwer2.github.io/img/Typora/image-20220317180714804.png)

![image-20220317180907945](https://chqwer2.github.io/img/Typora/image-20220317180907945.png)