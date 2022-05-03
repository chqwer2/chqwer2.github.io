



# Bayesian inference

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220401213759316.png" alt="image-20220401213759316" style="zoom:50%;" />



**Example:**

You're given data on a few patients,

and you need to figure out whether a certain treatment is

effective or not.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220401215024393.png" alt="image-20220401215024393" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220401215042353.png" alt="image-20220401215042353" style="zoom:50%;" />

Signal is interfered by noise.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220401215246998.png" alt="image-20220401215246998" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220401215437840.png" alt="image-20220401215437840" style="zoom:50%;" />

Generally speaking, these two types of problems, hypothesis

testing and estimation, have some significant differences

in the way that they are treated,

### The Bayesian inference framework

This is the prior distribution is discrete or continuing.

This is what we believe about Theta

before we obtain any data.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220401215846700.png" alt="image-20220401215846700" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220401215906170.png" alt="image-20220401215906170" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220401215934774.png" alt="image-20220401215934774" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220401223007799.png" alt="image-20220401223007799" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220401223101527.png" alt="image-20220401223101527" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220401223502742.png" alt="image-20220401223502742" style="zoom:50%;" />

![image-20220402090232487](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402090232487.png)

In this sense, the MAP rule is the optimum way

of coming up with estimates in the hypothesis-testing context,

where we want to minimize the probability of error.



“”

such a well crafted exercise to drive home a point.   I must say I've  been very impressed with the ingenuity of the vast majority of the  exercises and problem sets.  Often you think you understand something  from the lecture but then the exercise makes you look at it from a  different angle, forces you to think hard, hopefully get it right, but  always come away with a deeper understanding.  Kudos to the teaching  staff!! 

“”



### Discrete parameter, continuous observation

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402093325397.png" alt="image-20220402093325397" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402093441125.png" alt="image-20220402093441125" style="zoom:50%;" />

![image-20220402095237474](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402095237474.png)

Interesting Error

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402095424115.png" alt="image-20220402095424115" style="zoom:50%;" />

least mean square..

we form an estimator, and the main candidates for estimators at this points are, once more, the maximum a posteriori probability estimator,

**LMS**

![image-20220402104406132](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402104406132.png)

![image-20220402104858608](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402104858608.png)

![image-20220402104915077](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402104915077.png)

### Inferring the unknown bias of a coin and the Beta distribution

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402105655305.png" alt="image-20220402105655305" style="zoom:50%;" />





Normalization term: This particular form of the posterior distribution

for Theta is a certain type of density,

and it shows up in various contexts.

And for this reason, it has a name.

It is called a Beta distribution with certain parameters,

and the parameters reflect the exponents

that we have up here in the two terms.



Prior is not 1 in below:

![image-20220402110043519](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402110043519.png)

