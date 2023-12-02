def adicionaElementoLista(lista, elemento, posicao=None):
    if posicao is None:
        lista.append(elemento)
    else:
        lista.insert(posicao, elemento)

def removeElementoLista(lista, elemento=None, posicao=None):
    if posicao is not None:
        if posicao < len(lista):
            lista.pop(posicao)
    elif elemento is not None:
        if elemento in lista:
            lista.remove(elemento)
    else:
        raise ValueError("Deve fornecer um elemento ou posição para remover.")

def buscaElementoLista(lista, elemento):
    return elemento in lista


def insereElemento(dicionario, dado, chave, posicao=None):
    if chave not in dicionario:
        dicionario[chave] = []
    if posicao is None:
        dicionario[chave].append(dado)
    else:
        dicionario[chave].insert(posicao, dado)

def removeElemento(dicionario, dado, chave, posicao=None):
    if chave in dicionario:
        if posicao is None:
            dicionario[chave].remove(dado)
        else:
            dicionario[chave].pop(posicao)

def buscaElemento(dado, posicao, chave, dicionario):
    if chave in dicionario:
        if posicao is None:
            return dado in dicionario[chave]
        else:
            return dicionario[chave][posicao] == dado
    return False

def insereChave(dicionario, chave):
    if chave not in dicionario:
        dicionario[chave] = []
    return dicionario
