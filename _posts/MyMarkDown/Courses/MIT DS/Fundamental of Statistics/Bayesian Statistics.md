# Bayesian Statistics

At the end of this lecture, you will be able to do the following:

- Describe the **Bayesian approach**  to statistical decision making. 

- Explain the mechanisms of the Bayesian approach, particularly the **prior and posterior beliefs** . 

- Understand the role and significance of the prior distribution in a Bayesian set-up. 

- Identify the **Beta distribution**  and its role in Bayesian statistics as a prior distribution on a one-dimensional parameter. 

  ![image-20220410112727176](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220410112727176.png)

  

![image-20220410111911020](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220410111911020.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220410112527384.png" alt="image-20220410112527384" style="zoom:50%;" />

![image-20220410113912146](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220410113912146.png)

Beta is

extremely flexible.

Just by tweaking a and b, you can make

it look like a lot of shapes.



Now, the mean of a beta distribution with parameters a

and b is just a over a plus b.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/1920px-Beta_distribution_pdf.svg.png" alt="Probability density function for the Beta distribution" style="zoom:20%;" />



Beta Generator: https://keisan.casio.com/exec/system/1180573226

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220410114413786.png" alt="image-20220410114413786" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220410114436326.png" alt="image-20220410114436326" style="zoom:50%;" />

### ![image-20220410164848708](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220410164848708.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220410165157656.png" alt="image-20220410165157656" style="zoom: 33%;" />



Proportional sign that does not depends on $\theta$

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220410171803377.png" alt="image-20220410171803377" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220410200948359.png" alt="image-20220410200948359" style="zoom:50%;" />







### Choosing a Prior

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220411093219204.png" alt="image-20220411093219204" style="zoom: 33%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220411093732143.png" alt="image-20220411093732143" style="zoom:33%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220411094502375.png" alt="image-20220411094502375" style="zoom:50%;" />

No matter what theta is .

![image-20220418130020887](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220418130020887.png)

### Jeffreys Prior I: Definition

And the idea is to say, can I build a prior which is invariant under rescaling of the parameter.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220411113941628.png" alt="image-20220411113941628" style="zoom:50%;" />

estimate p or $p^{10}$? which will get the uniform prior?

Doesn’t matter. The is the goal of Jeffreys Prior

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417163144294.png" alt="image-20220417163144294" style="zoom:50%;" />

![image-20220417163414612](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417163414612.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417194016245.png" alt="image-20220417194016245" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220411113930387.png" alt="image-20220411113930387" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220416091513752.png" alt="image-20220416091513752" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220411114340866.png" alt="image-20220411114340866" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417154740999.png" alt="image-20220417154740999" style="zoom:50%;" />

And the reason why things can change

is because the variance might depend on your parameter,

but if nothing depends on your parameter,

then it doesn't matter where the mean is.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417155721550.png" alt="image-20220417155721550" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220411115039755.png" alt="image-20220411115039755" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220411115838417.png" alt="image-20220411115838417" style="zoom:50%;" />



It's trying to say, if those points with high Fisher

information are easier to estimate,

I'm going to put more prior on those guys.



And of course, the det is just the way

to collapse all this information into one number





### Bayesian Statistics for Inference

Depends on your prior has randomness or not?

![image-20220417201953207](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417201953207.png)

![image-20220417202542628](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417202542628.png)

### Bayesian Estimator:

![image-20220417203456907](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417203456907.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417204002606.png" alt="image-20220417204002606" style="zoom:50%;" />

Consistent and asymptotically normal

![image-20220419095801420](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220419095801420.png)



# Calculating Bayes Posteriors

Recitation

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220410154306057.png" alt="image-20220410154306057" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220410154957400.png" alt="image-20220410154957400" style="zoom:50%;" />



# Multinomial Bayesian Estimation

![image-20220417210226317](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417210226317.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417211932491.png" alt="image-20220417211932491" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417212405126.png" alt="image-20220417212405126" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417212503493.png" alt="image-20220417212503493" style="zoom:50%;" />

Example:

![](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417213535494.png)

![image-20220417214203149](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417214203149.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417214226166.png" alt="image-20220417214226166" style="zoom:50%;" />

![image-20220417225737204](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220417225737204.png)

Conjugate of Gau and Exp

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220418090752620.png" alt="image-20220418090752620" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220418090835900.png" alt="image-20220418090835900" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220418090854227.png" alt="image-20220418090854227" style="zoom:50%;" />

![image-20220418092030981](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220418092030981.png)

![image-20220418102033769](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220418102033769.png)

Gamma

![image-20220418102133813](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220418102133813.png)

