import acessodb

def __main__():
    invar = ""
    while invar!="exit":
        acess = acessodb.CreateDB()
        try: 
            invar = input("Digite uma palavra: ")
            result = acess.buscaDicionario(invar, 5)
            print(result)
        except NameError: pass

if __name__ == '__main__':
    __main__()