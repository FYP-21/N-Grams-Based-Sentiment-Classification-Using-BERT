# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:57:31 2020

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
    Trigrams = ngrams(tokenized, 3)

    TrigramsFreq = collections.Counter(Trigrams)
    #TrigramsFreq.items()

    numberOfTrigrams = len(TrigramsFreq)

    with open("C:/Dev/FYP/N-Grams/Trigrams/"+ str(FileNum) +".txt", "w") as file:
        print(TrigramsFreq, file = file)
    
    FileNum+=1
    
    print("File " + str(FileNum) + " done")
    file.close()