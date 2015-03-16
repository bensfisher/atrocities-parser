from corenlp import *
from nltk import tokenize
from datetime import datetime
import os,sys
import ast
import codecs
import pandas as pd
import multiprocessing as mp
from parse import parser

starttime = datetime.now()

#file_list = []
#pattern = "*.txt"
#root = "/Users/bensfisher/stanford-corenlp-python/examples2/"
#for path, subdirs, files in os.walk(root):
#    for name in files:
#        if name.endswith((".txt")):
#            files.append(os.path.join(path,name))

files = ['AI_Report_2000_CAMEROON.txt','AI_Report_2000_AFGHANISTAN.txt',
        'AI_Report_2001_CONGO_DEMOCRATIC_REPUBLIC_OF_THE.txt','AI_Report_2000_IRELAND.txt',
        'AI_Report_2000_LIBERIA.txt','AI_Report_2000_JAPAN.txt']

pool = mp.Pool(processes=3)
results = [pool.apply_async(parser, args=(filename,)) for filename in files]
output = [p.get() for p in results]

print output

print(datetime.now()-starttime)

file_list = []
root = "/Users/bensfisher/stanford-corenlp-python/Archive/"
for path, subdirs, files in os.walk(root):
    for name in files:
        if name.endswith((".txt")):
            file_list.append(os.path.join(path,name))
