from Mapa import Mapa


class VetorOrdenado:
    def __init__(self, tamanho):
        self.nElem = 0
        self.cidades = [None]*tamanho

    def inserir(self, cidade):
        if self.nElem == 0:
            self.cidades[0] = cidade
            self.nElem = 1
            return
        posicao = 0
        i = 0
        while i < self.nElem:
            if(cidade.distanciaObjetivo > self.cidades[posicao].distanciaObjetivo):
                posicao += 1
            i += 1
        for k in range(self.nElem, posicao, -1):
            self.cidades[k] = self.cidades[k-1]
        self.cidades[posicao] = cidade
        self.nElem += 1

    def getPrimeiro(self):
        return self.cidades[0]

    def mostrar(self):
        for i in range(0, self.nElem):
            print(
                '{} - {}'.format(self.cidades[i].nome, self.cidades[i].distanciaObjetivo))


mapa = Mapa()
vet = VetorOrdenado(5)
vet.inserir(mapa.portoUniao)  # 203
vet.inserir(mapa.pauloFrontin)  # 172
vet.inserir(mapa.balsaNova)  # 41
vet.mostrar()
print('------------------------')
vet.inserir(mapa.palmeiras)  # 59
vet.mostrar()
