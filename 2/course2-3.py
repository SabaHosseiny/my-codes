# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BjzOP9Pcrl2QOWbPuy-DidSuYX-ipc2Y
"""

based_list=[]
def num_base(counter , b):
    final=""
    while counter > 0:
      baghi_mande = counter%b
      final = str(baghi_mande) + final
      counter //= b
    return final

while True :
    n , b = map(int, input().split())
    if n == -1 and b == -1 :
       break
    else :
      counter=0
      if 1 < b < 10 :
       for i in range (1 , n+1) :
         if (n)%i == 0 :
           counter += i
       based_list.append(num_base(counter,b))

      else :
         print("invalid base!")
         exit()

listed_num = 0
for i in based_list :
   listed_num += int(i)
print(listed_num)