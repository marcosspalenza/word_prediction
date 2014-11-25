import string

class CreateDB():
    file = ""
    arqs = ""
    def __init__(self):
        self.file = "./arquivos/dictionary"
        self.arqs = "./arqs.txt"
    def createDicionario(self):
        open(self.arqs, mode='w')
        for l in string.ascii_uppercase:
            open(self.file+l+".txt", mode='w')
    def editDicionario(self, lst_palavras,lst_arq):
        for palavra in lst_palavras:
            try:
                word = palavra.getRoot()
                freq = palavra.getFreq()
                compls = ""
                for w in palavra.getComplem():
                    compls=(compls+"#"+w)
                l = word[0]
                l = l.upper()
                if l in string.ascii_uppercase:
                    with open(self.file+l+".txt", "a") as dicionario:
                        dicionario.write(word+"\t"+str(freq)+"\t"+compls+"\n")
            except Exception as e:
                print(e)
                pass
        for arq in lst_arq:
            try:
                with open(self.arqs, "a") as arquivos:
                    arquivos.write(arq+"\n")
            except:
                pass
    def buscaDicionario(self, palavra, nmax):
        strVal = ""
        l = palavra[0]
        l = l.upper()
        if l in string.ascii_uppercase:
            palavra = palavra.lower()
            freqAux = 0
            cmpl =[]
            with open(self.file+l+".txt", "r") as dicionario:
                for line in dicionario.readlines():
                    if line.find("\t")>0 and palavra == line[ : line.index("\t")]:
                        lAux = line[(line.index("\t")+1) : ]
                        freqAux += int(lAux[ : lAux.index("\t")])
                        lAux = lAux[(lAux.index("\t")+1) : ]
                        while lAux.find("#")>=0:
                            lAux = lAux[(lAux.index("#")+1) : ]   
                            if lAux.find("#")>=0:
                                aux =  lAux[ : (lAux.index("#"))]
                                cmpl.append(aux)
                            else: 
                                cmpl.append(lAux[:-1])
            strVal += "freq -> "+str(freqAux)
            cicnt = 0
            while len(cmpl)>0:
                if cicnt==nmax:
                    return strVal
                cicnt += 1
                strA = cmpl[0]
                num = 0
                for c in cmpl:
                    cnt = 0
                    for a in cmpl:
                        if a == c:
                            cnt+=1
                    if(cnt>num):
                        strA = c
                        num = cnt
                strVal += "\n | "+strA+" | - ["+str(num)+"]\n"
                auxL = []
                for c in cmpl:
                    if not c in strA:
                        auxL.append(c)
                cmpl = auxL
        return strVal
    def buscaPalavra(self, char, palavra):
        char = char.upper()
        with open(self.file+char+".txt", "r") as dicionario:
            for line in dicionario.readlines():
                probValue = line[ : line.index("\t")]
                if probValue != None:
                    coef = self.lev_dist(palavra,probValue)
                    if coef <= 2:
                        return probValue
    def lev_dist(self, source, target):
        if source == target:
            return 0
        slen, tlen = len(source), len(target)
        dist = [[0 for i in range(tlen+1)] for x in range(slen+1)]
        for i in range(slen+1):
            dist[i][0] = i
        for j in range(tlen+1):
            dist[0][j] = j
        for i in range(slen):
            for j in range(tlen):
                cost = 0 if source[i] == target[j] else 1
                dist[i+1][j+1] = min(
                    dist[i][j+1] + 1,   # deletion
                    dist[i+1][j] + 1,   # insertion
                    dist[i][j] + cost   # substitution
                )
        return dist[-1][-1]