from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

X,Y = carregar_acessos()

porcao_treinox = X[:90]
porcao_treinoy = Y[:90]
porcao_testex = X[-9:]
porcao_testey = Y[-9:]

modelo  = MultinomialNB()
modelo.fit(porcao_treinox,porcao_treinoy)

resultado =  modelo.predict(porcao_testex)

diferencas = resultado - porcao_testey

acertos = [d for d in diferencas if d == 0]

taxa_de_acerto = (len(acertos) * 100.0)/len(porcao_testey)

print resultado,porcao_testey
print taxa_de_acerto

