from Cidade import Cidade
from Adjacente import Adjacente


class Mapa:
    portoUniao = Cidade("Porto união", 203)
    pauloFrontin = Cidade("Paulo frontin", 172)
    canoinhas = Cidade("Canoinhas", 141)
    tresBarras = Cidade("Tres barras", 131)
    saoMatheus = Cidade("Sao Matheus", 123)
    irati = Cidade("Iriti", 139)
    curitiba = Cidade("Curitiba", 0)
    palmeiras = Cidade("Palmeiras", 59)
    mafra = Cidade("Mafra", 94)
    campoLargo = Cidade("Campo Largo", 27)
    balsaNova = Cidade("Balsa nova", 41)
    lapa = Cidade("Lapa", 74)
    tijucas = Cidade("Tijucas", 56)
    araucaria = Cidade("Araucaria", 23)
    saoJose = Cidade("Sao jose", 13)
    contenda = Cidade("Contenda", 39)

    portoUniao.addAdjacentes(Adjacente(pauloFrontin, 46),
                             Adjacente(canoinhas, 78), Adjacente(saoMatheus, 87))

    pauloFrontin.addAdjacentes(Adjacente(portoUniao, 46), Adjacente(irati, 75))

    canoinhas.addAdjacentes(Adjacente(portoUniao, 78),
                            Adjacente(tresBarras, 12), Adjacente(mafra, 66))

    saoMatheus.addAdjacentes(Adjacente(portoUniao, 87), Adjacente(
        tresBarras, 43), Adjacente(lapa, 60), Adjacente(irati, 57), Adjacente(palmeiras, 77))

    irati.addAdjacentes(Adjacente(pauloFrontin, 75), Adjacente(
        saoMatheus, 57), Adjacente(palmeiras, 75))

    tresBarras.addAdjacentes(Adjacente(canoinhas, 12),
                             Adjacente(saoMatheus, 43))

    palmeiras.addAdjacentes(Adjacente(irati, 75), Adjacente(
        saoMatheus, 77), Adjacente(campoLargo, 55))

    contenda.addAdjacentes(Adjacente(lapa, 26), Adjacente(
        balsaNova, 19), Adjacente(araucaria, 18))

    lapa.addAdjacentes(Adjacente(saoMatheus, 60),
                       Adjacente(contenda, 26), Adjacente(mafra, 57))

    mafra.addAdjacentes(Adjacente(canoinhas, 66),
                        Adjacente(lapa, 57), Adjacente(tijucas, 99))

    campoLargo.addAdjacentes(Adjacente(balsaNova, 22),
                             Adjacente(palmeiras, 55), Adjacente(curitiba, 29))

    balsaNova.addAdjacentes(Adjacente(contenda, 19), Adjacente(
        campoLargo, 22), Adjacente(curitiba, 51))

    araucaria.addAdjacentes(Adjacente(contenda, 18), Adjacente(curitiba, 37))

    tijucas.addAdjacentes(Adjacente(mafra, 99), Adjacente(saoJose, 49))

    saoJose.addAdjacentes(Adjacente(tijucas, 49), Adjacente(curitiba, 15))

    curitiba.addAdjacentes(Adjacente(araucaria, 37), Adjacente(
        balsaNova, 51), Adjacente(campoLargo, 29), Adjacente(saoJose, 15))

    def getAdjascentesCidade(self, cidade):
        for i in range(len(cidade.adjacentes)):
            print(cidade.adjacentes[i].cidade.nome)
