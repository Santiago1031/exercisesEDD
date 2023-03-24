class nodo():
    def __init__(self, valor: str, proximo):
        self.valor: str = valor
        self.proximo = proximo

nodo4=nodo("6", None)
nodo3=nodo("5", nodo4)
nodo2=nodo("4", nodo3)
nodo1=nodo("3", nodo2)

count = 0
def contarElementosLista(nodo, count):
    count = count
    if (nodo == None):
        return 0 + count
    else:
        count = count + 1
        nodo = nodo.proximo
        return contarElementosLista(nodo, count)

print(contarElementosLista(nodo1, count))
