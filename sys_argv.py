# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 17:59:17 2021
Oo-I punched some holes
And picked at my nails
Will somebody, please, push some tacks in my eyes?
@author: flamb
"""


import sys
import hashlib


data = sys.argv[1]
m = hashlib.sha1()
m.update(bytes(data, 'utf-8'))
print(m.hexdigest())