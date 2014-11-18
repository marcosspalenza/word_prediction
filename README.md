Preditor de Palavras
====================

Sistema de predição da próxima palavra de um texto. Escrito em Python 3 com banco de dados MySql.

O sistema produzido para a aula de Métodos Empíricos para Inteligência Artificial, idealiza predizer a próxima palavra após uma leitura. Para isso, ele está baseado em 45909 artigos escritos pelo jornal A Tribuna entre 2003 e 2006, cedidos à Universidade Federal do Espírito Santo. 

O sistema lê a base de dados e organiza um dicionário no banco para compreender a linguagem através da frequência de uso das palavras. Após criado seu conjunto de palavras ele utiliza do Teorema de Bayes para predizer as possíveis próximas palavras. Essa base foi subdividida em letras iniciais e as respectivas divisões à que pertenceram no jornal. O complemento então com poucas comparações e cálculos têm eficiencia na aplicação, apesar de sua demora na leitura da base.

O objetivo desse sistema é conseguir completar uma outra base de dados obtida por postagens no Twitter bem específica quanto ao assunto e com informações incompletas.
