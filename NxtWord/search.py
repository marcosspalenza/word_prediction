import re
from os import listdir
from os.path import os, isfile, join
from unicodedata import normalize
from complemento import Complemento

def busca(palavra):
    strLocation= os.getenv("HOME")+'/Databases/data/'
    onlyfiles = [ f for f in listdir(strLocation) if isfile(join(strLocation,f)) ]
    freqTot = 0
    finalList = []
    for arq in onlyfiles:
        try:
            charI = palavra[0]
            charI = normalize("NFKD",charI).encode("ASCII","ignore").decode("ASCII")
            charI = charI.capitalize()
        except:
            print("Palavra inválida! Tente novamente...\n")        
        if arq[len(arq)-5:]==(charI+".txt"):
            line = getLines(strLocation+arq, palavra)
            line = re.sub("\n","",line)
            listaCompl = []
            if line != "":
                entrada = line [line.index("\t")+1:]
                freqTot+= int(entrada[:entrada.index("\t")])
                entrada = line [line.index("\t")+1:]
                while entrada!="":
                    if entrada.find("#")>0:
                        entrada = entrada[entrada.index("#")+1:]
                        if entrada.find("#")>0:
                            aux = entrada[:entrada.index("#")]
                        else:
                            aux = entrada
                            entrada = ""
                    listaCompl.append(aux)
                listaAux = []
                for c in listaCompl:
                    c = c.replace(",","")
                    c = c.replace(".","")
                    c = c.replace(";","")
                    c = c.replace(":","")
                    listaAux.append(c)
                for i in listaAux:
                    finalList.append(c)
    listaAux = []
    for w in finalList:
        freq = 0
        if not w  in listaAux:
            for ind in finalList:
                if w == ind:
                    freq+=1
            bayes = freq/freqTot
            obj = Complemento(w,freq,bayes)
            listaAux.append(obj)
    printval = ""
    while(len(listaAux)>0):
        mbayes = listaAux[0]
        for obj in listaAux:
            if(mbayes.getBayes()<obj.getBayes()):      
                mbayes=obj
        aux = str(mbayes.getPalavra())
        printval = printval + aux+"\n"
        listaCompl = []
        for i in listaAux:
            if not i.getPalavra() == mbayes.getPalavra():
                listaCompl.append(i)
        listaAux = listaCompl
    return printval
def getLines(local,palavra):
    read = True
    value =""
    with open(local) as f:
        for line in f.readlines():
            if read:
                if line.find("\t")>0 and palavra == line[ : line.index("\t")] :
                    value +=  line
                    read=False
            else:
                if line != "":
                    value += line
                    return value
    return ""