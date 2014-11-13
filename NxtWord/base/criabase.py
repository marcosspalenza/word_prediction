from os import listdir
from os.path import os, isfile, join
from base import vocab, loadarchive

strLocation = os.getenv("HOME")+"/Databases/atribuna"
swords = vocab.openfiles(os.getenv("HOME")+"/Databases/stopwordsPT-BR.txt")
#lstwords = vocab.openfiles(strLocation+"/Databases/01012004at2.txt")

onlyfiles = [f for f in listdir(strLocation) if isfile(join(strLocation,f)) ]
count=0
ends = []
for f in onlyfiles:
    if not f[(len(f)-7):(len(f)-4)] in ends:
        ends.append(f[(len(f)-7):(len(f)-4)])
        vocab.newClass(f[(len(f)-7):(len(f)-4)])
    lstwords = vocab.openfiles(strLocation+"/"+f)
    lstwords = [x.lower() for x in lstwords]
    dicioList = vocab.makeObjects(lstwords,swords)
    print(count)
    loadarchive.editDicionario(dicioList, f[(len(f)-7):(len(f)-4)])
    count+=1