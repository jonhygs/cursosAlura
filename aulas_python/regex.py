import re

# a funcao match pequisa em uma string um padrao e guarda em uma variavel
resultado = re.match("[pP]y","python")

print resultado.group()

#se quisermos  procurar por qualquer silaba que acompanha y fazemos :

resultado = re.match("[a-zA-Z]y","python")

print resultado.group()

# o metodo match procura pelo primeiro padrao e para, se quisermos encontrar todos os padroes precisamos do metodo findall

resultado = re.findall("[a-zA-Z]y","python Python")

print resultado

# para retornar a palavra de onde o padrao foi encontrado, basta definir o caracter +, que define um ou mais caracteres apos o padrao encontrado

resultado = re.findall('([A-Za-z]y[A-Za-z]+)','python Python ou py')

print resultado

#zero ou mais caracteres apos o padrao

resultado = re.findall('([A-Za-z]y[A-Za-z]*)','python Python ou py')

print resultado


resultado = re.findall(r'([A-Za-z]y\w*)','python Python ou py')

print resultado

#verifica se a palavra termina com um numero, determinados pelo $ e \d

resultado = re.findall(r'([A-Za-z]y\w*\d$)','2python Python ou py2')

print resultado