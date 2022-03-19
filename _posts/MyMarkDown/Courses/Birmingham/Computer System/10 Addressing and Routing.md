# Addressing and Routing

[Week 10-IP_Addressing_and_Subnets_Solutions (1).pdf](C:\Users\calvchen\Documents/Week 10-IP_Addressing_and_Subnets_Solutions.pdf)

[Week 10 - Network_Security_Solution (1).pdf](C:\Users\calvchen\Documents/Week 10 - Network_Security_Solution (1).pdf)



![image-20211210001932630](https://chqwer2.github.io/img/Typora/image-20211210001932630.png)

![image-20211210002227124](https://chqwer2.github.io/img/Typora/image-20211210002227124.png)



# Network Security

- Chapter #8: **Security in Computer Networks,** Computer Networking: A Top-Down Approach (7th edition) by Kurose & Ross



![image-20211208090707696](https://chqwer2.github.io/img/Typora/image-20211208090707696.png)

![image-20211208093822165](https://chqwer2.github.io/img/Typora/image-20211208093822165.png)



# Addressing and Routing

Network Layer

![image-20211208204436181](https://chqwer2.github.io/img/Typora/image-20211208204436181.png)

![image-20211208205159943](https://chqwer2.github.io/img/Typora/image-20211208205159943.png)

**Routing**: Process of planning trip from source to destination

**Forwarding**: Process of getting through single interchange

![image-20211208205421269](https://chqwer2.github.io/img/Typora/image-20211208205421269.png)

Before datagrams flow, two end hosts and intervening  routers establish virtual connection

![image-20211208205918049](https://chqwer2.github.io/img/Typora/image-20211208205918049.png)

![image-20211208205953062](https://chqwer2.github.io/img/Typora/image-20211208205953062.png)

![image-20211208210644283](https://chqwer2.github.io/img/Typora/image-20211208210644283.png)

![image-20211208210923692](https://chqwer2.github.io/img/Typora/image-20211208210923692.png)

Input port pre-pends a switch-internal label (header) and  transmits the packet onto the bus. Header matching at  output ports.

![image-20211208211058563](https://chqwer2.github.io/img/Typora/image-20211208211058563.png)

![image-20211208211410520](https://chqwer2.github.io/img/Typora/image-20211208211410520.png)

![image-20211208211532964](https://chqwer2.github.io/img/Typora/image-20211208211532964.png)

### IPv4

![image-20211208211641081](https://chqwer2.github.io/img/Typora/image-20211208211641081.png)

Time-to-live accross one router minus 1

IP address: 32-bit 

![image-20211208215454754](https://chqwer2.github.io/img/Typora/image-20211208215454754.png)

![image-20211208215520503](https://chqwer2.github.io/img/Typora/image-20211208215520503.png)

![image-20211208215557661](https://chqwer2.github.io/img/Typora/image-20211208215557661.png)

NAT: Network Address Translation

![image-20211208215907606](https://chqwer2.github.io/img/Typora/image-20211208215907606.png)

![image-20211208215932752](https://chqwer2.github.io/img/Typora/image-20211208215932752.png)

![image-20211208220237824](https://chqwer2.github.io/img/Typora/image-20211208220237824.png)

### Network Layer Routing Algorithms

![image-20211208220346898](https://chqwer2.github.io/img/Typora/image-20211208220346898.png)

### Dijkstra's Algo (LS)

![image-20211208220507444](https://chqwer2.github.io/img/Typora/image-20211208220507444.png)

![image-20211208220521552](https://chqwer2.github.io/img/Typora/image-20211208220521552.png)

![image-20211208220613408](https://chqwer2.github.io/img/Typora/image-20211208220613408.png)

![image-20211208220915593](https://chqwer2.github.io/img/Typora/image-20211208220915593.png)

![image-20211209102507359](https://chqwer2.github.io/img/Typora/image-20211209102507359.png)

### Oscilations

![image-20211209104532450](https://chqwer2.github.io/img/Typora/image-20211209104532450.png)

Distance-Vector (DV) Routing Algorithm

![image-20211209105120266](https://chqwer2.github.io/img/Typora/image-20211209105120266.png)

![image-20211209105153062](https://chqwer2.github.io/img/Typora/image-20211209105153062.png)

![image-20211209105521837](https://chqwer2.github.io/img/Typora/image-20211209105521837.png)

**Notify Others**

![image-20211209105907886](https://chqwer2.github.io/img/Typora/image-20211209105907886.png)

**Drawbacks**: If local link cost changes, it will not notify others...

![image-20211209110301425](https://chqwer2.github.io/img/Typora/image-20211209110301425.png)

Link and Path ?

## In Practice

![image-20211209110639011](https://chqwer2.github.io/img/Typora/image-20211209110639011.png)

Same algorithm running in one AS as mentioned above

![image-20211209111103012](https://chqwer2.github.io/img/Typora/image-20211209111103012.png)

![image-20211209111226315](https://chqwer2.github.io/img/Typora/image-20211209111226315.png)

![image-20211209111538842](https://chqwer2.github.io/img/Typora/image-20211209111538842.png)

Inter : Set Forwarding Table od destinations

# Network Security

**Question:** Network Security refers to four core fundamental elements, what are these elements?

**Question:** We have mentioned some examples of Network Security threats such as Eavesdropping, Impersonation, Hijacking, and Denial of Service. Provide one example of each of these threats. Also, think about other Network Security Threats/Attacks that are existing?

**Exercise 1:** Consider a 16-block cipher. How many possible input blocks does this cipher have?

How many possible mappings are there? If we view each mapping as a key, then how many possible keys does this cipher have?

**Exercise 2:** Suppose n = 1000, a = 1017, and b = 1006. Use an identity of modular arithmetic to calculate in your head (a • b) mod n.

**Exercise 3:** Show that Trudy’s known-plaintext attack, in which she knows the (ciphertext, plaintext) translation pairs for seven letters, reduces the number of possible substitutions to be checked by approximately 109.

**Exercise 4:**

a) Using RSA, choose p = 3 and q = 11, and encode the word “dog” by encrypting each letter separately. Apply the decryption algorithm to the encrypted version to recover the original plaintext message.

Hint: Use the alphabetical order to determine the numerical values for letters. - See the table below. 

| Letter | m    |
| ------ | ---- |
| d      | 4    |
| o      | 15   |
| g      | 7    |

 b) Repeat part (a) but now encrypt “dog” as one message m.

**Solutions to the above exercises are available [HERE](https://canvas.bham.ac.uk/files/12122153).**

![image-20211209113138901](https://chqwer2.github.io/img/Typora/image-20211209113138901.png)

![image-20211209113743696](https://chqwer2.github.io/img/Typora/image-20211209113743696.png)

###  **Cryptography**

![image-20211209114127736](https://chqwer2.github.io/img/Typora/image-20211209114127736.png)

![image-20211209114451980](https://chqwer2.github.io/img/Typora/image-20211209114451980.png)

Symmetric Key Crypto: DES 

DES: Data Encryption Standard

### Public Key

![image-20211209121745900](https://chqwer2.github.io/img/Typora/image-20211209121745900.png)

![image-20211209121853166](https://chqwer2.github.io/img/Typora/image-20211209121853166.png)

### Modular Arithmetic

![image-20211209121920400](https://chqwer2.github.io/img/Typora/image-20211209121920400.png)

### RSA

![image-20211209122332249](https://chqwer2.github.io/img/Typora/image-20211209122332249.png)

![image-20211209122356352](https://chqwer2.github.io/img/Typora/image-20211209122356352.png)

![image-20211209122617380](https://chqwer2.github.io/img/Typora/image-20211209122617380.png)

![image-20211209122752991](https://chqwer2.github.io/img/Typora/image-20211209122752991.png)

![image-20211209123133432](https://chqwer2.github.io/img/Typora/image-20211209123133432.png)

![image-20211209123205255](https://chqwer2.github.io/img/Typora/image-20211209123205255.png)

### Practical Usage of RSA

![image-20211209123250411](https://chqwer2.github.io/img/Typora/image-20211209123250411.png)

