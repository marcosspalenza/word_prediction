import vocabulario, acessodb
invar = ""
while invar!="exit":
    acess = acessodb.CreateDB()
    try: 
        invar = input("Digite uma palavra: ")
        saida = acess.buscaDicionario(invar)
        print (saida)
    except NameError: pass