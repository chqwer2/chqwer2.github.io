### Tweet Samples

```python
# sample Twitter dataset from NLTK
from nltk.corpus import twitter_samples  

nltk.download('stopwords')
nltk.download('twitter_samples')

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')
```

### Stopwords with nltk and Punctuation

```python
# Python library for NLP
import nltk    
# module for stop words that come with NLTK
from nltk.corpus import stopwords          
# for string operations
import string                             

stopwords_english = stopwords.words('english') 

print('Stop words\n')
print(stopwords_english)

print('\nPunctuation\n')
print(string.punctuation)
```

### Tokenizer

```python
# module for tokenizing strings
from nltk.tokenize import TweetTokenizer   

tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)

# tokenize tweets
tweet_tokens = tokenizer.tokenize(tweet2)
```

![image-20220116111149913](https://chqwer2.github.io/img/Typora/image-20220116111149913.png)

### Re Lib

```python
# library for regular expression operations
# 正则表达式操作
import re    

print('\033[92m' + tweet)
print('\033[94m')

# remove old style retweet text "RT"
tweet2 = re.sub(r'^RT[\s]+', '', tweet)
print(tweet2)

# remove hyperlinks
tweet2 = re.sub(r'https?://[^\s\n\r]+', '', tweet2)
print(tweet2)

# remove hashtags
# only removing the hash # sign from the word
tweet2 = re.sub(r'#', '', tweet2)

print(tweet2)
```

![image-20220116110841532](https://chqwer2.github.io/img/Typora/image-20220116110841532.png)

### Stemming

NLTK has different modules for stemming and we will be using the [PorterStemmer](https://www.nltk.org/api/nltk.stem.html#module-nltk.stem.porter) module which uses the [Porter Stemming Algorithm](https://tartarus.org/martin/PorterStemmer/). Let's see how we can use it in the cell below

```python
# module for stemming
from nltk.stem import PorterStemmer 
stemmer = PorterStemmer() 
stem_word = stemmer.stem(word)  # stemming word
```

### Process Tweet

```python
from utils import process_tweet # Import the process_tweet function
tweets_stem = process_tweet(tweet); # Preprocess a given tweet
# As shown above, preprocessing consists of multiple steps before you arrive at the final list of words.
```

### Calc Frequency

```python
# Our functions for NLP
from utils import process_tweet, build_freqs 
```

