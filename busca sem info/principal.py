from Mapa import Mapa
from Pilha import Pilha
mapa = Mapa()
'''mapa.getAdjascentesCidade(mapa.mafra)'''

pilha = Pilha(5)
print("----")
print(pilha.topo)
pilha.empilhar(mapa.curitiba)
pilha.empilhar(mapa.araucaria)
pilha.empilhar(mapa.irati)
pilha.getTopo().nome
