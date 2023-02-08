# Problema que escolhi para praticar:
# Você precisa desenvolver uma solução para gerenciar as contas
# bancárias de um grupo de clientes. Cada conta bancária tem um
# número de conta, o nome do titular da conta e o saldo atual. 
# Sua solução deve permitir que os clientes consultem o saldo 
# de sua conta, façam depósitos e saques.
# ATRIBUTOS: Numero de conta, o nome do titular da conta e o saldo atual
# ACOES: Deposito, saque, consulta saldo
class ContaBancaria:
    
    def __init__(self, titular, numero_conta,saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    def consulta(self):
        print("{} com conta numero({}) seu saldo atual: {} \n".format(self.titular,self.numero_conta,self.saldo))
    
    def deposito(self,valor):
        self.saldo += valor
        print("{} com conta numero({}) voce fez um deposito no valor de {} \n Seu novo saldo: {} \n".format(self.titular,self.numero_conta,valor,self.saldo))
        
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("{} com conta numero({}) voce fez um saque no valor de {} \n Seu novo saldo: {} \n".format(self.titular,self.numero_conta,valor,self.saldo))
        else :
            print("Saldo insuficiente")
    
conta_day = ContaBancaria("Dayana", 123, 2000)
conta_day.consulta()
conta_day.deposito(250)
conta_day.saque(750)
conta_day.saque(2000)