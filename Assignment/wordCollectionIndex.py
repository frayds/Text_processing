#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 21:17:48 2016

@author: frayd
"""
import collections

class docTFIDFIndex:  
    def dicIndexChanged(self,dic):
        count=collections.defaultdict(lambda: collections.defaultdict(int))
        for docid in dic:
            for wd in dic[docid]:
                if wd in count.keys():
                    count[wd][docid]=dic[docid][wd]
                else:
                    count[wd]={}
                    count[wd][docid]=dic[docid][wd]
        return count
        
        
        
        
        
        





    
    
        
