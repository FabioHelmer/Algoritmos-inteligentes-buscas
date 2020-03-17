class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.visitado = False
        self.adjacentes = []

    def addCidadeAdjacente(self, cidade):
        self.adjacentes.append(cidade)

    def addAdjacentes(self, *cidades):
        for cidade in cidades:
            self.adjacentes.append(cidade)

    def getAdjacentes(self):
        return self.adjacentes
