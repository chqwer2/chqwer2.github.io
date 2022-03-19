# Repeated Games 

OPEC: Limited Oil Producing to control the price, cuz country will tend to pump more oil to make profit

### Infinitely Repeated Games: Utility 

![image-20220104000457024](https://chqwer2.github.io/img/Typora/image-20220104000457024.png)

![image-20220104000737297](https://chqwer2.github.io/img/Typora/image-20220104000737297.png)

### Stochastic Games

Is generalization of the repeated game (but not the same)

![image-20220105232551942](https://chqwer2.github.io/img/Typora/image-20220105232551942.png)

Also generalizes MDP (Markov Decision Process)

- MDP is a single-agent game

### Learning in Repeated Games 

two types: Fictitious Play and No-regret Learning

learner and teacher...

##### Fictitious Play

<img src="https://chqwer2.github.io/img/Typora/image-20220105233901548.png" alt="image-20220105233901548" style="zoom:33%;" />

<img src="https://chqwer2.github.io/img/Typora/image-20220105233944552.png" alt="image-20220105233944552" style="zoom: 33%;" />

player plays pure-strategy and model others using mixed-strategy.

![image-20220107212947342](https://chqwer2.github.io/img/Typora/image-20220107212947342.png)

Not converge but the empirical frequencies will...

##### No-regret Learning

![image-20220107213505803](https://chqwer2.github.io/img/Typora/image-20220107213505803.png)

not learning from others, instead modify their own strategies

![image-20220107213750463](https://chqwer2.github.io/img/Typora/image-20220107213750463.png)

Can converge..

### 5-5 Equilibria of Infinitely Repeated Games 

What is a pure strategy in an infinitely-repeated game?

A pure strategy is a rule that you will follow to make decisions

![image-20220107214622881](https://chqwer2.github.io/img/Typora/image-20220107214622881.png)

Can describe the stragety

**How to determine the NE?**

![image-20220107215501999](https://chqwer2.github.io/img/Typora/image-20220107215501999.png)

![image-20220107215422951](https://chqwer2.github.io/img/Typora/image-20220107215422951.png)

Minmax - player can get the best payoffs by himself

the potential payoffs profile should be larger than Minmax value

Folk Theorem

![image-20220107221626764](https://chqwer2.github.io/img/Typora/image-20220107221626764.png)

Not enforceable since in each case they give to a player an expected value lower than her minmax value. 

the payoff is reasonable and it is feasible... them there will be NE.

![image-20220107224055333](https://chqwer2.github.io/img/Typora/image-20220107224055333.png)

### 5-6 Discounted Repeated Games 

People value more of the payoff today

Discount factors $\beta$ are the decay factors

Usually assume all the  $\beta$ are same

![image-20220108153239272](https://chqwer2.github.io/img/Typora/image-20220108153239272.png)

Defect: First 5 then 1 forever...

![image-20220108155302521](https://chqwer2.github.io/img/Typora/image-20220108155302521.png)calc how much Discounted Factors value you need to keep Cooperation

![image-20220108160720117](https://chqwer2.github.io/img/Typora/image-20220108160720117.png)

choose to defect alternatively, then each one get 5

What if payoff varies? Not knowing others' movings?

### Keep Playing

PS of playing once  

Ps of playing twice  

playing more...? 
