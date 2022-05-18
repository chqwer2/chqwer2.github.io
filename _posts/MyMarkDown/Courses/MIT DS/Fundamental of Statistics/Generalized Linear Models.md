# Generalized Linear Model (GLM)

![image-20220507170508917](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220507170508917.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220507171317786.png" alt="image-20220507171317786" style="zoom:50%;" />

The final one is the *Regression Function*

And the covariance matrix was just as diagonal matrix

with all these sigma squareds on the diagonal.



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220507171531447.png" alt="image-20220507171531447" style="zoom:50%;" />

![image-20220507172408946](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220507172408946.png)



### eneralizing the Linear Model; the Link Function 

The first one is to relax the random component to be,

for now, anything I want.

y given x does not have to be Gaussian,

but y given x can be any distribution.



We are working in the exponential family

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220507173837912.png" alt="image-20220507173837912" style="zoom:50%;" />

The link function



The next one is the Poisson distribution,

which is an approximation of the binomial when n becomes

large and p becomes small.

![image-20220507221429053](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220507221429053.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508095705488.png" alt="image-20220508095705488" style="zoom:50%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508100020916.png" alt="image-20220508100020916" style="zoom:50%;" />

![image-20220508100104771](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508100104771.png)

![image-20220508100005341](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508100005341.png)

All I'm saying is this is a vector whose coordinates depend

only on theta.

And this is a vector whose coordinates depend only on y.

And by only, I mean those coordinates do not depend on y,

and those coordinates do not depend on theta.

OK, so that's for the first part.

Then this is actually quite stringent.



![image-20220508101629923](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508101629923.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508102159453.png" alt="image-20220508102159453" style="zoom:50%;" />



![image-20220508102930709](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508102930709.png)

![image-20220508110036985](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508110036985.png)

### Normal 

How to solve

![image-20220508112516326](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508112516326.png)

### Gamma

![image-20220508112712977](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508112712977.png)

![image-20220508150647686](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508150647686.png)

![image-20220508150659639](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508150659639.png)





### One-Parameter Canonical Exponential Families 

![image-20220508113032991](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508113032991.png)

The canonical parameter of my Poisson is not lambda.

It's log of lambda.

So you have to do a reparameterization

of your problem to actually find what the canonical parameter

theta actually is.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508113246738.png" alt="image-20220508113246738" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508113534158.png" alt="image-20220508113534158" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508113828592.png" alt="image-20220508113828592" style="zoom:50%;" />

### Expectation in Terms of the Canonical Parameter

![image-20220508120049190](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508120049190-2007649.png)

![image-20220508120303640](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508120303640.png)



### Variance in Terms of the Canonical Parameter

Use the second identity

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508144843861.png" alt="image-20220508144843861" style="zoom:50%;" />

![image-20220508153943670](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508153943670.png)







<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508144956889.png" alt="image-20220508144956889" style="zoom:50%;" />





### Link Function

So rather than having a function that

goes from the real line to the interval 0 1

for Bernoulli's, we have a function

that goes from the interval 0 1 to the real line.

So this function is g.

![image-20220508163637996](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508163637996.png)

### Examples of Link Functions: Log, Logit, Probit

![image-20220508163943738](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508163943738.png)

We want it to be differential, and we want

it to be monotone increasing.

![image-20220508164751624](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508164751624.png)

![image-20220508165343252](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508165343252.png)

![image-20220508165351770](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508165351770.png)

# The Canonical Link Function

So remember, canonical means that g of mu

is equal to theta itself.

![image-20220511110119125](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220511110119125.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508170456013.png" alt="image-20220508170456013" style="zoom:50%;" />

 ![image-20220508170922400](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508170922400.png)

![image-20220511101535302](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220511101535302.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220511102814153.png" alt="image-20220511102814153" style="zoom:50%;" />

![image-20220508171418344](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508171418344.png)

![image-20220508171425665](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508171425665.png)

![image-20220511103146968](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220511103146968.png)

![image-20220508204301142](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508204301142.png)

![image-20220508204644094](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508204644094.png)

### Log-Likelihood for Exponential Families: Preparation for Estimation of Beta in GLMs

![image-20220508204819192](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220508204819192.png)

Plus Constant

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220511095745944.png" alt="image-20220508205302616" style="zoom:50%;" />

Gradient Descend

Newton's method is a technique that says if I have a curve

and I'm trying to find its intersection with zero,

I can actually just use Newton's method.







