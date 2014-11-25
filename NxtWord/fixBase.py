import csv
import re
import string
import acessodb

def __main__():
    data = list(csv.DictReader(open('marcocivil.csv', 'rU')))
    invalid = []
    with open("mcivil.txt", "w") as base:
            base.write("~ ~  CORREÇÃO DA BASE DE DADOS:\n")
    for line in data:
        outval = ""
        strval = str(line)
        strval = re.sub("[!.,;?]"," ", strval)
        strval = strval.split(" ")
        for p in strval:
            if p != None:
                word = ""
                if p.find("�")>=0:
                    invalid.append(p)
                    dbacc = acessodb.CreateDB()
                    if p[0] in string.ascii_uppercase:
                        print(p)      
                        word = dbacc.buscaPalavra(p[0],p.lower())
                    else:
                        for l in string.ascii_uppercase:
                            word = dbacc.buscaPalavra(l,p.lower())
                else:
                    word = p 
                outval += " "+str(word)+" "
            if len(outval)>100:
                with open("mcivil.txt", "a") as base:
                    base.write(outval+"\n")
                outval=""
    print("Processo finalizado: acessivel em mcivil.txt")
if __name__ == '__main__':
    __main__()