from os.path import os
import acessodb, vocabulario

strLocation = ("C:/Datasets/atribuna/")
swords = vocabulario.openfiles("C:/Datasets/stopwordsPT-BR.txt")
#lstwords = vocab.openfiles(strLocation+"/Databases/01012004at2.txt")
onlyfiles = [f for f in os.listdir(strLocation) if f [ len(f)-4 : ] == ('.txt') ]
count = 0
ends = []
vardb = acessodb.CreateDB()
vardb.createDicionario()
for arq in onlyfiles:
    print(count)
    lstwords = vocabulario.openfiles(strLocation+"/"+arq)
    lstwords = [x.lower() for x in lstwords]
    dicioList = vocabulario.makeObjects(lstwords,swords)
    fim = arq[(len(arq)-7):(len(arq)-4)]
    vardb.editDicionario(dicioList,fim)
    count+=1