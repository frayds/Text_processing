#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 20:51:34 2016

@author: frayd
"""

import re


IndexDocCount={}
#==============================================================================
# f=open('/Users/frayd/Desktop/Text processing/lab/Assignment/IndexDocuments.txt','r') 
# lines=f.readlines()
# for line in lines :
#==============================================================================

numRE=re.compile(r'')
    
f=open('/Users/frayd/Desktop/Text processing/lab/Assignment/test.txt','r')
lines=f.readlines()
for line in lines :
    wd=line.split()
    print(wd)