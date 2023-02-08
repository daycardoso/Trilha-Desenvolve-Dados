# Exemplo dado em aula de Python Collections part 1
class ContaCorrente:
    
    def __init__(self, codigo_conta):
        self.codigo_conta = codigo_conta
        self.saldo = 0
        
    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return "[>> Codigo {} Saldo {} <<]".format(self.codigo_conta, self.saldo)
    

conta_da_day = ContaCorrente(57)
conta_da_day.deposita(2548)

conta_do_luca = ContaCorrente(2765)
conta_do_luca.deposita(1250)

contas = [conta_da_day,conta_do_luca]
for conta in contas:
  print(conta)

def deposita_para_todos(contas):
    for conta in contas: 
        conta.deposita(200)

deposita_para_todos(contas)
print(contas[0],contas[1])

contas = (conta_da_day,conta_do_luca)

contas[0].deposita(300)

for conta in contas:
  print(conta)