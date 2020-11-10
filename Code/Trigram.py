# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:57:31 2020

@author: Shaik Mathar
"""

import transformers
from nltk. util import ngrams
from CorpusInfo import CorpusFileList
import re, string, collections

def MakeTrigrams():
    FileNum = 0

    while FileNum < 164:
        with open(CorpusFileList[FileNum], "r", encoding='ANSI') as file:
            text = file.read()

        text = re.sub('<.*>', '', text)
        text = re.sub('ENDOFARTICLE.', '', text)
    
        punctuationNoPeriod = "[" + re.sub("\.", "", string.punctuation) + "]"

        text = re.sub(punctuationNoPeriod, "", text)

        tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-uncased')
        tokens = tokenizer(text)
        token_ids = tokenizer.convert_tokens_to_ids(tokens)
        Trigrams = ngrams(tokens, 3)

        TokenIDsFreq = collections.Counter(token_ids)
        TrigramsFreq = collections.Counter(Trigrams)
        #TrigramsFreq.items()

        #numberOfTrigrams = len(TrigramsFreq)

        with open("C:/Dev/FYP/N-Grams/Trigrams/"+ str(FileNum) +".txt", "w") as file:
            #print(TrigramsFreq, file = file)
            for (key, value), (key2, value2) in zip(TrigramsFreq.items(), TokenIDsFreq.items()):
                print(str(key2) + ":" + str(key) + ":" + str(TrigramsFreq[key]), file = file)
    
        FileNum+=1
    
        print("Trigrams File " + str(FileNum) + " done")