# Vector

### Sentiment Analysis 感情

Classify tweets: Positive or Negative?

### Vocabulary & Feature Extraction

A Sparse Representations of text as a vector

![image-20220114215432658](https://chqwer2.github.io/img/Typora/image-20220114215432658.png)

Problems:

Large feature space will need large training time and storage

### Tokenizing the string

**Map Vectors from (word, class) to Frequency**

![image-20220114215924345](https://chqwer2.github.io/img/Typora/image-20220114215924345.png)

How many times it shows up.

##### Preprocessing: Stemming, Lowercasing, Punctuation and Stop words

![image-20220114220747126](https://chqwer2.github.io/img/Typora/image-20220114220747126.png)

![image-20220114220908902](https://chqwer2.github.io/img/Typora/image-20220114220908902.png)

1. Eliminate handles and URLs
2. Tokenize the string into words. 
3. Remove stop words like "and, is, a, on, etc."
4. Stemming- or convert every word to its stem. Like dancer, dancing, danced, becomes 'danc'. er can be replaced with suffix ed and ing. You can use porter stemmer to take care of this. 
5. Convert all your words to lower case. 

Processed Results:

![image-20220114221136062](https://chqwer2.github.io/img/Typora/image-20220114221136062.png)

![image-20220114221244449](https://chqwer2.github.io/img/Typora/image-20220114221244449.png)

### Logistic Regression

using Sigmoid

![image-20220114221429148](https://chqwer2.github.io/img/Typora/image-20220114221429148.png)

### Cost Function

![image-20220116105412681](https://chqwer2.github.io/img/Typora/image-20220116105412681.png)

Calc the Gradient: [link](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/afcaR/optional-logistic-regression-gradient)

### Naive Bayes

##### Probability and Bayes’ Rule

![image-20220116115935915](https://chqwer2.github.io/img/Typora/image-20220116115935915.png)

![image-20220116120000597](https://chqwer2.github.io/img/Typora/image-20220116120000597.png)

### Naïve Bayes Introduction

Frequency:

![image-20220116122907250](https://chqwer2.github.io/img/Typora/image-20220116122907250.png)

Neg = 0 Influence the Calculation:

##### Laplacian Smoothing

We usually compute the probability of a word given a class as follows:

$P(wi∣ class )= \frac{freq (wi, class )}{Nclass}, class∈{ Positive, Negative } $

However, if a word does not appear in the training, then it automatically gets a probability of 0, to fix this we add smoothing as follows

$P\left(\mathrm{w}_{\mathrm{i}} \mid \mathrm{class}\right)=\frac{\operatorname{freq}\left(\mathrm{w}_{\mathrm{i}}, \text { class }\right)+1}{\left(\mathrm{N}_{\text {class }}+\mathrm{V}\right)} $

Note that we added a **1** in the numerator, and since there are **V** words to normalize, we add $V$ in the denominator. 

$N_{class}$: frequency of all words in class

$V$: number of unique words in vocabulary

![image-20220116123938962](https://chqwer2.github.io/img/Typora/image-20220116123938962.png)

![image-20220116143456774](https://chqwer2.github.io/img/Typora/image-20220116143456774.png)

### Log Likelihood

**Why using Log?**

more convenient to work with and they appeared throughout deep learning and NLP

![image-20220116143540060](https://chqwer2.github.io/img/Typora/image-20220116143540060.png)
$$
\lambda(w)=log\frac{P(w|pos)}{P(w|neg)}, logprior = los\frac{P(pos)}{P(neg)}
$$
![image-20220116144226781](https://chqwer2.github.io/img/Typora/image-20220116144226781.png)

### Application of Naïve Bayes

![image-20220116210841774](https://chqwer2.github.io/img/Typora/image-20220116210841774.png)

![image-20220116210929197](https://chqwer2.github.io/img/Typora/image-20220116210929197.png)

### Naïve Bayes Assumptions

Words in the sentences are necessarily independant… 

But Naive Bayes assume they are

It is relative to the frequencies in corpus.

### Error Analysis

What can cause errors:

![image-20220116211634892](https://chqwer2.github.io/img/Typora/image-20220116211634892.png)

![image-20220116211702407](https://chqwer2.github.io/img/Typora/image-20220116211702407.png)

![image-20220116211928496](https://chqwer2.github.io/img/Typora/image-20220116211928496.png)

Recap: Not is a neutral word??

![image-20220116212054560](https://chqwer2.github.io/img/Typora/image-20220116212054560.png)

### Adversarial Attack

Sarcasm, Irony and Euphemisms

挖苦,讽刺和委婉语气

![image-20220116212240884](https://chqwer2.github.io/img/Typora/image-20220116212240884.png)