**Illustration of the update of the posterior distribution.** The file that is linked [here](https://courses.edx.org/assets/courseware/v1/50e83fd161607df26df9fb296bff5650/asset-v1:MITx+6.431x+1T2022+type@asset+block/lectureslides_beta_plots.pdf) illustrates the updating of the Beta posterior distribution of the bias of a coin, as more and more coin flips are observed, starting with a  uniform prior (in red, in the figures). Suppose that the true value of  the bias is . We generate independent samples of the coin flips, and each figure  shows the resulting posterior (in blue). For example, the third figure  shows the posterior if we observe one Heads and one Tails. In order to  illustrate the evaluation of the posterior, we also show (in black) all  of the previous posteriors. In the last figure, after 64 flips that  resulted in 19 Heads, the posterior shown (in blue) is centered in the  vicinity of the true value. On the other hand, the posterior has a  substantial width, indicating that there is still significant  uncertainty about the true value of the coin bias. 

### Inferring the unknown bias of a coin - point estimates

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402110737429.png" alt="image-20220402110737429" style="zoom:30%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402111235682.png" alt="image-20220402111235682" style="zoom:50%;" />

Why $d(n,k)$ equal to this?



They're fairly similar, but not exactly the same.

This means that the mean of a Beta distribution

is not the same as the point at which the distribution is

highest.

On the other hand, if n is a very large number,

this expression is going to be approximately equal to k over n

when n is large.

And so in the limit of large n, the two estimators

will not be very different from each other.



**Summary**

But if we want to come up with a single guess of what Theta is,

then we use a so-called estimator.

What an estimator does is that it calculates a certain value

as a function of the observed data.

![image-20220402113907076](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402113907076.png)

### Linear models with normal noise

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402114121460.png" alt="image-20220402114121460" style="zoom:50%;" />

![image-20220402114442327](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402114442327.png)

### Normal unknown and additive noise

Linear Relation

Now, X is shift by $\theta$, so it is $N(0,1)$.

![image-20220402115122788](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402115122788.png)

Log then minimize by deriviation...



### The case of multiple observations

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402155042828-8911043.png" alt="image-20220402155042828" style="zoom:33%;" />



Once I tell you the value of Theta,

then because the noises are independent,

the observations are also independent, so we can separate them..

We don’t bothered by constant

![image-20220402155314673](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402155314673.png)

The posterior PDF is normal

![image-20220402160232091](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402160232091.png)

![image-20220402155525645](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402155525645.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402155543568.png" alt="image-20220402155543568" style="zoom:50%;" />

![image-20220402155804956](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402155804956.png)

So the solution to this estimation problem that we just

went through has many nice properties.

First, we stay within the world of normal random variables,

because even the posterior is normal.

We stay within the world of linear functions

of normal random variables, and the form

of the formula that we have, itself,

has an appealing intuitive content.



![image-20220402161327164](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402161327164.png)

### mean squared error

sigma can represent noise level

![image-20220402162215435](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402162215435.png)



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402162309834.png" alt="image-20220402162309834" style="zoom:50%;" />

This expression makes quite a lot of sense.

It tells us that if we obtain more and more observations,

that is, as n increases, we improve our performance.



So we started with a prior variance

for Theta, which was 1.

And after we obtained the observation,

our uncertainty gets reduced and the variance goes down to 1/2.

Pictorially, here is what's happening.

![image-20220402163612531](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402163612531.png)

### Multiple parameters; trajectory estimation

For a written summary of the trajectory estimation problem, see [this document](https://courses.edx.org/assets/courseware/v1/21ddfd5247c2500011c50b549bdf705b/asset-v1:MITx+6.431x+1T2022+type@asset+block/estimation-tracking-post-6.041x.pdf).

Do not know the $\theta$,

And we also need some prior distributions

for these random variable.

We should specify the joint PDF of these three

random variables.

A common assumption here is to assume

that the random variables involved are

independent of each other.



According to Newton’s Law

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402165953015.png" alt="image-20220402165953015" style="zoom:50%;" />

![image-20220402170250773](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402170250773.png)

Now we have following…

![image-20220402170301983](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402170301983.png)

![image-20220402170427711](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402170427711.png)

### Linear normal models

![image-20220402172102527](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402172102527.png)

### Trajectory estimation illustration

The acceleration term often has to do

with gravitational effects which are known,

so we will treat Theta2 as a constant.

And that means that there's no point

in having a **prior distribution for Theta2**.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402203527345.png" alt="image-20220402203527345" style="zoom:50%;" />

Other don’t affect the minimization

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402204034813.png" alt="image-20220402204034813" style="zoom:50%;" />

Bayesian Confidence Interval. 

# Least mean squares (LMS) estimation

### LMS estimation without any observations

![image-20220402204729147](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402204729147.png)

Optimal LMS:

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402204912378.png" alt="image-20220402204912378" style="zoom:50%;" />

![image-20220402205630184](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402205630184.png)

### LMS performance evaluation

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402205917279.png" alt="image-20220402205917279" style="zoom:50%;" />



This quantity is just the average of this quantity

up here, averaged over all the possible values of X.

### Example: the LMS estimate

We observe some other random variable

X that's related to Theta according

to the following model.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402211539779.png" alt="image-20220402211539779" style="zoom:33%;" />



So the conclusion is that the posterior distribution of Theta

is a uniform distribution on this set.

### Example: LMS performance evaluation

![image-20220402215634766](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402215634766.png)



![image-20220402215858441](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402215858441.png)

# The multidimensional case

![image-20220402220113080](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402220113080.png)

**Some Challenges**

One first difficulty is that in many applications,

we do not necessarily have a good model

or we're not very confident about our model

of the observations.

![image-20220402220342987](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402220342987.png)

But this integral should be once more, over all the parameters.

So it would be a multi-dimensional integral

in the general case, and that's one additional source

of difficulty.

And this is the reason why we will also

consider an alternative to least mean squares estimation, which

is much simpler computationally and much less

demanding in terms of the model that we

need to have in our hands.

### Properties of the LMS estimation error

This may seem difficult, but conditioning is always

a great trick, so let's do that.

$\tilde \Theta$ is a contant given x

![image-20220402221516823](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402221516823.png)

![image-20220402232516574](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220402232516574.png)

### Solved Problem

![image-20220403111551900](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220403111551900.png)



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220403111949136.png" alt="image-20220403111949136" style="zoom:33%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220403112058980.png" alt="image-20220403112058980" style="zoom:33%;" />

![image-20220404164956020](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220404164956020.png)

https://learning.edx.org/course/course-v1:MITx+6.431x+1T2022/block-v1:MITx+6.431x+1T2022+type@sequential+block@Problem_Set_7/block-v1:MITx+6.431x+1T2022+type@vertical+block@ch10-s5-tab7

#TODO