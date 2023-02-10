class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __lt__(self, outra):
        if self.idade != outra.idade:
            return self.idade < outra.idade
        return self.nome < outra.nome

pessoas = [Pessoa("João", 30, "Rua A"), Pessoa("Maria", 30, "Rua B"), Pessoa("Pedro", 40, "Rua C")]


for pessoa in sorted(pessoas):
    print(pessoa.nome, pessoa.idade)