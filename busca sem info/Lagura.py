from Mapa import Mapa
from Fila import Fila


class Largura:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Fila(20)
        self.fronteira.enfileirar(inicio)

    def buscar(self):
        primeiro = self.fronteira.getPrimeiro()
        print('atual:{}'.format(primeiro.nome))
        if(primeiro == self.objetivo):
            self.achou = True
        else:
            temp = self.fronteira.desenfileirar()
            print('desenfileirou:{}'.format(temp.nome))
            for a in primeiro.adjacentes:
                print('verificando se ja vitado:{}'.format(a.cidade.nome))
                if(a.cidade.visitado == False):
                    a.cidade.visitado = True
                    self.fronteira.enfileirar(a.cidade)
                    print("add-> {}".format(a.cidade.nome))
            if self.fronteira.numeroElementos > 0:
                Largura.buscar(self)


mapa = Mapa()
largura = Largura(mapa.portoUniao, mapa.pauloFrontin)
largura.buscar()
