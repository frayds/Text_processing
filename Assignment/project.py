#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
------------------------------------------------------------
USE: python <PROGNAME> (options) file1...fileN
OPTIONS:
    -h : print this help message
    -s FILE : use stoplist file FILE
    -I File : open the Queries file
    -c File : open the Documents file
------------------------------------------------------------
"""
from read_documents import ReadDocuments
from nltk.stem import PorterStemmer
from wordCollectionIndex import docTFIDFIndex
import math
import os



import sys, re, getopt, glob

opts, args = getopt.getopt(sys.argv[1:],'hs:bc:i:')
opts = dict(opts)
filenames = args

##############################
# HELP option

if '-h' in opts:
    help = __doc__.replace('<PROGNAME>',sys.argv[0],1)
    print(help,file=sys.stderr)
    sys.exit()

##############################
# the collection
if '-i' in opts:
    indexnames = glob.glob(opts['-i'])
print('INDEX-FILES:', ' '.join(indexnames))

##############################
# for naming the index file 

if '-c' in opts:
    collectionnames = glob.glob(opts['-c'])
print('COLLECTION-FILES:', ' '.join(collectionnames))

##############################
# STOPLIST option
stops = set()
if '-s' in opts:
    with open(opts['-s'],'r') as stop_fs:
        for line in stop_fs :
            stops.add(line.strip())
            

##############################
# Compute counts for individual documents
wordCollectionCount={}
wordCollection={}
wordIndexCounttf={}
newwordIndexCountnum={}
wordRE = re.compile(r'(?x) (?: [\w-]+ )')

stemmer=PorterStemmer()
##############################
# {id word TF} of each part of queries
for file in indexnames:
    documents = ReadDocuments(file)
    for doc in documents:
        sumWord=0
        wordIndexCounttf[doc.docid]={}
        newwordIndexCountnum[doc.docid]={}
        string=' '.join(doc.lines)
        for wd in wordRE.findall(string.lower()):
            sumWord+=1
            wd =stemmer.stem(wd)
            if wd not in stops:
                if wd not in wordIndexCounttf[doc.docid]:
                    wordIndexCounttf[doc.docid][wd]=1
                    newwordIndexCountnum[doc.docid][wd]=1
                else:
                    wordIndexCounttf[doc.docid][wd]+=1
                    newwordIndexCountnum[doc.docid][wd]+=1
        for wd in wordIndexCounttf[doc.docid]:
            wordIndexCounttf[doc.docid][wd]/=sumWord
filename=r'/Users/frayd/Desktop/Text processing/lab/Assignment/IndexDocuments.txt'
if os.path.exists(filename):
    print('<the indexqueries file exists....>', file=sys.stderr)
else:
    print('<writing lexicon to file....>', file=sys.stderr)
    lex = open('/Users/frayd/Desktop/Text processing/lab/Assignment/IndexQueries.txt','w')
    for docid in wordIndexCounttf:
        print(docid, end=' ', file=lex)
            #wds = sorted(wordIndexCount[docid], key=lambda x:wordIndexCount[wd][x], reverse=True)
        for wd in wordIndexCounttf[docid]:
            print('%s:%.6s' % (wd,wordIndexCounttf[docid][wd]), end=' ', file=lex)
            print(file=lex)
    lex.close()    

 

         


##############################
# {word id  {tf, idf, tf*idf}} of each part of queries
sumDocumentsWordNum=0
for file in collectionnames:
    documents= ReadDocuments(file)
    for doc in documents:
        sentenceWord=0
        wordCollectionCount[doc.docid]={}
        string=' '.join(doc.lines)
        for wd in wordRE.findall(string.lower()):
            sentenceWord+=1
            wd =stemmer.stem(wd)
            if wd not in stops:
                if wd not in wordCollectionCount[doc.docid]:
                    wordCollectionCount[doc.docid][wd]=1
                else:
                    wordCollectionCount[doc.docid][wd]+=1
        sumDocumentsWordNum+=sentenceWord
        
   


 
       
newwordCollectionCount={}
newIndex=docTFIDFIndex()
newwordCollectionCount=newIndex.dicIndexChanged(wordCollectionCount)

for wd in newwordCollectionCount:
    sumwdNum=0
    sumarcNum=1
    for docid in newwordCollectionCount[wd]:
        sumwdNum+=newwordCollectionCount[wd][docid]
    for docid in newwordCollectionCount[wd]:
        sumarcNum+=1
    for docid in newwordCollectionCount[wd]:
        wordCollectionCount[docid][wd]=math.log(3204/sumarcNum)*sumwdNum/sumDocumentsWordNum
        newwordCollectionCount[wd][docid]={'idf':math.log(3204/sumarcNum),'tf':sumwdNum/sumDocumentsWordNum,'tf*idf':math.log(3204/sumarcNum)*sumwdNum/sumDocumentsWordNum}

filename=r'/Users/frayd/Desktop/Text processing/lab/Assignment/IndexDocuments.txt'

if os.path.exists(filename):
     print('<the indexdocument file exists....>', file=sys.stderr)
else:
    print('<writing lexicon to file....>', file=sys.stderr)
    lex = open('/Users/frayd/Desktop/Text processing/lab/Assignment/IndexDocuments.txt','w')
    for wd in newwordCollectionCount:
        print(wd, end=' ', file=lex)
        #wds = sorted(wordIndexCount[docid], key=lambda x:wordIndexCount[wd][x], reverse=True)
        for docid in newwordCollectionCount[wd]:
            print('%s:%s' % (docid,newwordCollectionCount[wd][docid]), end=' ', file=lex)
            print(file=lex)
    lex.close()
  
for docid in wordIndexCounttf:
    for wd in wordIndexCounttf[docid]:
        if wd in newwordCollectionCount.keys():
            k=list(newwordCollectionCount[wd])[0]
            q=newwordCollectionCount[wd][k]['idf']
            j=wordIndexCounttf[docid][wd]
            tfidf=j*q
            wordIndexCounttf[docid][wd]=tfidf




    
##############################
#  wordCollectionCount    newwordIndexCount  
    
TopArcN=5
finalIndex={}
wordList=[]

        
   
for docid in wordIndexCounttf:
    finalIndex[docid]={}
    uppersum=0
    squwordIndexCounttfsum=0
    squwordCollectionCountsum=0
    sqetwordCollectionCount=0
    sqrtwordIndexCounttf=0
    for did in wordCollectionCount: 
        for wd in wordIndexCounttf[docid]:
            squ=wordIndexCounttf[docid][wd]*wordIndexCounttf[docid][wd]
            squwordIndexCounttfsum+=squ
            if wd in wordCollectionCount[did]:
                upper=wordIndexCounttf[docid][wd]*wordCollectionCount[did][wd]
                uppersum+=upper
            for wd1 in wordCollectionCount[did]:
                squ=wordCollectionCount[did][wd1]*wordCollectionCount[did][wd1]
                squwordCollectionCountsum+=squ
            sqetwordCollectionCount=squwordCollectionCountsum
        sqrtwordIndexCounttf=squwordIndexCounttfsum
        denominator=math.sqrt(squwordCollectionCountsum*squwordIndexCounttfsum)
        if sqetwordCollectionCount*sqrtwordIndexCounttf==0:
            finalIndex[docid][did]=0
        else:
            finalIndex[docid][did]=uppersum/denominator
        squwordCollectionCountsum=0
        sqrtwordIndexCounttf=0
        sqetwordCollectionCount=0
        sqrtwordIndexCounttf=0
        

          
                
                
print('<writing lexicon to file....>', file=sys.stderr)
lex = open('/Users/frayd/Desktop/Text processing/lab/Assignment/DocSort.txt','w')
for docid in finalIndex:
    print(docid, end=' ', file=lex)
    finalIndexSort=sorted(finalIndex[docid].items(),key=lambda v:v[1],reverse=True)
    finalIndexSort=finalIndexSort[:TopArcN]
    for part in finalIndexSort:
        for n in range(len(part)):
             if n==0:
                 print('%s' % (part[n]), end=' ', file=lex)
                 print(file=lex)
lex.close()          
        
    
        



                             
          
            



    
