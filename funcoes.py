import numpy as np
from estampas import *


def readLines(
    fileName,
):  # abre o arquivo e transforma cada linha em um objeto de uma lista
    with open(f"{fileName}.txt") as file:
        lines = file.read().splitlines()
    return lines


# varre a lista de linhas e determina os componentes através da string de "id", associando-os aos respectivos objetos criados nas estampas
def createComponents(linesList):
    components = []
    ids = ["R", "C", "L", "K", "G", "I"]
    for line in linesList:
        if line[0] not in ids:
            pass
        else:
            id = line[0]
            component = dicComponents[id](
                line=line
            )  # cria o objeto cuja id corresponde a classe presente no dicionário, com data passado como parâmetro
            components.append(component)
    return components


def matrixSize(
    components,
):  # Avaliamos o tamanho da matriz, através do maior nó dentre os componentes
    maiorNo = 0
    for component in components:
        if component.id == "K" or component.id == "G":
            if maiorNo < max(
                component.no1, component.no2, component.no3, component.no4
            ):
                maiorNo = max(
                    component.no1, component.no2, component.no3, component.no4
                )
        else:
            if maiorNo < max(component.no1, component.no2):
                maiorNo = max(component.no1, component.no2)
    return maiorNo


def zeroMatrix(
    maiorNo,
):  # Criamos uma matriz de 0's para ser preenchida (Inclusive com a linha 0 e coluna 0, para não haver conflito ao adicionarmos os componentes)
    Gn = []
    I = []
    for lines in range(0, maiorNo + 1, 1):
        I.append(0)
        Gn.append([])
        for columns in range(0, maiorNo + 1, 1):
            Gn[lines].append(0)
    return Gn, I


def determineFrequency(components):
    frequency = 0
    for component in components:
        if component.id == "I" and component.tipo == "AC":
            frequency = component.w
    return frequency


def popZero(
    Gn, I
):  # Retiramos as linhas e colunas referentes ao nó zero criadas na matriz
    Gn.pop(0)
    I.pop(0)
    for lines in Gn:
        lines.pop(0)
    return Gn, I


def buildMatrix(Gn, I, w, components):
    for component in components:
        if component.id == "L" or component.id == "C" or component.id == "K":
            component.addToMatrix(Gn, w)
        elif component.id == "I":
            component.addToMatrix(I, w)
        else:
            component.addToMatrix(Gn)
    popZero(Gn, I)
    return


def solveCircuit(Gn, I):

    G = np.array(Gn)
    Iv = np.array(I)
    e = np.linalg.solve(G, Iv)
    return e
