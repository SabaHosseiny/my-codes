# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XUDUSv7uq8cdnoDgvSUx2mgW8KWgIRav
"""

a = int(input())
b = int(input())
k = int(input())

def func(a,b) :
    if b == 0 :
        return a
    else :
        return func( a^b , (a&b) << 1 )

print (func(a,b))

if func(a,b) == k :
    print("YES")
else :
    print("NO")