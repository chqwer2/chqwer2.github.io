---
layout:     post
title:      "Hugging Face NLP"
subtitle:   " \"NLP never been so easy to implement.\""
date:       2022-02-20 00:10:00
author:     "Calvchen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - NLP
    - AI 
    - ML


---

> “This course will teach you about natural language processing (NLP) using libraries from the [Hugging Face](https://huggingface.co/) ecosystem — [🤗 Transformers](https://github.com/huggingface/transformers), [🤗 Datasets](https://github.com/huggingface/datasets), [🤗 Tokenizers](https://github.com/huggingface/tokenizers), and [🤗 Accelerate](https://github.com/huggingface/accelerate) — as well as the [Hugging Face Hub](https://huggingface.co/models). It’s completely free and without ads.”

![image-20220220175250225](https://chqwer2.github.io/img/Typora/image-20220220175250225.png)

## Setup

```python
!pip install transformers
#The whole development version
#!pip install transformers[sentencepiece] 
#pip install "transformers[sentencepiece]"
import transformers
```

### Build virture env

```python
mkdir ~/transformers-course
cd ~/transformers-course

python -m venv .env

```



### Transformers, what can they do?

![image-20220220180354499](https://chqwer2.github.io/img/Typora/image-20220220180354499.png)

A bit of Transformer history

### 

- **Architecture**: This is the skeleton of the model — the definition of each layer and each operation that happens within the model. 
- **Checkpoints**: These are the weights that will be loaded in a given architecture.
- **Model**: This is an umbrella term that isn’t as precise as “architecture” or “checkpoint”: it can mean both. This course will specify *architecture* or *checkpoint* when it matters to reduce ambiguity.

## Tokenizers

![image-20220220180943937](https://chqwer2.github.io/img/Typora/image-20220220180943937.png)

#### Word-based tokenization

Each word has a specific ID. We can split the sentense by the **space** or **punctuation**.

But the total number of words can be very large, so maybe we just train it on the most frequent 10,000 words.

#### Character-based tokenization

The vocabulary is much smaller, now we can use like 256 to represent english based language.

There are much fewer out-of-vocabulary (unknown) tokens, since every word can be built from characters.

#### Subword tokenization

A combination of both methods above.

For instance, “annoyingly” might be considered a rare word and could be decomposed into “annoying” and “ly”.

<img src="https://chqwer2.github.io/img/Typora/image-20220220182034207.png" alt="image-20220220182034207" style="zoom:50%;" />

### And more! 

Unsurprisingly, there are many more techniques out there. To name a few:

- Byte-level BPE, as used in GPT-2
- WordPiece, as used in BERT
- SentencePiece or Unigram, as used in several multilingual models

### How to batch inputs together

You can’t build a sequence list with different lengths. 

Padding

![image-20220220183514903](https://chqwer2.github.io/img/Typora/image-20220220183514903.png)

```
tokenizer.pad_token_id
```

and **attention masks** is to ignore [PAD].

Most models handle sequences of up to 512 or 1024 tokens, and will crash when asked to process longer sequences.

- Use a model with a longer supported sequence length.
- Truncate your sequences.

 [Longformer](https://huggingface.co/transformers/model_doc/longformer.html) is one example, and another is [LED](https://huggingface.co/transformers/model_doc/led.html). 

### Code

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
```

We try an example below, 

```python
sequence = "Using a Transformer network is simple"
tokens = tokenizer.tokenize(sequence)

print(tokens)
```

Output:

```python
['Using', 'a', 'transform', '##er', 'network', 'is', 'simple']
```

Normally we do

```python
tokenizer(sequence)
```

Output:

```python
{'input_ids': [101, 7993, 170, 11303, 1200, 2443, 1110, 3014, 102],
 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0],
 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1]}
```

type_ids tells you which sentence the ids belong to.

**Decode，**

```python
decoded_string = tokenizer.decode([7993, 170, 11303, 1200, 2443, 1110, 3014])
```

**parameters of tokenizer**

1. padding: longest, max_length(need to specify)
2. max_length
3. truncation=True
4. return_tensors: “tf”, “pt”, “np” for tensorflow, pytorch and numpy

For input model:

```python
tokens = tokenizer(sequences, padding=True, truncation=True, return_tensors="pt")
output = model(**tokens)
```



## Fine-Tune

```python
checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)

import torch
device = torch.device("cuda")
model.to(device)
```

```python
sequences = [
    "I've been waiting for a HuggingFace course my whole life.",
    "This course is amazing!",
]
batch = tokenizer(sequences, padding=True, truncation=True, return_tensors="pt")

# This is new
batch["labels"] = torch.tensor([1, 1])

optimizer = AdamW(model.parameters())
loss = model(**batch).loss
loss.backward()
optimizer.step()
```

### Processing the data

Duplicate Question?

![image-20220220184937397](https://chqwer2.github.io/img/Typora/image-20220220184937397.png)

Logic related?

![image-20220220184953845](https://chqwer2.github.io/img/Typora/image-20220220184953845.png)

### Dynamic Padding

Pad the max_length to whole data set:

![image-20220220185343120](https://chqwer2.github.io/img/Typora/image-20220220185343120.png)

To avoid this, we pad according to the longgest sentences in the batch:

```python
from transformers import DataCollatorWithPadding

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
```

### ![image-20220220185737869](https://chqwer2.github.io/img/Typora/image-20220220185737869.png)

```python
tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)

tokenized_datasets = tokenized_datasets.remove_columns(["sentence1", "sentence2", "idx"])
tokenized_datasets = tokenized_datasets.rename_column("label", "labels")
tokenized_datasets.set_format("torch")
```

Or

```python
from torch.utils.data import DataLoader

train_dataloader = DataLoader(
    tokenized_datasets["train"], shuffle=True, batch_size=8, collate_fn=data_collator
)
eval_dataloader = DataLoader(
    tokenized_datasets["validation"], batch_size=8, collate_fn=data_collator
)
```

### Trainer API

```python
from transformers import Trainer

trainer = Trainer(
    model,
    training_args,
    epoch,
    eval_steps,
    compute_metrics=compute_metrics,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
)
```

**Train**

```python
trainer.train()
```

**Evaluation**

```python
predictions = trainer.predict(tokenized_datasets["validation"])
print(predictions.predictions.shape, predictions.label_ids.shape)
```

### Supercharge your training loop with 🤗 Accelerate 

```python
+ from accelerate import Accelerator
  from transformers import AdamW, AutoModelForSequenceClassification, get_scheduler

+ accelerator = Accelerator()

  model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)
  optimizer = AdamW(model.parameters(), lr=3e-5)

- device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
- model.to(device)

+ train_dataloader, eval_dataloader, model, optimizer = accelerator.prepare(
+     train_dataloader, eval_dataloader, model, optimizer
+ )

  num_epochs = 3
  num_training_steps = num_epochs * len(train_dataloader)
  lr_scheduler = get_scheduler(
      "linear",
      optimizer=optimizer,
      num_warmup_steps=0,
      num_training_steps=num_training_steps
  )

  progress_bar = tqdm(range(num_training_steps))

  model.train()
  for epoch in range(num_epochs):
      for batch in train_dataloader:
-         batch = {k: v.to(device) for k, v in batch.items()}
          outputs = model(**batch)
          loss = outputs.loss
-         loss.backward()
+         accelerator.backward(loss)

          optimizer.step()
          lr_scheduler.step()
          optimizer.zero_grad()
          progress_bar.update(1)
```

If you want to try this in a Notebook (for instance, to test it with TPUs on Colab), just paste the code in a `training_function()` and run a last cell with:

```
from accelerate import notebook_launcher

notebook_launcher(training_function)
```

You can find more examples in the [🤗 Accelerate repo](https://github.com/huggingface/accelerate/tree/main/examples).

### Sharing models and tokenizers

Sharing is caring. 		

- [The Hugging Face Hub](https://huggingface.co/models)

## Dataset Library

### Loading a customized dataset

```python
from datasets import load_dataset
```

![image-20220221102235951](https://chqwer2.github.io/img/Typora/image-20220221102235951.png)

### Slice and Dice

```python
drug_dataset = load_dataset("csv", data_files=data_files, delimiter="\t")
# test
drug_dataset.train_test_split(test_size=0.1, seed=42) 
# validation
drug_dataset_clean = drug_dataset.train_test_split(test_size=0.1, seed=42)

drug_dataset_clean["validation"] = drug_dataset_clean.pop("test")

### Shuffling
drug_sample = drug_dataset["train"].shuffle(seed=42).select(range(1000))

drug_sample[:3] 
## Or
drug_sample.select(indeces)

## Filter
drug_dataset = drug_dataset.filter(lambda x: x["condition"] is not None)
```

**Mapping:**

```python
def lowercase_condition(example):
    return {"condition": example["condition"].lower()}

# can be used to add a new column...
drug_dataset.map(lowercase_condition)   # super power
# Or faster..
# batched=True can accelerate.
new_drug_dataset = drug_dataset.map(
    lambda x: {"review": [html.unescape(o) for o in x["review"]]}, batched=True, num_proc=8)  

# Also
drug_dataset.add_column() 


```

**Tokenize and Split**

```python
def tokenize_and_split(examples):
    return tokenizer(
        examples["review"],
        truncation=True,
        max_length=128,
        return_overflowing_tokens=True, # this will return all data but in different chunks.
    )
# Output: [128, 49]
```

```python
tokenized_dataset = drug_dataset.map(tokenize_and_split, batched=True,
remove_columns=drug_dataset["train"].column_names)# need to do this                                    
# Otherwise will get an error
```

If we change the split function to:

```python
def tokenize_and_split(examples):
    return tokenizer(
        examples["review"],
        truncation=True,
        max_length=128,
        return_overflowing_tokens=True, 
    )
	# Extract mapping between new and old indices
    sample_map = result.pop("overflow_to_sample_mapping")
    for key, values in examples.items():
        result[key] = [values[i] for i in sample_map]
    return result

# Output: [128, 49]
```

It gives us a mapping from a new feature index to the index of the  sample it originated from. Using this, we can associate each key present in our original dataset with a list of values of the right size by  repeating the values of each example as many times as it generates new  features:

### Dataset + DataFrames =  🤗

```python
drug_dataset.set_format("pandas")  # to pandas
# Indiced...
drug_dataset["train"][:3]

```

We can do fancy chaining to compute the class distribution among the `condition` entries:

```python
frequencies = (
    train_df["condition"]
    .value_counts()
    .to_frame()
    .reset_index()
    .rename(columns={"index": "condition", "condition": "frequency"})
)
frequencies.head()
```

And once we’re done with our Pandas analysis:

```python
from datasets import Dataset

freq_dataset = Dataset.from_pandas(frequencies)
freq_dataset

# from "pandas" to "arrow":
drug_dataset.reset_format()
```

 **Saving & Reload** 

| Data format | Function                 |
| ----------- | ------------------------ |
| Arrow       | `Dataset.save_to_disk()` |
| CSV         | `Dataset.to_csv()`       |
| JSON        | `Dataset.to_json()`      |

```
drug_dataset_reloaded = load_from_disk("drug-reviews")
```

## Big data? Datasets to the rescure!

**Memory mapping & streaming**

The Pile dataset is a huge 825 GB corpus, created by [EleutherAI](https://www.eleuther.ai) for training large-scale language models.



```python
!pip install zstandard
from datasets import load_dataset

# This takes a few minutes to run, so go grab a tea or coffee while you wait :)
data_files = "https://mystic.the-eye.eu/public/AI/pile_preliminary_components/PUBMED_title_abstracts_2019_baseline.jsonl.zst"
pubmed_dataset = load_dataset("json", data_files=data_files, split="train")
pubmed_dataset
```

We can see that there are 15,518,009 rows and 2 columns in our dataset — that’s a lot!

### Magic of Memory Mapping

```python
!pip install psutil   # A simple way to measure memory usage
import psutil

# Process.memory_info is expressed in bytes, so convert to megabytes
print(f"RAM used: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} MB")

```

Here the `rss` attribute refers to the *resident set size*, which is the fraction of memory that a process occupies in RAM. 

If you’re familiar with Pandas, this result might come as a surprise because of Wes Kinney’s famous [rule of thumb](https://wesmckinney.com/blog/apache-arrow-pandas-internals/) that you typically need 5 to 10 times as much RAM as the size of your dataset.

```python
print(f"Number of files in dataset : {pubmed_dataset.dataset_size}")
size_gb = pubmed_dataset.dataset_size / (1024**3)
print(f"Dataset size (cache file) : {size_gb:.2f} GB")
```

Datasets treats each dataset as a [memory-mapped file](https://en.wikipedia.org/wiki/Memory-mapped_file), which provides a mapping between RAM and filesystem storage that allows the library to access and operate on elements of the dataset without  needing to fully load it into memory. 🤗 Datasets treats each dataset as a [memory-mapped file](https://en.wikipedia.org/wiki/Memory-mapped_file), which provides a mapping between RAM and filesystem storage that allows the library to access and operate on elements of the dataset without  needing to fully load it into memory.

Memory-mapped files can also be shared across multiple processes, which enables methods like `Dataset.map()` to be parallelized without needing to move or copy the dataset. Under the hood, these capabilities are all realized by the [Apache Arrow](https://arrow.apache.org) memory format and [`pyarrow`](https://arrow.apache.org/docs/python/index.html) library, which make the data loading and processing lightning fast.  (For more details about Apache Arrow and comparisons to Pandas, check  out [Dejan Simic’s blog post](https://towardsdatascience.com/apache-arrow-read-dataframe-with-zero-memory-69634092b1a).) To see this in action, let’s run a little speed test by iterating over all the elements in the PubMed Abstracts dataset:

```python
import timeit

code_snippet = """batch_size = 1000

for idx in range(0, len(pubmed_dataset), batch_size):
    _ = pubmed_dataset[idx:idx + batch_size]
"""

time = timeit.timeit(stmt=code_snippet, number=1, globals=globals())
print(
    f"Iterated over {len(pubmed_dataset)} examples (about {size_gb:.1f} GB) in "
    f"{time:.1f}s, i.e. {size_gb/time:.3f} GB/s"
)
```

### Streaming datasets 

```python
pubmed_dataset_streamed = load_dataset(
    "json", data_files=data_files, split="train", streaming=True # This enable data streaming
)
```

The elements from a streamed dataset can be processed on the fly using `IterableDataset.map()` 

```python
tokenized_dataset = pubmed_dataset_streamed.map(lambda x: tokenizer(x["text"]))

#  this only shuffles the elements in a predefined buffer_size
shuffled_dataset = pubmed_dataset_streamed.shuffle(buffer_size=10_000, seed=42)


next(iter(tokenized_dataset))
```

select elements from a streamed dataset using the `IterableDataset.take()` and `IterableDataset.skip()` functions, which act in a similar way to `Dataset.select()`. 

```python
pubmed_dataset_streamed.take(5)
# Skip the first 1,000 examples and include the rest in the training set
train_dataset = shuffled_dataset.skip(1000)
# Take the first 1,000 examples for the validation set
validation_dataset = shuffled_dataset.take(1000)
```

Combine Dataset

```python
from itertools import islice
from datasets import interleave_datasets

combined_dataset = interleave_datasets([pubmed_dataset_streamed, law_dataset_streamed])
```

Here we’ve used the `islice()` function from Python’s `itertools` module to select the first two examples from the combined dataset, and  we can see that they match the first examples from each of the two  source datasets.

```python
list(islice(combined_dataset, 2))
```

### Classification Problem Embedding

One popular approach is to perform *CLS pooling* on our model’s outputs, where we simply collect the last hidden state for the special `[CLS]` token. 

```python
def cls_pooling(model_output):
    return model_output.last_hidden_state[:, 0]
```

Next, we’ll create a helper function that will tokenize a list of  documents, place the tensors on the GPU, feed them to the model, and  finally apply CLS pooling to the outputs:

```python
def get_embeddings(text_list):
    encoded_input = tokenizer(
        text_list, padding=True, truncation=True, return_tensors="pt"
    )
    encoded_input = {k: v.to(device) for k, v in encoded_input.items()}
    model_output = model(**encoded_input)
    return cls_pooling(model_output)
```

### FAISS for efficient similarity search

To do this, we’ll use a special data structure in 🤗 Datasets called a *FAISS index*. [FAISS](https://faiss.ai/) (short for Facebook AI Similarity Search) is a library that provides efficient algorithms to quickly search and cluster embedding vectors.

FAISS will create a special data sturcture callde *index*

```python
embeddings_dataset.add_faiss_index(column="embeddings")
```

```python
question = "How can I load a dataset offline?"
question_embedding = get_embeddings([question]).cpu().detach().numpy()
question_embedding.shape

# Get Similarity Score
scores, samples = embeddings_dataset.get_nearest_examples(
    "embeddings", question_embedding, k=5
)
```

To Pandas

```python
import pandas as pd

samples_df = pd.DataFrame.from_dict(samples)
samples_df["scores"] = scores
samples_df.sort_values("scores", ascending=False, inplace=True)   
# df.iterrows()
```



## The 🤗Tokenizers Library

*You've got to tokenize them all* 				

### Training a new tokenizer from an old one

⚠️ Training a tokenizer is not the same as training a model! Model  training uses stochastic gradient descent to make the loss a little bit  smaller for each batch.

<img src="https://chqwer2.github.io/img/Typora/image-20220221114225821.png" alt="image-20220221114225821" style="zoom:33%;" />

We first download new [corpus](https://huggingface.co/course/chapter6/2?fw=pt) and load it.

```python
def get_training_corpus():
    return (
        raw_datasets["train"][i : i + 1000]["whole_func_string"]
        for i in range(0, len(raw_datasets["train"]), 1000)
    )


training_corpus = get_training_corpus()
```

### Training a new tokenizer 

```python
from transformers import AutoTokenizer

old_tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer = old_tokenizer.train_new_from_iterator(training_corpus, 52000)

# Saving
tokenizer.save_pretrained("code-search-net-tokenizer")
```

Upload to Hub

```python
from huggingface_hub import notebook_login

notebook_login()

huggingface-cli login

tokenizer.push_to_hub("code-search-net-tokenizer")
```

### Fast tokenizers' special powers

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased", use_fast=True) # To use Fast

encoding = tokenizer(example, return_offsets_mapping=True)
print(type(encoding))
```

<img src="https://chqwer2.github.io/img/Typora/image-20220221115927988.png" alt="image-20220221115927988" style="zoom:80%;" />

<img src="https://chqwer2.github.io/img/Typora/image-20220221115523975.png" alt="image-20220221115523975" style="zoom:67%;" />

Besides their parallelization capabilities, the key functionality of  fast tokenizers is that they always keep track of the original span of  texts the final tokens come from — a feature we call *offset mapping*. 

[QA Pipeline](https://huggingface.co/course/chapter6/4?fw=pt)

### Normalization and pre-tokenization

Before we dive more deeply into the three most common subword  tokenization algorithms used with Transformer models (Byte-Pair Encoding [BPE], WordPiece, and Unigram), we’ll first take a look at the  preprocessing that each tokenizer applies to text. 

<img src="https://huggingface.co/course/static/chapter6/tokenization_pipeline.PNG" alt="The tokenization pipeline." style="zoom:80%;" />

1. The **normalization** step involves some general cleanup, such as removing  needless whitespace, lowercasing, and/or removing accents.

2. A tokenizer cannot be trained on raw text alone. Instead, we first need to split the texts into small entities, like words. That’s where the  pre-tokenization step comes in. 

### Algorithm Overview

| Model         | BPE                                                          | WordPiece                                                    | Unigram                                                      |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Training      | Starts from a small vocabulary and learns rules to merge tokens | Starts from a small vocabulary and learns rules to merge tokens | Starts from a large vocabulary and learns rules to remove tokens |
| Training step | Merges the tokens corresponding to the most common pair      | Merges the tokens corresponding to the pair with the  best score based on the frequency of the pair, privileging pairs where  each individual token is less frequent | Removes all the tokens in the vocabulary that will minimize the loss computed on the whole corpus |
| Learns        | Merge rules and a vocabulary                                 | Just a vocabulary                                            | A vocabulary with a score for each token                     |
| Encoding      | Splits a word into characters and applies the merges learned during training | Finds the longest subword starting from the beginning that is in the vocabulary, then does the same for the rest of the word | Finds the most likely split into tokens, using the scores learned during training |

**The Byte-Pair Encoding tokenization (BPE)**

https://huggingface.co/course/chapter6/6?fw=pt Lacking

**WordPiece tokenization**



**Unigram tokenization**

### Tokenization Detail

```python
from tokenizers import (
    decoders,
    models,
    normalizers,
    pre_tokenizers,
    processors,
    trainers,
    Tokenizer,
)
```

Basic model

```python
tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))
```

Normalizer

```python
tokenizer.normalizer = normalizers.Sequence(
    [normalizers.NFD(), normalizers.Lowercase(), normalizers.StripAccents()])

print(tokenizer.normalizer.normalize_str("Héllò hôw are ü?"))
# Output: hello how are u?
```

Pre-tokenizer

```python
tokenizer.pre_tokenizer = pre_tokenizers.BertPreTokenizer()

tokenizer.pre_tokenizer.pre_tokenize_str("Let's test my pre-tokenizer.")
```

Like with normalizers, you can use a `Sequence` to compose several pre-tokenizers:

```python
pre_tokenizer = pre_tokenizers.Sequence(
    [pre_tokenizers.WhitespaceSplit(), pre_tokenizers.Punctuation()]
)
```

**Train**

```python
pecial_tokens = ["[UNK]", "[PAD]", "[CLS]", "[SEP]", "[MASK]"]
trainer = trainers.WordPieceTrainer(vocab_size=25000, special_tokens=special_tokens)

tokenizer.train_from_iterator(get_training_corpus(), trainer=trainer)
```

**Test**

```python
encoding = tokenizer.encode("Let's test this tokenizer.")
print(encoding.tokens)
```

**Warp tokenizer**

```python
from transformers import PreTrainedTokenizerFast

wrapped_tokenizer = PreTrainedTokenizerFast(
    tokenizer_object=tokenizer,
    # tokenizer_file="tokenizer.json", # You can load from the tokenizer file, alternatively
    unk_token="[UNK]",
    pad_token="[PAD]",
    cls_token="[CLS]",
    sep_token="[SEP]",
    mask_token="[MASK]",
)

```

Or

```python
from transformers import BertTokenizerFast

wrapped_tokenizer = BertTokenizerFast(tokenizer_object=tokenizer)
```

## Main NLP Tasks

### Token Classification

This generic task encompasses any problem that can be formulated as “attributing a label to each token in a sentence,” such as:

- **Named entity recognition (NER)**: Find the  entities (such as persons, locations, or organizations) in a sentence.  This can be formulated as attributing a label to each token by having  one class per entity and one class for “no entity.”
- **Part-of-speech tagging (POS)**: Mark each word in a sentence as corresponding to a particular part of speech (such as noun, verb, adjective, etc.).
- **Chunking**: Find the tokens that belong to the same entity. This task (which can be combined with POS or NER) can be formulated as attributing one label (usually `B-`) to any tokens that are at the **beginning** of a chunk, another label (usually `I-`) to tokens that are **inside a chunk**, and a third label (usually `O`) to tokens that don’t belong to any chunk.

![img]<img src="https://chqwer2.github.io/img/Typora/image-20220221122540065.png" alt="image-20220221122540065" style="zoom:50%;" />

Take The CoNLL-2003 dataset For Instance.

```python
from datasets import load_dataset

raw_datasets = load_dataset("conll2003")
```

```python
ner_feature = raw_datasets["train"].features["ner_tags"]
ner_feature
```

```python
Sequence(feature=ClassLabel(num_classes=9, 
                            names=['O', 
                                   'B-PER', 'I-PER', 
                                   'B-ORG', 'I-ORG', 
                                   'B-LOC', 'I-LOC', 
                                   'B-MISC', 'I-MISC'], names_file=None, id=None), length=-1, id=None)

label_names = ner_feature.feature.names
label_names
```

`O` means the word doesn’t correspond to any entity.

Now we decode the labels we saw earlier gives us and visualize this:

```python
words = raw_datasets["train"][0]["tokens"]
labels = raw_datasets["train"][0]["ner_tags"]
line1 = ""
line2 = ""
for word, label in zip(words, labels):
    full_label = label_names[label]
    max_length = max(len(word), len(full_label))
    line1 += word + " " * (max_length - len(word) + 1)
    line2 += full_label + " " * (max_length - len(full_label) + 1)

print(line1)
print(line2)
```

Output:

```python
'Germany \'s representative to the European Union \'s veterinary committee Werner Zwingmann said on Wednesday consumers should buy sheepmeat from countries other than Britain until the scientific advice was clearer .'
'B-LOC   O  O              O  O   B-ORG    I-ORG O  O          O         B-PER  I-PER     O    O  O         O         O      O   O         O    O         O     O    B-LOC   O     O   O          O      O   O       O'
```

<img src="https://chqwer2.github.io/img/Typora/image-20220221134743694.png" alt="image-20220221134743694" style="zoom:67%;" />

**Processing the Data**

```python
inputs = tokenizer(raw_datasets["train"][0]["tokens"], is_split_into_words=True)
```

The first rule we’ll apply is that special tokens get a label of `-100`. 

For tokens inside a word but not at the beginning, we replace the `B-` with `I-` (since the token does not begin the entity):

```python
def align_labels_with_tokens(labels, word_ids):
    new_labels = []
    current_word = None
    for word_id in word_ids:
        if word_id != current_word:
            # Start of a new word!
            current_word = word_id
            label = -100 if word_id is None else labels[word_id]
            new_labels.append(label)
        elif word_id is None:
            # Special token
            new_labels.append(-100)
        else:
            # Same word as previous token
            label = labels[word_id]
            # If the label is B-XXX we change it to I-XXX
            if label % 2 == 1:
                label += 1
            new_labels.append(label)

    return new_labels
```

The next thing that is different from our previous example is that the `word_ids()` function needs to get the index of the example we want the word IDs of  when the inputs to the tokenizer are lists of texts (or in our case,  list of lists of words), so we add that too:

```python
def tokenize_and_align_labels(examples):
    tokenized_inputs = tokenizer(
        examples["tokens"], truncation=True, is_split_into_words=True
    )
    all_labels = examples["ner_tags"]
    new_labels = []
    for i, labels in enumerate(all_labels):
        word_ids = tokenized_inputs.word_ids(i)
        new_labels.append(align_labels_with_tokens(labels, word_ids))

    tokenized_inputs["labels"] = new_labels
    return tokenized_inputs
```

We can now apply all that preprocessing in one go on the other splits of our dataset:

```python
tokenized_datasets = raw_datasets.map(
    tokenize_and_align_labels,
    batched=True,
    remove_columns=raw_datasets["train"].column_names,
)
```

### Training

We can’t just use a `DataCollatorWithPadding` like in [Chapter 3](https://huggingface.co/course/chapter3) because that only pads the inputs (input IDs, attention mask, and token type IDs). Here our labels should be padded the exact same way as the  inputs so that they stay the same size, using `-100` as a value so that the corresponding predictions are ignored in the loss computation.

```python
from transformers import DataCollatorForTokenClassification

data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)
```

test on few examples:

```python
batch = data_collator([tokenized_datasets["train"][i] for i in range(2)])
batch["labels"]
```

**Metric**

```python
#  traditional framework used to evaluate token classification prediction
!pip install seqeval 

from datasets import load_metric
metric = load_metric("seqeval")
```

This metric does not behave like the standard accuracy: it will actually take the lists of labels as strings, not integers, so we will need to  fully decode the predictions and labels before passing them to the metric. 

```python
{'MISC': {'precision': 1.0, 'recall': 0.5, 'f1': 0.67, 'number': 2},
 'ORG': {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'number': 1},
 'overall_precision': 1.0,
 'overall_recall': 0.67,
 'overall_f1': 0.8,
 'overall_accuracy': 0.89}
```

We get the precision, recall, and F1 score for each separate entity, as well as overall, here we only **take overall result**:

```python
def compute_metrics(eval_preds):
    logits, labels = eval_preds
    predictions = np.argmax(logits, axis=-1)

    # Remove ignored index (special tokens) and convert to labels
    true_labels = [[label_names[l] for l in label if l != -100] for label in labels]
    true_predictions = [
        [label_names[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    all_metrics = metric.compute(predictions=true_predictions, references=true_labels)
    return {
        "precision": all_metrics["overall_precision"],
        "recall": all_metrics["overall_recall"],
        "f1": all_metrics["overall_f1"],
        "accuracy": all_metrics["overall_accuracy"],
    }
```

**Trainer**

If we want a nice inference **widget** working like the one we saw at the  beginning of this section, it’s better to set the correct label correspondences instead.

They should be set by two dictionaries, `id2label` and `label2id`, which contain the mappings from ID to label and vice versa:

```python
id2label = {str(i): label for i, label in enumerate(label_names)}
label2id = {v: k for k, v in id2label.items()}

from transformers import AutoModelForTokenClassification

model = AutoModelForTokenClassification.from_pretrained(
    model_checkpoint,
    id2label=id2label,
    label2id=label2id,
)
```

check number of labels:

```python
model.config.num_labels
```

Fine tune

```python
from huggingface_hub import notebook_login

notebook_login()

# Or
huggingface-cli login
```

**Parameters**

```python
from transformers import TrainingArguments

args = TrainingArguments(
    "bert-finetuned-ner",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=3,
    weight_decay=0.01,
    push_to_hub=True,  # indicate that we want to save the model and evaluate it at the end of every epoch
    hub_model_id="huggingface-course/bert-finetuned-ner",
)
```

```python
from transformers import Trainer

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    compute_metrics=compute_metrics,
    tokenizer=tokenizer,
)
trainer.train()
```

Push Model

```python
trainer.push_to_hub(commit_message="Training complete")
# Get a return URL
```

Use the Fine-tuned Model

```python
from transformers import pipeline

# Replace this with your own checkpoint
model_checkpoint = "huggingface-course/bert-finetuned-ner"
token_classifier = pipeline(
    "token-classification", model=model_checkpoint, aggregation_strategy="simple"
)
token_classifier("My name is Sylvain and I work at Hugging Face in Brooklyn.")
```

History Saved: https://huggingface.co/course/chapter7/3?fw=pt

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

