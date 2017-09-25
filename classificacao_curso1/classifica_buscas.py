import pandas as pd 
from sklearn.naive_bayes import MultinomialNB

# subimos os dados do csv com o pandas atraves da dataframes df
df = pd.read_csv('buscas.csv')
#podemos separar os dados atraves de seus headers
X_df = df[['home','busca','logado']]
Y_df = df['comprou']

#o panda reconhece variaveis categoricas, e organiza os dummies em categorias

Xdummies = pd.get_dummies(X_df).astype(int)

#print (Xdummies)

#para jogar nossos dados no modelo, devemos transformar os frames em arrays

X = Xdummies.values
Y = Y_df.values

#funcao generica para dividir os dados em treinamento e teste
porcentagem_treino = 0.9

tamanho_treinamento = porcentagem_treino * len(Y)
tamanho_teste = len(Y) - tamanho_treinamento

#dividindo os dados em porcao de treinamento e teste
porcao_treinamentoX = X[:int(tamanho_treinamento)]
porcao_treinamentoY = Y[:int(tamanho_treinamento)]
porcao_testeX  = X[int(-tamanho_teste):]
porcao_testeY = Y[int(-tamanho_teste):]

#podemos agora colocar nossos dados em nosso 
modelo = MultinomialNB()
modelo.fit(porcao_treinamentoX,porcao_treinamentoY)
resultado = modelo.predict(porcao_testeX)

diferencas = resultado - porcao_testeY

acertos = [d for d in diferencas if d == 0]

taxa_de_acerto = (len(acertos) * 100.0)/len(porcao_testeY)

print taxa_de_acerto
