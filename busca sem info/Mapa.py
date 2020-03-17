from Cidade import Cidade
from Adjacente import Adjacente


class Mapa:
    portoUniao = Cidade("Porto união")
    pauloFrontin = Cidade("Paulo frontin")
    canoinhas = Cidade("Canoinhas")
    irati = Cidade("Iriti")
    palmeiras = Cidade("Palmeiras")
    campoLargo = Cidade("Campo Largo")
    curitiba = Cidade("Curitiba")
    balsaNova = Cidade("Balsa nova")
    araucaria = Cidade("Araucaria")
    saoJose = Cidade("Sao jose")
    contenda = Cidade("Contenda")
    mafra = Cidade("Mafra")
    tijucas = Cidade("Tijucas")
    lapa = Cidade("Lapa")
    saoMatheus = Cidade("Sao Matheus")
    tresBarras = Cidade("Tres barras")

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
