# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 12:27:24 2020

@author: Shaik Mathar
"""

from nltk. util import ngrams
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

        tokenized = text.split()
        Bigrams = ngrams(tokenized, 2)
    
        BigramsFreq = collections.Counter(Bigrams)
        #BigramsFreq.items()

        #numberOfBigrams = len(BigramsFreq)

        with open("C:/Dev/FYP/N-Grams/Bigrams/"+ str(FileNum) +".txt", "w") as file:
            #print(BigramsFreq, file = file)
            for key in BigramsFreq.keys():
                print(str(key) + ":" + str(BigramsFreq[key]), file = file)
    
        FileNum+=1
    
        print("Bigrams File " + str(FileNum) + " done")