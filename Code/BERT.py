# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:33:48 2020

@author: Shaik Mathar
"""

from transformers import BertTokenizer, BertModel
import logging
import torch
import matplotlib.pyplot as plt
import re
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = []
tokenIDs = []
segmentIDs = []

model = BertModel.from_pretrained('bert-base-uncased', output_hidden_states = True)

def InputFormatting(inputText):
    global tokens
    global tokenIDs
    global segmentIDs
    
    inputText = re.sub('<.*>', '', inputText)   #Removes XML tags
    inputText = re.sub('ENDOFARTICLE.', '', inputText)  #Removes ENDOFARTICLE tag

    inputText = "[CLS]" + inputText + "[SEP]"   #Adds Special tokens
    tokens = tokenizer.tokenize(inputText)
    tokenIDs = tokenizer.convert_tokens_to_ids(tokens)
    segmentIDs = [1] * len(tokens)
    
    return tokens, tokenIDs, segmentIDs

def ExtractEmbeddings():
    global tokens
    global tokenIDs
    global segmentIDs
    global model
    
    tokenIDsTensor = torch.tensor([tokenIDs])
    segmentIDsTensor = torch.tensor([segmentIDs])
    model.eval()
    
    with torch.no_grad():
        output = model(tokenIDsTensor, segmentIDsTensor)
    print(output)
    
def main():
    text = "I have so many questions; for example: will this work (Re-moval of punctuation, I mean."

    print(text)
    print(InputFormatting(text))

    ExtractEmbeddings()