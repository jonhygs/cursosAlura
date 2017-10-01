#-*- coding: utf8 -*-
import pandas as pd 
import numpy as np
import nltk 


stopwords = nltk.corpus.stopwords.words("portuguese") #Stopwords são as palavras frequentes na lingua portuguesa que não possuem relevancia na definição do sentido de palavras ou textos
stemmer = nltk.stem.RSLPStemmer()  #Com o stemmer pegamos apenas a raiz da palavra, vamos limpar nosso dicionario colocando os sufixos para que palavras com o mesmo sentido não sejam repetidas, como carreira e carreiras

def vetorizar_texto(texto, tradutor):
	vetor = [0] * len(tradutor)
	for palavra in texto:
		if len(palavra) > 0:
			raiz = stemmer.stem(palavra)
			if raiz in tradutor:
				posicao = tradutor[raiz]
				vetor[posicao] += 1

	return vetor


classificacao = pd.read_csv("emails.csv",encoding = 'utf-8')
textos_puros = classificacao["email"]
marcas = classificacao["classificacao"]
frases = textos_puros.str.lower()
textos_quebrados = [nltk.tokenize.word_tokenize(frase) for frase in frases] #quebrando as palavras entre palavras e pontuação

print textos_quebrados

dicionario = set()

for lista in textos_quebrados:
	validas = [stemmer.stem(palavra) for palavra in lista if palavra not in stopwords and len(palavra) > 2] #excluo de meu dicionario as palavras não relevantes na classificacao dos emails. Agora meu dicionario tem a raiz das palavras, eliminando mais de uma ocorrencia em palavras com o mesmo sentido
	dicionario.update(validas)


total_palavras = len(dicionario)
tuplas = zip(dicionario,xrange(total_palavras))
tradutor = {palavra:indice for palavra, indice in tuplas}
vetores_de_texto = [vetorizar_texto(texto, tradutor) for texto in textos_quebrados]

print len(dicionario)
print dicionario
#print vetores_de_texto

