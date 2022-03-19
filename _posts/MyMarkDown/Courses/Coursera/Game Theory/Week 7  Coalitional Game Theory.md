# 7-1 Coalitional Game Theory: Taste 

Some things can be accomplished together, some are not

About Competition and Coalition...

**Which coalition will form?**

**How should that coalition devide its payoffs among its members**

$v$ is the value of the coalition

![image-20220114164331681](https://chqwer2.github.io/img/Typora/image-20220114164331681.png)

![image-20220114164452473](https://chqwer2.github.io/img/Typora/image-20220114164452473.png)

### 7-3 The Lloyd Shapley Value

Consider what is a 'fair' way for a coalition to divide its payoff?

This depends on how we define 'fairness'.

One Approach: identify **axioms** that express properties of a fair payoff division.



The idea: members should receive payments or shares proportional to their marginal contributions

N is all members

But this is tricky:

- Suppose $v(N)=1$ but $v(s)=0$ if $N!=S.$
- Then for every $i$: everybody's marginal contribution is 1, everybody is essential to generating any value.
- Cannot pay everyone their marginal Contribution!

![image-20220201173032636](https://chqwer2.github.io/img/Typora/image-20220201173032636.png)

But we can’t pay everybody 1

We need some **weighting system** for contribution.



#### Symmetry

- i and j are interchangeable relative to $v$
- for all $S$ that contains neither $i$ not $j$, $v(S\cup{i}) = v(S\cup{j})$

![image-20220114165632575](https://chqwer2.github.io/img/Typora/image-20220114165632575.png)

They should get equivalent payoffs



#### Dummy Players

- i is a dummy player if the amount of that i contributes to any coalition is 0.
- for all $S$:  $v(S\cup{{i}}) = v(S)$



![image-20220114165907317](https://chqwer2.github.io/img/Typora/image-20220114165907317.png)

They should receive nothing.



#### Additivity

If we can separate a game $v = v_1 + v_2$, then we should be able to decompose the payments:

superadditive?

![image-20220114170014028](https://chqwer2.github.io/img/Typora/image-20220114170014028.png)

![image-20220201162800343](https://chqwer2.github.io/img/Typora/image-20220201162800343.png)

### Shapley Value

Given a coalitional game $(N,v)$, the SV divides payoffs among players according to:

The first:  

all the possible ways that, we could have done this.

The middle: weighting that by different possible ways in which we could've come up with this marginal calculation

The final: marginal calculations![image-20220114170142312](https://chqwer2.github.io/img/Typora/image-20220114170142312.png)

![image-20220114170234633](https://chqwer2.github.io/img/Typora/image-20220114170234633.png)

This captures the "marginal contributions" of agent $i$, averaging over all the different sequences according to which the grand coalition could be built up.

It is daunting but：

N!:  permutation sequence ( 1, 12, 123; 2, 21, 213;…. 6 types), the final part is each i’s value

![image-20220201174559690](https://chqwer2.github.io/img/Typora/image-20220201174559690.png)

sequence of possible permutation with $i$ adding additional value



- For any such sequence, look at agent $i$'s marginal contribution when added $[v(S\cup{i})-v(s)]$ 
- Weight this quantity by the $|S|!$ ways the set $S$ could have been formed prior $i$'s addition by the $(|N|-|S|-1)!$ ways the remaining players could be added.
- 人员排列方式 * 他们加入所带来的收益
- ![image-20220201172011388](https://chqwer2.github.io/img/Typora/image-20220201172011388.png)

#### Example

![image-20220201174901535](https://chqwer2.github.io/img/Typora/image-20220201174901535.png)

![image-20220114204707150](https://chqwer2.github.io/img/Typora/image-20220114204707150.png)



### The Core

![image-20220114210146810](https://chqwer2.github.io/img/Typora/image-20220114210146810.png)

**Voting Game**

![image-20220114205932003](https://chqwer2.github.io/img/Typora/image-20220114205932003.png)

Can each sub-coalition gain by defecting from 

the grand coalition?

<img src="https://chqwer2.github.io/img/Typora/image-20220114210657199.png" alt="image-20220114210657199" style="zoom:25%;" />

A and B have enough votes to pass and gain higher payoff.

Shapley values is fair but don't necessarily give the right incentives to all of the different parties to want to actually join the grand coalition 

instead, **So the Core....**

![image-20220201170649771](https://chqwer2.github.io/img/Typora/image-20220201170649771.png)

Answer: And the answer as we'll see is that they would be willing to do so if the payment the profile belongs to a set which we'll call the core.

![image-20220201170807663](https://chqwer2.github.io/img/Typora/image-20220201170807663.png)

It isn't the case that any subcoalition could deviate away from the grand coalition, and end up with higher payment for themselves.

The sum of payoffs to the agents in any sub-coalition $S$ is at least as much as they could earn on their own

sub-coalition cannot deviate the grand coalition to gain higher payment

But the core always nonempty and unique?

Will be empty and no unique.

![image-20220114211353308](https://chqwer2.github.io/img/Typora/image-20220114211353308.png)

![image-20220114211501642](https://chqwer2.github.io/img/Typora/image-20220114211501642.png)

![image-20220114211649364](https://chqwer2.github.io/img/Typora/image-20220114211649364.png)

What is Veto?

否决权， 不包含$i$的Coalition value=0



**Another example**

![image-20220114211927507](https://chqwer2.github.io/img/Typora/image-20220114211927507.png)

City Airport or Regional airport?

The cost is depends on the largest aircraft...

#### Convex Game

![image-20220114212142396](https://chqwer2.github.io/img/Typora/image-20220114212142396.png)

Former we assume each coalition have empty intersection. Now we allow it but substract it.

![image-20220114212335519](https://chqwer2.github.io/img/Typora/image-20220114212335519.png)



### 7-5 Comparing the Core and Shapley value in an Example

Cooperative Game:

UN has 5 permanent members: CFRBU and 10 temporary members

Let’s start with simple version with 1 PM and 2 TM:

- $v(S)=1$ if $1 \in S$ and $\#S \geq 2$
- $v(S)=0$ otherwise.

Core: $x_1 + x_2\geq 1, x_1 + x_3\geq 1, x_1 + x_2 + x_3= 1, x_i\geq0$ 

Core:$x_1=1,x_2=0, x_3=0 $

The order of they attend the game.

![image-20220201160139074](https://chqwer2.github.io/img/Typora/image-20220201160139074.png)

![image-20220201160333153](https://chqwer2.github.io/img/Typora/image-20220201160333153.png)

![image-20220201160534277](https://chqwer2.github.io/img/Typora/image-20220201160534277.png)

So there's a fairly 

rich literature on cooperative game theory that's based on, on different approaches, 

to characterizing what fair kinds of values are.

### Quiz

![image-20220201170011755](https://chqwer2.github.io/img/Typora/image-20220201170011755.png)

