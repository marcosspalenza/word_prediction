import sys
from complemento import Complemento
import mysql.connector
import re
class CreateDB():
    user = ""
    pswd = ""
    bd = ""    
    def __init__(self):
        self.bd = "dictionary"
    def createDicionario(self):
        try:
            conn = mysql.connector.connect(user="root", password="", database=self.bd)
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE PALAVRAS(
                IDWD        INT   PRIMARY KEY   AUTO_INCREMENT,
                WORD   VARCHAR(50)   NOT NULL,
                FREQ   INT     NOT NULL)''')
            cursor.execute('''CREATE TABLE COMPLEMENTOS(
                IDCP        INT   PRIMARY KEY   AUTO_INCREMENT,
                PALAVRA   VARCHAR(50)   NOT NULL,
                BASE   VARCHAR(3),
                IDPALAVRA INT    NOT NULL,
                CONSTRAINT `cplmn_palavras` FOREIGN KEY (`IDPALAVRA`)
                    REFERENCES `PALAVRAS` (`IDWD`))''')
            cursor.close()
        except mysql.connector.Error as e:
            print("[DB-ERROR] : ERRO AO ACESSAR o DB [ERRORv01]")
            print(e)
            sys.exit(1)
        print ("[Database] Estrutura criada com sucesso!");
    def editDicionario(self, lst_palavras,end):
        try :
            conn = mysql.connector.connect(user="root", password="", database=self.bd)
            cursor = conn.cursor(buffered=True)
            for palavra in lst_palavras:
                word = palavra.getRoot()
                freq = palavra.getFreq()
                cursor.execute("SELECT `IDWD` FROM PALAVRAS WHERE `WORD` = '"+word+"'")
                values = cursor.fetchone()
                if values == None:
                    fval  = palavra.getFreq()
                    query = ("INSERT INTO PALAVRAS (`IDWD`, `WORD`, `FREQ`) VALUES (NULL,'"+word+"',"+str(fval)+")")
                    cursor.execute(query)
                    gen_id = cursor.lastrowid
                    if gen_id >= 0:
                        for w in palavra.getComplem():
                            query = ("INSERT INTO COMPLEMENTOS (`IDCP`,`PALAVRA`,`BASE`,`IDPALAVRA`) VALUES (NULL,'"+w+"','"+end+"',"+str(gen_id)+")")
                            cursor.execute(query)
                else:
                    gen_id = int(values[0])
                    freq =freq+gen_id
                    cursor.execute("UPDATE PALAVRAS SET `FREQ`="+str(freq)+" WHERE `IDWD` = "+str(gen_id))
                    for w in palavra.getComplem():
                        cursor.execute("INSERT INTO COMPLEMENTOS (`IDCP`,`PALAVRA`,`BASE`,`IDPALAVRA`) VALUES (NULL,'"+w+"','"+end+"',"+str(gen_id)+")")
            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print("[DB-ERROR] : ERRO AO ACESSAR o DB [ERRORv02]")
            print(e)
            sys.exit(1)
    def buscaDicionario(self,palavra):
    #id [0] - palavra [1] - freq [2] >>> PALAVRAS 
    #id [0] - compl [1] - - base [3]  fk_id [4]
        printval=""
        try:
            conn = mysql.connector.connect(user="root", password="", database=self.bd)
            cursor = conn.cursor()
            cursor.execute("SELECT `IDWD`, `FREQ` FROM PALAVRAS WHERE `WORD` = '"+palavra+"'")
            values = cursor.fetchone()
            if values == None:
                print ("Palavra inexistente no DB!")
            else:
                listCompl = []
                ident = values[0]
                freq = int(values[1])
                cursor.execute("SELECT `PALAVRA` FROM COMPLEMENTOS WHERE `IDPALAVRA` = "+str(ident))
                compls = cursor.fetchall()
                for i in compls:
                    aux = re.sub('[.=,:;!?<>]',"",i[0])
                    listCompl.append(aux)
                lstaux = []
                for c in listCompl:
                    if not c in lstaux:
                        freqc = listCompl.count(c)
                        bayes = freqc /freq
                        obj = Complemento(c,freqc,bayes)
                        lstaux.append(obj)
                while len(lstaux)>0:
                    obj = lstaux[0]
                    for compl in lstaux:
                        if obj.getBayes()<compl.getBayes():
                            obj = compl
                    aux = str(obj.getPalavra())
                    printval = printval + aux+"\n"
                    listaCompl = []
                    for i in lstaux:
                        if i.getPalavra() != obj.getPalavra():
                            listaCompl.append(i)
                    lstaux = listaCompl
            conn.close()
        except mysql.connector.Error as e:
            print("[DB-ERROR] : ERRO AO ACESSAR o DB [ERRORv03]")
            print(e)
            sys.exit(1)
        return printval  