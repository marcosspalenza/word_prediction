# initialize.py
class WordObj():
    chars = ""
    ant = ""
    post = ""
    # The class "constructor" - It's actually an initializer 
    def __init__(self, chars_,ant_, post_):
        self.chars = chars_
        self.ant=ant_
        self.post=post_
    def __str__(self):
        strObj = (self.ant,self.chars,self.post)
        return strObj
    def getPalavra(self):
        return self.chars
    def getAnterior(self):
        return self.ant
    def getPosterior(self):
        return self.post
def __init__(chars_,ant_, post_):
    return WordObj(chars_,ant_,post_)