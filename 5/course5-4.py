# -*- coding: utf-8 -*-
"""Untitled23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A4PmGe6MfnpmjbQdZsZqCxZyQN-2ZbtE
"""

import re

def remove_char(text):
    characters = re.compile(r'[،:؛.؟!٬٫]+')
    new_text = characters.sub('', text)
    return new_text

outputs=[]
def search(n, sentence, word):
    sentence = remove_char(sentence)
    words = sentence.split()
    for item in words:
      if len(item) <= n:
        outputs.append(item)
      else:
        if len(word) > len(item):
            item += '_' * (len(word)-len(item))
        if len(item) > len(word):
           word += '_' * (len(item)-len(word))
        result = sum(a != b for a,b in zip(word,item))
        if result <= n:
           if item not in outputs:
               item = item.replace("_","")
               outputs.append(item)
    return outputs


n = int(input())
sentence = input()
word = input()
answer = search(n,sentence,word)
for i in answer:
    print(i)