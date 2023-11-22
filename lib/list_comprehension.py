#!/usr/bin/env python3

def return_evens(num_list):
   
    evens = [n for n in num_list if n % 2 == 0]
    return evens
    pass

num_list=[0, 1, 3, 5, 7, 8, 9]
output=return_evens(num_list)
print(output)

def make_exclamation(sentence_list):
    exclaimed_sentences=[sentence+'!'for sentence in sentence_list]
    return exclaimed_sentences
    pass

sentence_list=["Hello", "I'm doing great", "Python is fun"]
output=make_exclamation(sentence_list)
print(output)

