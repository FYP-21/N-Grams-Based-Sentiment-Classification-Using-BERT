# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:33:48 2020

@author: Shaik Mathar
"""

from transformers import BertTokenizer, BertModel
import torch
import re

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = []
tokenIDs = []
segmentIDs = []
hidden_states = []
model = BertModel.from_pretrained('bert-base-uncased', output_hidden_states = True)

def InputFormatting(inputText):
    global tokens
    global tokenIDs
    global segmentIDs
    inputText = re.sub('<.*>', '', inputText)
    inputText = re.sub('ENDOFARTICLE.', '', inputText)
    inputText = "[CLS]" + inputText + "[SEP]"
    tokens = tokenizer.tokenize(inputText)
    tokenIDs = tokenizer.convert_tokens_to_ids(tokens)
    segmentIDs = [1] * len(tokens)   
    return tokens, tokenIDs, segmentIDs

def ExtractHiddenStates():
    global tokens
    global tokenIDs
    global segmentIDs
    global model   
    tokenIDsTensor = torch.tensor([tokenIDs])
    segmentIDsTensor = torch.tensor([segmentIDs])
    model.eval()   
    with torch.no_grad():
        output = model(tokenIDsTensor, segmentIDsTensor)    
    global hidden_states
    hidden_states = output[2]
    return hidden_states
    
def CreateInputVectors():
    h = ExtractHiddenStates()
    token_Embeddings = torch.stack(h, dim=0)
    token_Embeddings = torch.squeeze(token_Embeddings, dim=1)
    token_Embeddings = token_Embeddings.permute(1, 0, 2)
    
    token_Vectors = []
    for token in token_Embeddings:
        vec = torch.cat((token[-1], token[-2], token[-3], token[-4]), dim=0)
        token_Vectors.append(vec)
        
    return token_Vectors
    
def main():
    text = "Test Line. I hope this works. Persnickety. Inchoate."
    t, tID, sID = InputFormatting(text)
    """
    print(text)
    print(t)
    print(tID)
    print(sID)
    """
    Vectors = CreateInputVectors()
    with open("inputVectors.txt", "w") as file:
        for token in Vectors:
            print(token, file = file)
    
main()