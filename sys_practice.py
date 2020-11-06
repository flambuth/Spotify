# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 18:20:08 2020

@author: flamb
"""



import sys 
  
  
for line in sys.stdin: 
    if 'q' == line.rstrip(): 
        break
    print(f'Input : {line}') 
  
print("Exit") 
