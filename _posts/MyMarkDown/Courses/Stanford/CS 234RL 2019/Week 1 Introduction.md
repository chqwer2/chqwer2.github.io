# Week 1

Learn to make a good **sequences of decisions**

Not immediately feedbacks

<img src="https://chqwer2.github.io/img/Typora/image-20211120133007461.png" alt="image-20211120133007461" style="zoom: 50%;" />

![image-20211120133227721](https://chqwer2.github.io/img/Typora/image-20211120133227721.png)

![image-20211120133331909](https://chqwer2.github.io/img/Typora/image-20211120133331909.png)

Agent Obeserve others' doing

### Course Goals

![image-20211120133601032](https://chqwer2.github.io/img/Typora/image-20211120133601032.png)

![image-20211121100858305](https://chqwer2.github.io/img/Typora/image-20211121100858305.png)

![image-20211121101011749](https://chqwer2.github.io/img/Typora/image-20211121101011749.png)

Machine Teaching

two model try to help each others

### Markov Assumption

you only need the current state of the enc to ...

![image-20211121102316037](https://chqwer2.github.io/img/Typora/image-20211121102316037.png)

If include enough history data into a state, can we make them part of Markov?

![image-20211121102457986](https://chqwer2.github.io/img/Typora/image-20211121102457986.png)

But hard to learn cuz all states are different

### Markov Decision Process (MDP)

### Partially Obeservable Markov Decision Process (POMDP)

![image-20211121103104282](https://chqwer2.github.io/img/Typora/image-20211121103104282.png)

![image-20211121103235622](https://chqwer2.github.io/img/Typora/image-20211121103235622.png)

### Bandits: not influence on future state

Ads that shown to Customer1, doesn't influence Customer2: they are independent, no relayed reward

The world is deterministic? 决定论? or Stochastic?
$$
Reward\ Function:\\
R(state)\\
R(State, Action)\\
R(State, Action, State' )
$$
![image-20211121104457592](https://chqwer2.github.io/img/Typora/image-20211121104457592.png)

![image-20211121104921221](https://chqwer2.github.io/img/Typora/image-20211121104921221.png)

### Intermix them

![image-20211121105145939](https://chqwer2.github.io/img/Typora/image-20211121105145939.png)

Different in finite horizon case:

Tend to mimic it is infinite horizon and look at the probability of reaching different termination states

### Evaluation and Control

![image-20211121110045260](https://chqwer2.github.io/img/Typora/image-20211121110045260.png)

