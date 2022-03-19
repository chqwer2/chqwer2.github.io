### MLOps: Data-centric AI

![image-20220119213744998](https://chqwer2.github.io/img/Typora/image-20220119213744998.png)

Improve the quality of the data
Data Augmentation….

### The Lifecycle of a ML Project

![image-20220119215217578](https://chqwer2.github.io/img/Typora/image-20220119215217578.png)

**Is the label labelled consistently?**

![image-20220119215558506](https://chqwer2.github.io/img/Typora/image-20220119215558506.png) 

![image-20220119215907637](https://chqwer2.github.io/img/Typora/image-20220119215907637.png)



### Data-Centric view (MLOPS)

The consitency of the data is paramount. Use tools to improve the data quality; this will allow multiple model to do well.

Hold the code fixed and iteratively improve the data.

About 1W data…

##### Small data and Label Consistency…

![image-20220121101201773](https://chqwer2.github.io/img/Typora/image-20220121101201773.png)

![image-20220121101333321](https://chqwer2.github.io/img/Typora/image-20220121101333321.png)

![image-20220121101616802](https://chqwer2.github.io/img/Typora/image-20220121101616802.png)

#### Long Tail Problem

Rare Events Inside Big Data: Web Search, Self-driving Car, Recommender Systems 

#### Error Analysis

Shows your algorithm does poorly in speech with car noise in the background. What do you do?

To indentify the types of data the algorithm does poorly on….

#### Data-Centric view:

How can I modify my data? (new examples, data augmentation, labeling, etc.)

give more consistent definition for labels if they were found to be ambiguous…

#### Production Deployment

Flow new data back for continuous refinement of model/

- Systematically check for concept drift/ data drift (Performance degradatioin)
- Flow data back to retrain/ update model regularly

### What is MLOps?

DevOps: Check Quality and Infrastructure..

![image-20220121102902491](https://chqwer2.github.io/img/Typora/image-20220121102902491.png)

![image-20220121103032495](https://chqwer2.github.io/img/Typora/image-20220121103032495.png)

![image-20220121103438493](https://chqwer2.github.io/img/Typora/image-20220121103438493.png)

![image-20220121103837167](https://chqwer2.github.io/img/Typora/image-20220121103837167.png)

