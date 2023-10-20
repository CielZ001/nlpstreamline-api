# Introduction
Hello! This is a brief introduction for this api tool.
This tool could be used for streamlining your NLP process.

# Basice Text Processing
This is a function that could preprocess your str. It could:
    1. Lowercase all words
    2. Remove URLs
    3. Tokenize the string into individual words
    4. Remove punctuations
    5. Remove stopwords    

This function will return a string after done all of these works.

To use it:
```
import requests
response = requests.get('https://nlpstreamline-api-5b8e6f695807.herokuapp.com/basic_text_processing', params={'raw_str': "Good morning! I'm a student from the University of Toronto. I'm studying computer science."})
print(response.text)
```
The 'raw_str' is the str you want to process. It will return a string.

# Basic NLP Processing

This function will process your raw str to stemmed and lemmatized words list.
To use it:
```
import requests
response = requests.get('https://nlpstreamline-api-5b8e6f695807.herokuapp.com/nlp_text_processing', params={'raw_str': "Good morning! I'm a student from the University of Toronto. I'm studying computer science."})
print(response.text)
```
It will return a list which contains all words after stemmed and lemmatized.
The stemming method is Snowball Stemmer, and the Lemmatizer is called WordNet.

# N-gram Generation and Counter 
This function could generate n grams.    
To use it:
```
import requests
# Return 2 grams and their frequency
response = requests.get('https://nlpstreamline-api-5b8e6f695807.herokuapp.com/n_gram_generation', params={'raw_str': "Good morning! I'm a student from the University of Toronto. I'm studying computer science.", 'n': 2})
print(response.text)
```
It will return a dictionary containing all n grams ranked from the highest frequency to the lowest one.
n must be a positive number.

Github Repo: https://github.com/CielZ001/nlpstreamline-api
