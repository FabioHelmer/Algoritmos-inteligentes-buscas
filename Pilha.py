class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.topo = -1

    def isvazia(self):
        return (self.topo == -1)

    def ischeia(self):
        return (self.topo == self.tamanho-1)

    def empilhar(self, cidade):
        if not Pilha.ischeia(self):
            self.topo += 1
            self.cidades[self.topo] = cidade
        else:
            print("pilha cheia")
            return None

    def desempilhar(self):
        if not Pilha.isvazia(self):
            temp = self.cidades[self.topo]
            self.topo -= 1
            return temp
        else:
            print("pilha vazia")
            return False

    def getTopo(self):
        return self.cidades[self.topo]
