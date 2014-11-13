class Complemento():
	palavra = ""
	freq = 0
	bayes = 0
	def __init__(self, palavra_, freq_, bayes_):
		self.palavra = palavra_
		self.freq = freq_
		self.bayes = bayes_
	def incFreq(self):
		self.freq += 1
	def getBayes(self):
		return self.bayes
	def getPalavra(self):
		return self.palavra
	def getFreq(self):
		return self.freq