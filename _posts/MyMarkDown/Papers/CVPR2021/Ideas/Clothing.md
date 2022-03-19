## Toward AI fashion design: An Attribute-GAN model for clothing match

investigates clothing match rules based on semantic attributes

Attributed-GAN

![image-20211113190338640](https://chqwer2.github.io/img/Typora/image-20211113190338640.png)

![image-20211113205028487](https://chqwer2.github.io/img/Typora/image-20211113205028487.png)





## Clothing generation by multi-modal embedding: A compatibility matrix-regularized GAN model

[pdf](https://reader.elsevier.com/reader/sd/pii/S0262885621000020?token=605965EF308D1BF5D8E265A1C0CAE67627993A18B35578A583236393F8DB94E0670391AFCCF04DB59A4E7A5811DDA670&originRegion=eu-west-1&originCreation=20211113184223)

Clothing compatibility learning

image + text **->** latent features **->** style space.

To verify the proposed model,
we train an Inception-v3 classification model to evaluate the authenticity of synthesized images, a
regression scoring VGG model to measure the compatibility degree of the generated image pairs and a deep attentional multimodal
similarity model to evaluate the semantic similarity between generated images and ground truth text descriptions.

![image-20211113185113176](https://chqwer2.github.io/img/Typora/image-20211113185113176.png)







## ClothGAN: generation of fashionable Dunhuang clothes using generative adversarial networks

[pdf](https://www.tandfonline.com/doi/epub/10.1080/09540091.2020.1822780?needAccess=true)

![image-20211113205752691](https://chqwer2.github.io/img/Typora/image-20211113205752691.png)



### A Generative Model of People in Clothing

[pdf](https://openaccess.thecvf.com/content_iccv_2017/html/Lassner_A_Generative_Model_ICCV_2017_paper.html) ICCV 2017

1 semantic segmentation of the body and clothing

2 conditional model on the resulting segments that creates realistic images. 

<img src="https://chqwer2.github.io/img/Typora/image-20211113210633389.png" alt="image-20211113210633389" style="zoom:50%;" /><img src="https://chqwer2.github.io/img/Typora/image-20211113210641483.png" alt="image-20211113210641483" style="zoom:50%;" />



# Ours

**Dall.e**

Mano + Style + Scene

1. 时尚风格data， cloth data, Mano（3D）
2. 爬数据
3. 怎么包衣服+shape， cloth->3D body
4. Dall.e Demo
5. Dalle 的精确度和精细化，语言的模糊描述

![image-20211116082353697](https://chqwer2.github.io/img/Typora/image-20211116082353697.png)

[8:44 AM] Chloe Huang A **thin** woman in a **STYLE\* coat** **running** in the rain

\1. dalle demo
 \2. clothes dataset +mano?
 \3. combine clothes with 3D body model
 \4. ask jing about the topic (training gpu)



电影， 单个人的bodyshape, 

TPU trained Dall.e, 

![image-20211116083824254](https://chqwer2.github.io/img/Typora/image-20211116083824254.png)
