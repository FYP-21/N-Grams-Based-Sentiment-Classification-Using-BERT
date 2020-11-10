# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 12:27:24 2020

@author: Shaik Mathar
"""

import transformers
from nltk.util import ngrams
from CorpusInfo import CorpusFileList
import re, string, collections

def MakeBigrams():
    FileNum = 0

    while FileNum < 164:
        with open(CorpusFileList[FileNum], "r", encoding='ANSI') as file:
            text = file.read()    
    
        text = re.sub('<.*>', '', text)
        text = re.sub('ENDOFARTICLE.', '', text)

        punctuationNoPeriod = "[" + re.sub("\.", "", string.punctuation) + "]"

        text = re.sub(punctuationNoPeriod, "", text)

        tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-uncased')
        tokens = tokenizer.tokenize(text)
        token_ids = tokenizer.convert_tokens_to_ids(tokens)
        Bigrams = ngrams(tokens, 2)

        TokenIDsFreq = collections.Counter(token_ids)
        BigramsFreq = collections.Counter(Bigrams)
        #BigramsFreq.items()

        #numberOfBigrams = len(BigramsFreq)

        with open("C:/Dev/FYP/N-Grams/Bigrams/"+ str(FileNum) +".txt", "w") as file:
            #print(BigramsFreq, file = file)
            for (key, value), (key2, value2) in zip(BigramsFreq.items(), TokenIDsFreq.items()):
                print(str(key2) + ":" + str(key) + ":" + str(BigramsFreq[key]), file = file)
    
        FileNum+=1
    
        print("Bigrams File " + str(FileNum) + " done")