from nltk import word_tokenize,FreqDist,ngrams
from nltk.corpus import reuters
import nltk
nltk.download('reuters','punkt')
from collections import defaultdict
import random

corpus = reuters.sents()

def preprocessing(corpus):
    tokenized_words=[]
    sequence=[]
    for sentence in corpus:
        sequence.append(sentence)
    word_dic={}
    count=1
    for words in sequence:
        words=list(map(lambda x:x.lower(),words))
        for word in words:
            if (word_dic.get(word) is None):
                word_dic.update({word:count})
            else:
                word_dic.update({word:word_dic.get(word)+1})
            if word.isalpha():    
                tokenized_words.append(word)    
    return tokenized_words

def createNgramModel(tokenized_words):
    bigram=list(ngrams(tokenized_words,2))
    frequecy_uni=FreqDist(tokenized_words)
    print(frequecy_uni.most_common(10))
    frequency_bi=FreqDist(bigram)
    print(frequency_bi.most_common(10))
    
tokens=preprocessing(corpus)

createNgramModel(tokens)


'''Part 2 of the ngram model word and sentence prediction '''
'''Create a defaultdict and assign the key as 0 if the key is not present'''
trigram = defaultdict(lambda: defaultdict(lambda: 0))

'''calculate the count of the trigram in the training set from reuters '''
for sents in reuters.sents():
    for word1, word2, word3 in ngrams(sents,3, pad_right=True, pad_left=True):
        trigram[(word1, word2)][word3] += 1
 
'''dividing the the total count of the trigrams by the count of
 each trigram to covert it into probability'''
for word1_word2 in trigram:
    total_count = float(sum(trigram[word1_word2].values()))
    for word3 in trigram[word1_word2]:
        trigram[word1_word2][word3] /= total_count

#next word predection part 2 of assignment
prediction_text_for_next_word = ["he", "is"]
sent_end=False
random_prob=random.random()
threshold=.0
while sent_end==False:
    for word in trigram[tuple(prediction_text_for_next_word[-2:])].keys():
        threshold = threshold + trigram[tuple(prediction_text_for_next_word[-2:])][word]
        '''Select the words for the prediction text in trigrams formed by the ngram model''' 
        if  threshold>=random_prob :
          prediction_text_for_next_word.append(word)
          break
    '''checking if the data set contains the text for prediction'''
    if len(prediction_text_for_next_word)>3:
        sent_end = True
    '''printing the predected Text'''
print("Next word Prediction")
print (' '.join([text_pred_nextword for text_pred_nextword in prediction_text_for_next_word if text_pred_nextword]))

# sentence prediction part 3 of assignment
prediction_text = ["he", "is"]
sent_end = False
 
while sent_end==False:
  '''to select probabilty threshold as a random number using random function '''
  probability = random.random()
  threshold=.0
  for word in trigram[tuple(prediction_text[-2:])].keys():
      threshold = threshold + trigram[tuple(prediction_text[-2:])][word]
      '''Select the words for the prediction text in trigrams formed by the model''' 
      if threshold >= probability:
          prediction_text.append(word)
          break

  '''checking if the data set contains the text for prediction'''
  if prediction_text[-2:] == [None, None]:
      sent_end = True
'''printing the predected Text'''
print("Sentence Prediction")
print (' '.join([text_pred for text_pred in prediction_text if text_pred]))


