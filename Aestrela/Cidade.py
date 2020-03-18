class Cidade:
    def __init__(self, nome, distaciaObjectivo):
        self.nome = nome
        self.visitado = False
        self.adjacentes = []
        self.distanciaObjetivo = distaciaObjectivo

    def addCidadeAdjacente(self, cidade):
        self.adjacentes.append(cidade)

    def addAdjacentes(self, *cidades):
        for cidade in cidades:
            self.adjacentes.append(cidade)

    def getAdjacentes(self):
        return self.adjacentes
