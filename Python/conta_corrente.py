class ContaCorrente:
    
    def __init__(self, codigo_conta):
        self.codigo_conta = codigo_conta
        self.saldo = 0
        
    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return "[>> Codigo {} Saldo {} <<]".format(self.codigo_conta, self.saldo)
    

conta_da_day = ContaCorrente(26)
print(conta_da_day)

conta_da_day.deposita(2548)
print(conta_da_day)