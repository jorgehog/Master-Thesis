# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:47:43 2013

@author: jorgen
"""

import os, sys, re

cwd = os.getcwd()

sources = []

excludeSource = ["ch04QM.tex", "lst.tex", "ImpVal.tex", "makeFolderStruct.tex", "HarmonicOscillator.tex", "hydrogenic.tex", "appendixMatrix.tex", "3DHO.tex", "hydrogenic.tex", "HarmonicOscillator.tex"]

for root, dirs, files in os.walk(cwd):

    for f in files:
        if f.endswith(".tex") and f not in excludeSource:
            sources.append(os.path.join(root, f))



#excludePatterns = [r"\\begin", r"\\end"]

#words = {}

searchFor = sys.argv[1]

succ = 0
for s in sources:
    with open(s, 'r') as tex:
        
        raw = tex.read()
        
        if re.findall(searchFor, raw):
            print "found in  ", os.path.split(s)[-1], len(re.findall(searchFor, raw))
            
        else:
            succ += 1
        
if succ == len(sources):
    print "Success"

"""        
        for word in raw:
            word = word.strip(".").strip(",").strip(":").strip(";")
            if word.lower() in words.keys():
                words[word.lower()] += 1
            else:
                words[word.lower()] = 1
                
                

for key, value in sorted(words.items(), key=lambda x: x[1]):
    print key, value
    
"""