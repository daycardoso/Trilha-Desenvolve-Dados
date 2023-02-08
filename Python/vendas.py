#Problema que escolhi para praticar:
# Uma empresa de análise de dados está coletando informações sobre as vendas
# de produtos em diferentes lojas. Eles desejam armazenar informações sobre 
# cada produto vendido, incluindo o nome do produto, o preço de venda, 
# a quantidade vendida e o local da loja onde a venda foi realizada.
# ATRIBUTOS: nome do produto, o preço de venda, quantidade vendida e o local da loja
# ACAO: coletar os dados da venda

class Venda:
    
    def __init__(self, produto, preco, quantidade, local):
        self.produto = produto
        self.preco = preco
        self.quantidade = quantidade
        self.local = local
        

vendas = []
n = int(input("Escreva quantas vendas deseja inserir "))
while n > 0:        
# Coletando
    print("Insira abaixo separando apenas por virgula \n o nome do produto, o preço de venda, a quantidade vendida e o local da loja")
    x = [x for x in input("Enter multiple value: ").split(",")]
    if len(x) != 4:
        break
    
    produto, preco, quantidade, local = x
    venda = Venda(produto, float(preco), int(quantidade), local)
    vendas.append(venda)
    n -= 1

print("Essas são as venda coletadas:")
for venda in vendas:
    print(venda.__dict__)