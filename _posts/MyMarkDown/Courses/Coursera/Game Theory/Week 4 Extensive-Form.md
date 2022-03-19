# Extensive-Form Games

### 4-1 Perfect Information Extensive Form: Taste 

![image-20211203085043154](https://chqwer2.github.io/img/Typora/image-20211203085043154.png)



Game Tree ?

### 4-2 Formalizing Perfect Information Extensive Form Games 

![image-20211203085303892](https://chqwer2.github.io/img/Typora/image-20211203085303892.png)

![image-20211203085422816](https://chqwer2.github.io/img/Typora/image-20211203085422816.png)

The factors to Define Utility Functions,

Players take turn in the game tree

![image-20211203090019939](https://chqwer2.github.io/img/Typora/image-20211203090019939.png)

![image-20211203090121016](https://chqwer2.github.io/img/Typora/image-20211203090121016.png)

Two people chose nodes in turn

### 4-3 Perfect Information Extensive Form: Strategies, BR, NE 

How many pure-strategy does each player have?

P1: 3, P2: 8 (because PS is a combination of choices)

![image-20211203090600615](https://chqwer2.github.io/img/Typora/image-20211203090600615.png)



![image-20211203090833048](https://chqwer2.github.io/img/Typora/image-20211203090833048.png)

![image-20211203091159902](https://chqwer2.github.io/img/Typora/image-20211203091159902.png)

Have some repitition will cause some problem (blow up)

![image-20211203091558139](https://chqwer2.github.io/img/Typora/image-20211203091558139.png)

What are the three pure-strategy equilibria?

<img src="https://chqwer2.github.io/img/Typora/image-20211203091743537.png" alt="image-20211203091743537" style="zoom:50%;" />

### How to find it?

<img src="https://chqwer2.github.io/img/Typora/image-20211203092002363.png" alt="image-20211203092002363" style="zoom:50%;" />



## 4-4 Subgame Perfection 

Normally, nobody can get a profitable deviation from NE.

![image-20211203094033629](https://chqwer2.github.io/img/Typora/image-20211203094033629.png)

**Claming** going down H so better go to E, It is a **thread** of player 1 to prevent player 2 goto **F**

![image-20211203094356036](https://chqwer2.github.io/img/Typora/image-20211203094356036.png)

![image-20211203094512742](https://chqwer2.github.io/img/Typora/image-20211203094512742.png)

Sub-game E sample: **for each node?**

**Deviate** when can be profitable but not determined...  such as E and F 

![image-20211203095012582](https://chqwer2.github.io/img/Typora/image-20211203095012582.png)

<img src="https://chqwer2.github.io/img/Typora/image-20220107145026428.png" alt="image-20220107145026428" style="zoom:50%;" />

BHCE is not a subgame perfection

AHCF is nor a subgame perfection

![image-20220107145842558](https://chqwer2.github.io/img/Typora/image-20220107145842558.png)

$$
p + p^2 + p^3 +\cdots + p^n = \frac{p}{1-p}
$$


### 4-5 Backward Induction 

the way to compute the subgame perfection.

**Assueming** others play the subgame perfect, 

![image-20211203102129342](https://chqwer2.github.io/img/Typora/image-20211203102129342.png)

Can use minimax algorithm  

Also pruning nodes that will never be reached in play.

![image-20211203103117721](https://chqwer2.github.io/img/Typora/image-20211203103117721.png)

![image-20220103165703939](https://chqwer2.github.io/img/Typora/image-20220103165703939.png)

Only subgame perfection...

assum that if... backwards

But if player 1 won't go down, player 2 will know and maybe won't down either



### 4-6 Subgame Perfect Application: Ultimatum Bargaining

![image-20220103170008930](https://chqwer2.github.io/img/Typora/image-20220103170008930.png)

### 4-8 Imperfect Information Extensive Form: Definition, Strategies 

Poker: players can remember all the history

![image-20220103173811423](https://chqwer2.github.io/img/Typora/image-20220103173811423.png)

### Mixed and Behavioral Strategies 

![image-20220103223131974](https://chqwer2.github.io/img/Typora/image-20220103223131974.png)

Mixed strategy is a pure-strategy based on given information set

Behavioral strategy is fully randomized

![image-20220103230826247](https://chqwer2.github.io/img/Typora/image-20220103230826247.png)

![image-20220103231411233](https://chqwer2.github.io/img/Typora/image-20220103231411233.png)

Mixed Strategy cannot reach the high payoff point

Behavioral Strategy can. 

### 4-10 Incomplete Information in the Extensive Form: Beyond Subgame Perfection 

with **incomplete information** there may not be many proper subgames 

The line dedicate that incomplete information... that player 2 doesn't know...

##### Using subgame perfection

the node is related so cannot be chopped



**subgame perfection** about open a coffee shop

![image-20220103232324474](https://chqwer2.github.io/img/Typora/image-20220103232324474.png)



