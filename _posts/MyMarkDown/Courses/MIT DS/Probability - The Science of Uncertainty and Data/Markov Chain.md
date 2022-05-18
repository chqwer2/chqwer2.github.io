# Markov Model

We can approach this problem by using a Markov chain

model, a model where if we know the present situation,

the past history does not matter.



Markov chains are more elaborate, as they

allow some dependencies between different times.

However, these dependencies are of simple and restricted

nature, captured by the so-called Markov property.



### Markov Process

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220506223943264.png" alt="image-20220506223943264" style="zoom:50%;" />

#### Discrete time finite state Markov chains

$X_n$ is a random variable.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220506224212245.png" alt="image-20220506224212245" style="zoom:50%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220506224511762.png" alt="image-20220506224511762" style="zoom:50%;" />

### N-step transition probabilities

There is no way to know exactly where the system will be.

But you may be able to give probabilistic prediction.

That is, to give the probability for the system

to be in a given state 900 time steps later.



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220506224825302.png" alt="image-20220506224825302" style="zoom:50%;" />



Start with $i$, ends in $j$ with $n$ steps

Break down the possibility

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220506225126653.png" alt="image-20220506225126653" style="zoom:33%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220506225213775.png" alt="image-20220506225213775" style="zoom: 25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220506225459413.png" alt="image-20220506225459413" style="zoom:50%;" />

### A numerical example

Two-state example

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220506225858976.png" alt="image-20220506225858976" style="zoom:50%;" />

The probability starts to converge to constant.

### Generic convergence questions

Mathematically, we are asking the question, is rij of n pi j

when n goes to infinity?

The answer is that for nice Markov chains,

this will be true, but this is not always true.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220506232115635.png" alt="image-20220506232115635" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220506232248984.png" alt="image-20220506232248984" style="zoom:50%;" />

##### Recurrent and transient states

##### ![image-20220506234629468](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220506234629468.png)

# Steady-state behavior of Markov chains

time-homogeneous

#### Periodicity

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220507105302074.png" alt="image-20220507105302074" style="zoom:50%;" />

#### Steady-state convergence

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220507105848680.png" alt="image-20220507105848680" style="zoom:25%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220507105946361.png" alt="image-20220507105946361" style="zoom:25%;" />

#### Birth-death processes

![image-20220507113551615](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220507113551615.png)

![image-20220507120729914](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220507120729914.png)

![image-20220507120907241](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220507120907241.png)













