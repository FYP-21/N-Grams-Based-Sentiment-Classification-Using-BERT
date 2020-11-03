# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 12:27:24 2020

@author: Shaik Mathar
"""

from nltk. util import ngrams
from CorpusInfo import CorpusFileList
import re, string, collections

FileNum = 0

while FileNum < 164:
    with open(CorpusFileList[FileNum], "r", encoding='ANSI') as file:
        text = file.read()    
    file.close()
    
    text = re.sub('<.*>', '', text)
    text = re.sub('ENDOFARTICLE.', '', text)

    punctuationNoPeriod = "[" + re.sub("\.", "", string.punctuation) + "]"

    text = re.sub(punctuationNoPeriod, "", text)

    tokenized = text.split()
    Bigrams = ngrams(tokenized, 2)

    BigramsFreq = collections.Counter(Bigrams)
    #BigramsFreq.items()

    numberOfBigrams = len(BigramsFreq)

    with open("C:/Dev/FYP/N-Grams/Bigrams/"+ str(FileNum) +".txt", "w") as file:
        print(BigramsFreq, file = file)
    
    FileNum+=1
    
    print("File " + str(FileNum) + " done")
    file.close()