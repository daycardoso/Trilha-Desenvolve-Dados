# Esse exemplo tem o objetivo de deixar os conceitos de herança e polimorfismo mais claros

class Cachorro:
    def __init__(self, nome, idade, amigavel):
        self.nome = nome
        self.idade = idade
        self.amigavel = amigavel

    def gosta_de_passear(self):
        # Todo cachorro gosta depassear então sempre Thrue
        return True 
    
    def latido(self):
        return 'Woooof!'
    
class Caramelo(Cachorro):
    def __init__(self, nome, idade, amigavel):
        super().__init__(nome, idade, amigavel)
        
    def brincalhao(self):
        return "Fiquei esperando o dia todo pra você brincar comigo!"
    
    def latido(self):
        return 'AuAu Auu!'
    
class GoldenRetriever(Cachorro):
    def __init__(self, nome, idade, amigavel):
        super().__init__(nome, idade, amigavel)
        
    def bagunceiro(self):
        return "Amo fazer uma bagunça, não deixa um chinelo ou uma carteira na minha frente que eu mastigo hahhaha"
    
    #def latido(self):
    #    return 'Hauf hauf hauf!'

class HuskySiberiano(Cachorro):
    def __init__(self, nome, idade, amigavel):
        super().__init__(nome, idade, amigavel)
        
    def barulhento(self):
        return "Eu só to tentando te contar como foi o meu dia!!"
    
    def latido(self):
        return 'wuff, wuff; wau!'
        
class ViraLata(Caramelo, GoldenRetriever):
    def __init__(self, nome, idade, amigavel):
        super().__init__(nome, idade, amigavel)
        
    def latido(self):
       return 'voff, voff!'
    

bebeto = Caramelo('Bebeto', 3, 10)

print("Seu nome é {}, ele tem {} anos e seu nivel de amabilidade é {}/10".format(bebeto.nome, bebeto.idade, bebeto.amigavel))
print("Ele gosta de passear? R: {}".format(bebeto.gosta_de_passear()))

pitchula = ViraLata('Pitchula', 12, 10)

#Note que eu não declarei brincalhao ou bagunceiro em ViraLata mas ele herdou isso dos pais.
print(pitchula.brincalhao(),"\n",pitchula.bagunceiro()) 


lily = GoldenRetriever('Lily', 7, 10)
romeu = HuskySiberiano('Romeu', 5, 10)

# Usando polimorfismo
cachorros = [bebeto, pitchula, romeu, lily]
for raca in cachorros:
    print("Meu nome é {} e eu faço {}".format(raca.nome,raca.latido()))
