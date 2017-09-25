# Cria uma tupla de com os tipos de convites
lista_convites = ('normal','vip','meia')

print lista_convites

#podemos concatenar tuplass

lista_convites = lista_convites + ('cortesia',)

print lista_convites

#python possui tipagem forte que nao permite uma concatenao de uma tupla com uma lista por exemplo
#lista_convites = lista_convites + ['luxo']
#para realizar a concatenacao desses tipo, devemos deixar explicito nosso desejo

lista_convites = lista_convites + tuple(['luxo'])

print lista_convites

#podemos pegar o maior numero de uma lista ou tupla 

print max(lista_convites) 

#ou o menor

print min(lista_convites)

#Se preciso de valores para esses convites posso usar dicionarios

lista_convites_com_valor = {'normal' : 60, 'vip' : 120, 'meia' : 30, }

#podemos buscar no dicionario um valor buscando por sua chave, irei buscar o valor do convite normal

print lista_convites_com_valor, lista_convites_com_valor["normal"]

# Sempre que e inserido um valor com uma chave ja existente no dicionario, esse valor e substituido
# na lista abaixo normal 12 foi inserido depois, portanto o 12 substituiu o valor 60
lista_convites_com_valor = {'normal' : 60, 'vip' : 120, 'meia' : 30, 'normal' : 12 }

print lista_convites_com_valor, lista_convites_com_valor["normal"]

#podemos pegar separadamente as chaves e os valores do dicionario

print lista_convites_com_valor.keys(),lista_convites_com_valor.values()
