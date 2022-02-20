**0-1 integer programming is NP-complete.** 

See [Richard Karp's 21 NP-complete problems]([Karp's 21 NP-complete problems - Wikipedia](https://en.wikipedia.org/wiki/Karp's_21_NP-complete_problems))

- P vs NP vs NP-complete vs NP-hard
- **P**: a complexity class that represents the set of all decision problems that can be solved **in polynomial time** (efficiently).
- **NP**: a complexity class that represents the set of all decision problems for which the instances where the answer is "yes" have proofs that **can be verified in polynomial time**.
- **NP-complete**: NP-Complete is a complexity class which represents the set of all problems $X$ in NP for which it is **possible to reduce any other NP problem $Y$ to $X$ in polynomial time.**
  - Intuition: NP-complete means we can solve $Y$ quickly if we know how to solve $X$ quickly.

**P versus NP problem:**  whether “polynomial time algorithms actually exist for solving NP-Complete, or NP problems? Current answer is NO.

- What if we can proof [P = NP](https://cacm.acm.org/magazines/2009/9/38904-the-status-of-the-p-versus-np-problem/fulltext), What we would gain from P = NP will make the whole Internet look like a footnote in history.”

**NP-Hard:** the problems that are at least as hard as the NP-complete problems. 

- Note: NP-hard problems do not have to be in NP, and they do not have to be decision problems.

![image-20220219150649332](https://chqwer2.github.io/img/Typora/image-20220219150649332.png)

### How to solve the problem?

**Deterministic (Exact) methods**: 

- The Branch & Bound Method: Relax the problem as a continuous problem 

**Heuristic methods**: 

- Local search (hill climbing) 
- Simulated annealing 
- Genetic Algorithm