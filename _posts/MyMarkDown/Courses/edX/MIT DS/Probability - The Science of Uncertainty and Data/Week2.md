

### 





### Bayes' Rule

![image-20220207220907291](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220207220907291.png)



, or conclusions about the more likely or less

likely scenarios that may have caused this events to occur.

That's what inference is.

So that’s what Bayes rule is doing.

Starting from conditional probabilities going in one

direction, it allows us to calculate conditional

probabilities going in the opposite direction.

It allows us to revise the probabilities of the different

scenarios, taking into account the new information.

And that's exactly what inference is all about, as



### Lec .3: Independence

Independence of two events

did not affect the probabilities of the second event

![image-20220207225210168](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220207225210168.png)



So this definition is indeed more general, and this alsomakes it more elegant.

![image-20220207230221107](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220207230221107.png)

##### Independence of event complements

A and B are independent,  then A and $B^c$ are also independent

![image-20220207232805300](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220207232805300.png)

### Conditional independence

Well, in the new universe where C has happened, events A and B have no intersection.

As we discussed earlier this means that events A and B are extremely dependent.

![image-20220207233716560](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220207233716560.png)

The conclusion from this example is that independence

does not imply conditional independence.

So in this particular example, we saw that the

answer here is no.

Given C, A and B are not independent.

![image-20220207234505488](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220207234505488.png)

This may be true in some special cases, e.g., if  and  both have zero probability. However, it is in general false. Suppose, for example, that events  and  have nonempty intersection inside , and are conditionally independent, but have empty intersection inside , which would make them dependent (given ).



##### Conditioning may affect independence

![image-20220208163744435](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220208163744435.png)

And therefore, information on the first 10 tosses

affects my beliefs about what's going

to happen in the [11th] toss.

And therefore, we do not have independence between the different tosses.

##### Independence of a collection of events

We will say that a family of events are independent if

knowledge about some of the events doesn't change my beliefs, my probability model, for the remaining events.

![image-20220208164716591](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220208164716591.png)

![image-20220208164727816](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220208164727816.png)

![image-20220208164823226](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220208164823226.png)

##### Independence versus pairwise independence

![image-20220208165658622](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220208165658622.png)



So we have here a situation where knowledge of H1 having

occurred does not help you in making a better guess on

whether C is going to occur.

### Reliablity

Independence is a very useful property.

Whenever it is true, we can break up complicated

situations into simpler ones.



We did prove that if two events are independent, then

their complements are also independent.

Now that we're dealing with multiple events here, a

general number n, how do we argue?

One approach would be to be formal and start from the

definition of independence of the U events.

![image-20220210155324986](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220210155324986.png)

And in the notation that we have introduced this is just

p1 times p2 times p3.

How do we turn a union into an intersection?

Use Morgan’s Laws

### The King's sibling

We are told that the king comes from a

family of two children.

What is the probability that his sibling is female?

Well, the problem is too loosely stated, so we need to

start by making some assumptions.

First, let's assume that we're dealing with an anachronistic

kingdom where boys have precedence.



In other words, if the royal family has two children, one

of which is a boy and one is a girl, it is always the boy who

becomes king, even if the girl was born first.

Let us also assume that when a child is born, it has 50%

probability of being a boy and 50%

probability of being a girl.



And in addition, let's assume that different children are

independent as far as their gender is concerned.

Let me state what these assumptions are.

We also need to … to determine the answer 2/3 is correct.

We assume that the royal family decided to have exactly

two children.

So the number two that we have here is not random.

It was something that was predetermined.

The general moral from this story is that when we deal

with situations that are described in words somewhat

vaguely, we must be very careful to state whatever

assumptions are being made.

And that needs to be done before we are able to fix a

particular probabilistic model.

This process of modeling will always be something of an art

in which judgment calls will have to be made.

### Example

**Rolling two dices**

Our sample space is clearly discrete.

So let's use some shorthand.



Doubles Rolled means we get same result from two dice

**chess tournament problem**

**A chess tournament problem.** This year's Belmont  chess champion is to be selected by the following procedure. Bo and Ci,  the leading challengers, first play a two-game match. If one of them  wins both games, he gets to play a two-game  **second round** with Al, the current champion. Al retains his championship unless a  second round is required and the challenger beats Al in both games. If  Al wins the initial game of the second round, no more games are played.

Furthermore, we know the following:
 The probability that Bo will beat Ci in any particular game is 0.6.
 The probability that Al will beat Bo in any particular game is 0.5.
 The probability that Al will beat Ci in any particular game is 0.7.

Assume no tie games are possible and all games are independent. 

\1. Determine the a priori probabilities that
 (a) the second round will be required.
 (b) Bo will win the first round.
 (c) Al will retain his championship this year.

\2. Given that the second round is required, determine the conditional probabilities that
 (a) Bo is the surviving challenger.
 (b) Al retains his championship.

\3. Given that the second round was required and that it comprised only  one game, what is the conditional probability that it was Bo who won the first round?



et cetera.

**The Monty Hall problem.** This is a much discussed  puzzle, based on an old American game show. You are told that a prize is equally likely to be found behind any one of three closed doors in  front of you. You point to one of the doors. A friend opens for you one  of the remaining two doors, after making sure that the prize is not  behind it. At this point, you can stick to your initial choice, or  switch to the other unopened door. You win the prize if it lies behind  your final choice of a door. Consider the following strategies: 

- Stick to your initial choice. 
- Switch to the other unopened door. 
- You first point to door 1. If door 2 is opened, you do not switch. If door 3 is opened, you switch. 

Which is the best strategy?



OK, so it turns out that the specific rules here actually

are very important.

Specifically, the rule about how your friend chooses to

open doors.

And the fact that he will always open one of the two

other door that you haven't picked and he will make sure

that that door doesn't have a prize behind it.

And let's see how that actually

plays out in this problem.

![image-20220210162754836](C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora\image-20220210162754836.png)

But by switching, you're actually banking on your first

choice being wrong, which is a relatively better bet, because

you're more likely to be wrong than right in your first

choice, because you're just picking blindly.

### A random walker

**A random walker.** Imagine a drunk tightrope walker, who manages to keep his balance, but takes a step forward with probability  and takes a step back with probability . 

(a) What is the probability that after two steps, the tightrope walker  will be at the same place on the rope as where he started?

(b) What is the probability that after three steps, the tightrope walker will be one step forward from where he started?

(c) Given that after three steps he has managed to move ahead one step,  what is the probability that the first step he took was a step forward? 

###  Communication over a noisy channel



