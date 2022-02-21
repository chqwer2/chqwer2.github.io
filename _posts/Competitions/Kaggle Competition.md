# CommonLit

1. **No Dropout**, set to 0. Only for Regression.

   hidden_dropout_prob = 0 and attention_probs_dropout_prob = 0 

2. 19 models ensembled and post process

   How to post process?

   

3. **TLDR Solution**
    I made a large collection of external data. I used sentence bert (Reimers and Gurevych 2019 - https://github.com/UKPLab/sentence-transformers) to select for each excerpt in the train set the 5 most similar snippets in the external data collection. I then used a roberta-base (later on I used a roberta-base/-large ensemble) model trained on the original  training data to label the selected data. I then filtered the data on  standard error of each sample to keep roughly the same distribution as  in the train set.

   Then, I trained some different models on the pseudo-labeled data for  1-4 epochs. After training on the pseudo-labeled data, I trained each  model on the original training set. Models used in my final submission  were albert-xxlarge, deberta-large, roberta-large and electra-large. I  used ridge regression to ensemble these models.



