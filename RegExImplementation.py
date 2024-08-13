from nltk.book import text7
from nltk import re,FreqDist

'''converting text to tokens'''
token=text7.tokens
'''converting the tokens to lower case and removing all the non alpha characters from the text'''
lower_nonpunt=[word.lower() for word in token if re.search("\w", word)]
'''Freqdist finds the count of the words'''
word_frequency=FreqDist(lower_nonpunt).most_common(50)
'''printing the first 50 words with high frequency'''
print(word_frequency)


