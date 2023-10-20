from flask import Flask, request
import re
import nltk
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import string
from typing import List
from collections import Counter
from nltk.util import ngrams

app = Flask(__name__)


@app.route('/')
def index():
    intro = """
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
    
    ```

    
    """
    return 'Hello World!'


@app.route('/basic_text_processing')
def basic_text_processing():
    """

    A function that could preprocess your str. It could:
        1. Lowercase all words
        2. Remove URLs
        3. Tokenize the string into individual words
        4. Remove punctuations
        5. Remove stopwords    

    This function will return a string after done all of these works.

    """

    raw_str = request.args.get('raw_str')

    # Lowercase all words
    content = raw_str.lower()

    # Remove URLs from the content using regular expressions
    content_without_urls = re.sub(r"http\S+", "", content)
    contents = re.sub(r"www\S+", "", content_without_urls)

    # Tokenize the string into individual words
    words = nltk.word_tokenize(contents)

    # Remove stopwords and punctuation from the list of words
    stop_words = set(stopwords.words('english'))

    punctuations = set(string.punctuation)
    filtered_words = []
    for word in words:
        if word not in stop_words:
            filtered_word = ''.join(
                ch for ch in word if ch not in punctuations)
            if filtered_word:
                filtered_words.append(filtered_word)

    final_str = " ".join(filtered_words)

    return final_str


@app.route('/nlp_text_processing')
def nlp_text_processing():
    """

    This function will process your raw str to stemmed and lemmatized words list.
    It will return a list which contains all words after stemmed and lemmatized.
    The stemming method is Snowball Stemmer, and the Lemmatizer is called WordNet.

    """

    raw_str = request.args.get('raw_str')

    # Lowercase all words
    content = raw_str.lower()

    # Remove URLs from the content using regular expressions
    content_without_urls = re.sub(r"http\S+", "", content)
    contents = re.sub(r"www\S+", "", content_without_urls)

    # Tokenize the string into individual words
    words = nltk.word_tokenize(contents)

    # Remove stopwords and punctuation from the list of words
    stop_words = set(stopwords.words('english'))

    punctuations = set(string.punctuation)
    filtered_words = []
    for word in words:
        if word not in stop_words:
            filtered_word = ''.join(
                ch for ch in word if ch not in punctuations)
            if filtered_word:
                filtered_words.append(filtered_word)

    processed_str = filtered_words

    # Stem the filtered words using the Snowball stemmer
    stemmer = SnowballStemmer('english')
    stemmed_words = []
    for word in processed_str:
        stemmed_word = stemmer.stem(word)
        stemmed_words.append(stemmed_word)

    # Lemmatize the stemmed words using the WordNet lemmatizer
    lemma = nltk.wordnet.WordNetLemmatizer()
    lemma_words = []
    for word in stemmed_words:
        lemma_word = lemma.lemmatize(word)
        lemma_words.append(lemma_word)

    return lemma_words


@app.route('/n_gram_generation')
def n_gram_generation():
    """

    This function could generate n grams.    
    It will return a dictionary containing all n grams ranked from the highest frequency to the lowest one.
    n must be a positive number.

    """

    raw_str = request.args.get('raw_str')
    n = request.args.get('n')

    # Lowercase all words
    content = raw_str.lower()

    # Remove URLs from the content using regular expressions
    content_without_urls = re.sub(r"http\S+", "", content)
    contents = re.sub(r"www\S+", "", content_without_urls)

    # Tokenize the string into individual words
    words = nltk.word_tokenize(contents)

    # Remove stopwords and punctuation from the list of words
    stop_words = set(stopwords.words('english'))

    punctuations = set(string.punctuation)
    filtered_words = []
    for word in words:
        if word not in stop_words:
            filtered_word = ''.join(
                ch for ch in word if ch not in punctuations)
            if filtered_word:
                filtered_words.append(filtered_word)

    processed_str = filtered_words

    # Stem the filtered words using the Snowball stemmer
    stemmer = SnowballStemmer('english')
    stemmed_words = []
    for word in processed_str:
        stemmed_word = stemmer.stem(word)
        stemmed_words.append(stemmed_word)

    # Lemmatize the stemmed words using the WordNet lemmatizer
    lemma = nltk.wordnet.WordNetLemmatizer()
    lemma_words = []
    for word in stemmed_words:
        lemma_word = lemma.lemmatize(word)
        lemma_words.append(lemma_word)

    # Process raw string using basice text processing function and NLP processing function
    nlp_processed_words = lemma_words

    if n > 0:
        # generate a list of ngram
        n_gram = ngrams(nlp_processed_words, n)
        # Count the frequency of each ngram in the list
        n_gram_count = Counter(n_gram)
        # Sort the word counts in descending order
        sorted_word_counts = sorted(
            n_gram_count.items(), key=lambda x: x[1], reverse=True)

        return sorted_word_counts
    else:
        return print('n must be a positive number!')


# Run the application
if __name__ == '__app__':
    app.run(threaded=True, port=5000)
