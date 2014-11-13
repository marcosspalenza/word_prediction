from unicodedata import normalize
import os

def createDicionario(local):
    with open(local, "w") as text_file:
        print("", file=text_file)
def editDicionario(lst_palavras,end):
    for palavra in lst_palavras:
        word = palavra.getRoot()
        try:
            charI = word[0]
        except:
            pass 
        charI = normalize("NFKD",charI).encode("ASCII","ignore").decode("ASCII")
        charI = charI.capitalize()
        local = os.getenv("HOME")+'/Databases/data/'+end+charI+'.txt'
        if os.path.isfile(local):
            line = removeLine(local, palavra.getRoot())
            if line == "":
                word = word+'\t'+str(palavra.getFreq())+'\t'
                for c in palavra.getComplem():
                    if c != "":
                        word=word+'#'+c  
            else:
                aux = line[line.index("\t")+1:]
                freq = int(aux[:aux.index("\t")])
                freq+= palavra.getFreq()
                complm = aux[aux.index("\t")+1:]
                word=word+str(freq)+complm
                for c in palavra.getComplem():
                    if c != "":
                        word=word+'#'+c
            word = word +'\n'
            with open(local, "a") as text_file:
                print(word, file=text_file)
def removeLine(original,palavra):
    value = ""
    auxiliar = original[:-4] +"AUX.txt"
    with open(original) as f, open(auxiliar, "w") as subst:
        for line in f.readlines():
            if line.find("\t")>0 and palavra == line[ : line.index("\t")] :
                value =  line
            else:
                subst.write(line)
        os.rename(auxiliar, original)
    return value