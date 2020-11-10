# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:51:53 2020

@author: Shaik Mathar
"""

import transformers
from nltk.util import ngrams
from CorpusInfo import CorpusFileList
import re, string, collections

def MakeUnigrams():
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
        Unigrams = ngrams(tokens, 1)
        
        TokenIDsFreq = collections.Counter(token_ids)
        UnigramsFreq = collections.Counter(Unigrams)
        #UnigramsFreq.items()

        #numberOfUnigrams = len(UnigramsFreq)

        with open("C:/Dev/FYP/N-Grams/Unigrams/"+ str(FileNum) +".txt", "w") as file:
            #print(UnigramsFreq, file = file)
            for (key, value), (key2, value2) in zip(UnigramsFreq.items(), TokenIDsFreq.items()):
                print(str(key2) + ":" + str(key) + ":" + str(UnigramsFreq[key]), file = file)
    
        FileNum+=1
    
        print("Unigrams File " + str(FileNum) + " done")