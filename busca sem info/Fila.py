from Mapa import Mapa


class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numeroElementos = 0

    def isVazia(self):
        return self.numeroElementos == 0

    def isCheia(self):
        return self.tamanho == self.numeroElementos

    def getPrimeiro(self):
        return self.cidades[self.inicio]

    def getFim(self):
        return self.cidades[self.fim]

    def enfileirar(self, cidade):
        if not Fila.isCheia(self):
            if self.fim == self.tamanho-1:
                self.fim = -1
            self.fim += 1
            self.cidades[self.fim] = cidade
            self.numeroElementos += 1
        else:
            print("fila cheia")

    def desenfileirar(self):
        if not Fila.isVazia(self):
            temp = self.cidades[self.inicio]
            self.inicio += 1
            if self.inicio == self.tamanho:
                self.inicio = 0
            self.numeroElementos -= 1
            return temp
        else:
            print("fila vazia")
            return None

    def getCidades(self, fila):
        for i in range(self.inicio, self.fim+1):
            print(self.cidades[i].nome)
