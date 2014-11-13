from search import busca

invar = ""
while invar!="exit":
    try: 
        invar = input("Digite uma palavra: ")
        saida = busca(invar) 
        print (saida)
    except NameError: pass