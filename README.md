Preditor de Palavras
====================

Sistema de predição da próxima palavra de um texto. Escrito em Python 3.4.

O sistema produzido para a aula de Métodos Empíricos para Inteligência Artificial, idealiza predizer a próxima palavra após uma leitura. Para isso, ele está baseado em 45909 artigos em .txt escritos pelo jornal A Tribuna entre 2003 e 2006, cedidos à Universidade Federal do Espírito Santo. 

O sistema lê a base de dados e organiza um dicionário em alguns .txt para compreender a linguagem através da frequência de uso das palavras. Após criado seu conjunto (denominado dicionário) ele utiliza o método Naive Bayes para predizer as possíveis próximas palavras dada a entrada do usuário ou corrigir palavras com caracteres incorretos por meio da distância de levenshtein. Para isso, essa base foi subdividida nas letras iniciais de cada palavra para facilitar a busca e reduzir os arquivos evitando sobrecarga na leitura e/ou visualização dos mesmos. O complemento então com poucas comparações e cálculos têm certa eficiência na aplicação, apesar de sua demora na criação da base.

O objetivo desse sistema é conseguir completar uma outra base de dados obtida por postagens no Twitter bem específica quanto ao assunto e com informações incompletas.

Requisitos
====================
- [Python 3.4](https://www.python.org/downloads/)
