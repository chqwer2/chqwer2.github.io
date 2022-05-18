# Week 5 ER Modeling

How to build?

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423103203067.png" alt="image-20220423103203067" style="zoom:50%;" />

entities, relationships and attributes.

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423103432264.png" alt="image-20220423103432264" style="zoom:30%;" />



<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423104002284.png" alt="image-20220423104002284" style="zoom:50%;" />

Exercise 5.1

ER Modeling tool [Draw.io (Links to an external site.)](https://app.diagrams.net/) (Free)





### Week 6 DBMS

### Week 7 SQL

PostgreSQL website: [https://www.postgresql.org/ (Links to an external site.)](https://www.postgresql.org/)

Getting Started With PostgreSQL [https://www.postgresqltutorial.com/postgresql-getting-started/ (Links to an external site.)](https://www.postgresqltutorial.com/postgresql-getting-started/)

PostgreSQL 14.2 Documentation [https://www.postgresql.org/docs/14/index.html (Links to an external site.)](https://www.postgresql.org/docs/14/index.html)

PostgreSQL cheat sheer [https://www.postgresqltutorial.com/postgresql-cheat-sheet/Links to an external site.](http:// https://www.postgresqltutorial.com/postgresql-cheat-sheet/)



```
export PSQL_DIR=/Library/PostgreSQL/13/bin
export PATH="$PSQL_DIR:$PATH"

psql postgres
#Username [postgres] [2022]
psql -U postgres \

```

```
\l   # Dataset info include all table
\du  # User info
\dt  # Relation info
\d Table # Table info
\c Table User # Connect
```

Create user

CREATE ROLE fsad NOINHERIT LOGIN PASSWORD 'fsad2022';



![image-20220423113419494](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423113419494.png)

Create database

![image-20220423113529108](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423113529108.png)

Connect database

![image-20220423113638981](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423113638981.png)

Create Table

![image-20220423113752921](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423113752921.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423154039160.png" alt="image-20220423154039160" style="zoom:50%;" />





Select and Insert

![image-20220423113914098](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423113914098.png)

![image-20220423114011654](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423114011654.png)

![image-20220423114046549](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423114046549-0710453.png)



Update and If statement

![image-20220423114138044](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423114138044.png)

![image-20220423114240240](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423114240240.png)

![image-20220423114307854](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423114307854.png)

### Querying

Slow and Fast delete

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423150902980.png" alt="image-20220423150902980" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423150940838.png" alt="image-20220423150940838" style="zoom:50%;" />

Load file into Table

![image-20220423151155532](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423151155532.png)

Constrain between tables: ALTER

What is ALTER?

![image-20220423151544478](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423151544478.png)

![image-20220423151654524](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423151654524.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423151706317.png" alt="image-20220423151706317" style="zoom:50%;" />

Insert

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423151804034.png" alt="image-20220423151804034" style="zoom:50%;" />

Count how many rows that match the return: SUM, COUNT, MAX, ROUND, AVG

![image-20220423152119633](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423152119633.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423152226645.png" alt="image-20220423152226645" style="zoom:50%;" />

![image-20220423152422683](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423152422683.png)

Order: ASC and DESC - depending

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423152507593.png" alt="image-20220423152507593" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423152521380.png" alt="image-20220423152521380" style="zoom:50%;" />

### Advanced SQL

Backup

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423153323500.png" alt="image-20220423153323500" style="zoom:50%;" />

Import from sql file

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423154127654.png" alt="image-20220423154127654" style="zoom:50%;" />

### Join : intersection and union, compliment

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423155154300.png" alt="image-20220423155154300" style="zoom:50%;" />



INNER JOIN: only work with correct relationship

![image-20220423155350058](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423155350058.png)

RIGHT JOIN, FULL JOIN

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423155709368.png" alt="image-20220423155709368" style="zoom:50%;" />

![image-20220423155726885](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20220423155726885.png)

