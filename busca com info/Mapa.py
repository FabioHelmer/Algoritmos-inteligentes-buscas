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

    portoUniao.addAdjacentes(Adjacente(pauloFrontin),
                             Adjacente(canoinhas), Adjacente(saoMatheus))

    pauloFrontin.addAdjacentes(Adjacente(portoUniao), Adjacente(irati))

    canoinhas.addAdjacentes(Adjacente(portoUniao),
                            Adjacente(tresBarras), Adjacente(mafra))

    saoMatheus.addAdjacentes(Adjacente(portoUniao), Adjacente(
        tresBarras), Adjacente(lapa), Adjacente(irati), Adjacente(palmeiras))

    irati.addAdjacentes(Adjacente(pauloFrontin), Adjacente(
        saoMatheus), Adjacente(palmeiras))

    tresBarras.addAdjacentes(Adjacente(canoinhas),
                             Adjacente(saoMatheus))

    palmeiras.addAdjacentes(Adjacente(irati), Adjacente(
        saoMatheus), Adjacente(campoLargo))

    contenda.addAdjacentes(Adjacente(lapa), Adjacente(
        balsaNova), Adjacente(araucaria))

    lapa.addAdjacentes(Adjacente(saoMatheus),
                       Adjacente(contenda), Adjacente(mafra))

    mafra.addAdjacentes(Adjacente(canoinhas),
                        Adjacente(lapa), Adjacente(tijucas))

    campoLargo.addAdjacentes(Adjacente(balsaNova),
                             Adjacente(palmeiras), Adjacente(curitiba))

    balsaNova.addAdjacentes(Adjacente(contenda), Adjacente(
        campoLargo), Adjacente(curitiba))

    araucaria.addAdjacentes(Adjacente(contenda), Adjacente(curitiba))

    tijucas.addAdjacentes(Adjacente(mafra), Adjacente(saoJose))

    saoJose.addAdjacentes(Adjacente(tijucas), Adjacente(curitiba))

    curitiba.addAdjacentes(Adjacente(araucaria), Adjacente(
        balsaNova), Adjacente(campoLargo), Adjacente(saoJose))

    def getAdjascentesCidade(self, cidade):
        for i in range(len(cidade.adjacentes)):
            print(cidade.adjacentes[i].cidade.nome)
