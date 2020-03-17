class Ordenador:
    def __init__(self, vetor):
        self.vetor = vetor
        Ordenador.ordenar(self)

    def ordenar(self):
        elementos = len(self.vetor)-1
        ordenado = False
        while not ordenado:
            ordenado = True
            for i in range(elementos):
                if self.vetor[i] > self.vetor[i+1]:
                    self.vetor[i], self.vetor[i +
                                              1] = self.vetor[i+1], self.vetor[i]
                    ordenado = False
        print(self.vetor)
        return self.vetor
