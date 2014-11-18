# initialize.py
class DicioObj():
    rootWord = ""
    freq = 0
    postWords = list
    def __init__(self, root_,freq_, post_):
        self.rootWord = root_
        self.freq=freq_
        self.postWords=post_
    def __str__(self):
        str_aux = (self.rootWord,str(self.freq),str(self.postWords))
        return str_aux
    def getRoot(self):
        return self.rootWord
    def getFreq(self):
        return self.freq
    def setFreqIncrem(self):
        self.freq+=1
    def setNewComplem(self,newcomp):
        self.postWords.append(newcomp)
    def getComplem(self):
        return self.postWords    
def __init__(root_, freq_, post_):
    return DicioObj(root_, freq_, post_)