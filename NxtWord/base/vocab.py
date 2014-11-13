import re
from codecs import open
import string
import os
from base import loadarchive, wordObj
from base.dicioObj import DicioObj

def openfiles(arquivo):
    wordgroup = []
    wordCount = 0
    arq = open(arquivo, encoding="iso8859_1")
    for line in arq:
        for word in line.split():
            wordgroup.append(word)
            wordCount += 1
    return (wordgroup)
def makeObjects(baselist,swords):
    newList = []
    for i in range(len(baselist)):
        anterior = ""
        posterior = ""
        palavra = baselist[i]
        if not palavra in swords:
            if wordVerify(baselist[i-1]) and i>0:
                anterior = baselist[i-1]
            if wordVerify(palavra) and i<(len(baselist)-1): 
                posterior = baselist[i+1]
            newList.append(wordObj.makeWord(palavra,anterior,posterior))
    return makeDicioObjs(newList) 
def wordVerify(word_):
    if word_.find('.')==-1 and word_.find('!')==-1 and word_.find('?')==-1 and word_.find(';')==-1:
        return True
    else: 
        return False
def makeDicioObjs(baselist):
    objList = []
    for i in baselist:
        newWord = True
        for obj in objList:
            if cleaner(obj.getRoot()) == cleaner(i.getPalavra()):
                ind = objList.index(obj)
                post = cleaner(i.getPosterior())
                if not post == "":
                    objList[ind].setNewComplem(post)
                objList[ind].setFreqIncrem()
                newWord=False
        if newWord:
            objList.append(insertNewWord(i))    
    return objList
def insertNewWord(wordObject):
    wordPosList = []
    palavra = cleaner(wordObject.getPalavra())
    post = cleaner(wordObject.getPosterior())
    wordPosList.append(post)
    dicioUn = DicioObj(palavra, 1, wordPosList)
    return dicioUn
def cleaner(word):
    nword = re.sub('\W\d','',word)
    return nword
def newClass(endstr):
    for alfa in string.ascii_uppercase:
        if not os.path.isfile(os.getenv("HOME")+"/Databases/data/"+endstr+alfa+".txt"):
            loadarchive.createDicionario(os.getenv("HOME")+"/Databases/data/"+endstr+alfa+".txt")