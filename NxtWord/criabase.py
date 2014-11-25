from os.path import os
import acessodb, vocabulario
from os.path import expanduser

def salvaLista(lst,arquivos):
    if lst == None :
        return
    vardb = acessodb.CreateDB()    
    home = expanduser("~")
    swords = vocabulario.openfiles(home+"/Datasets/stopwordsPT-BR.txt")
    dicioAux = []
    dicioList = []
    for i in lst:
        dicioAux.append(vocabulario.makeObjects(i,swords))
    for j in dicioAux:
        for i in j :
            dicioList.append(i)
    vardb.editDicionario(dicioList,arquivos)

def __main__():
    home = expanduser("~")
    strLocation = (home+"/Datasets/atribuna/")
    onlyfiles = [f for f in os.listdir(strLocation) if f [ len(f)-4 : ] == ('.txt') ]
    acessodb.CreateDB().createDicionario()
    lstwords=[]
    arq=[]
    for i in range(len(onlyfiles)):
        lstaux = vocabulario.openfiles(strLocation+onlyfiles[i])
        arq.append(onlyfiles[i])
        lstaux = [x.lower() for x in lstaux]
        lstwords.append(lstaux)
        if i % 100 == 0:
            print(str(i))
            salvaLista(lstwords,arq)
            lstwords=[]
            arq=[]
    if lstwords != None:
        salvaLista(lstwords,arq)

if __name__ == '__main__':
    __main__()