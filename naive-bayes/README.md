# Naïve Bayes


## Introduction

Naïve Bayes Classifier for sentiment analysis.

The starter code in `naive_bayes.py` contains the definition of a class for the Naïve Bayes Classifier.
The `train` function of the classifier class takes a list of lines from the dataset (the format of each line is described below). 
The `classify` function takes another list of lines to be classified and returns a Python list of strings indicating the predicted class (1 or 5).

## Evaluation

Construct the best Naïve Bayes Classifier possible for the dataset. The provided test does a 90-10 split of the dataset, using 90% of the data for training and the other 10% for testing. A function is provided to calculate the F-score for evaluating the performance of the classifier on the test data.

## Data 

The dataset is in the file, `data.txt`, which contains about 13,000 reviews, each on its own line. 

Each line of data is of the form:

```
NUMBER OF STARS|ID|TEXT
```

- The number of stars is 1 or 5. 
- The text goes until a newline (`\n`). 
- The text won't contain a '|', so you can safely invoke `split('|')`.

The `f_score` function has code that shows one method of reading each line of the data.
