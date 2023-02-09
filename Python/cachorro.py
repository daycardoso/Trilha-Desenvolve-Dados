class Cachorro:
    def __init__(self, nome, idade, amigavel):
        self.nome = nome
        self.idade = idade
        self.amigavel = amigavel

    def gosta_de_passear(self):
        # Todo cachorro gosta depassear então sempre Thrue
        return True 
    
class Caramelo(Cachorro):
    def __init__(self, nome, idade, amigavel):
        super().__init__(nome, idade, amigavel)
       
class GoldenRetriever(Cachorro):
    def __init__(self, nome, idade, amigavel):
        super().__init__(nome, idade, amigavel)

class HuskySiberiano(Cachorro):
    def __init__(self, nome, idade, amigavel):
        super().__init__(nome, idade, amigavel)

