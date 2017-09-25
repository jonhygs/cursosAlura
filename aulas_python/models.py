
class Perfil(object):
	''' Classe padrao para Perfis de usuarios'''
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
	def imprimir(self):
		print "Nome : %s, telefone : %s, empresa : %s" % (self.nome,self.telefone,self.empresa)



#python permite passar parametros nomeaveis, portanto nao importa a ordem que os parametros sejam passados, se estiverem nomeados eles serao "ordenados"

perfil_1 = Perfil(empresa = "EQUALS", nome = "Jonhy", telefone = "Nao informado")
perfil_1.imprimir()

#podemos verificar o tipo do objeto

print type(perfil_1)


### Heranca 
class Conta(object):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def calcular_imposto(self): 
        self.saldo = self.saldo * 0.10
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, titular, saldo,bonus):
        super(ContaCorrente, self).__init__(titular, saldo)
        self.bonus = bonus

    def calcular_imposto(self):
        return super(ContaCorrente, self).calcular_imposto() + 20


conta_corrente = ContaCorrente("jonhy",300,50)

print conta_corrente.calcular_imposto()