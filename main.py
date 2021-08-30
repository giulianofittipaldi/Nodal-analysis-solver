from funcoes import *


def main():
    fileName = input("nome do arquivo")
    linelist = readLines(fileName)
    components = createComponents(linelist)
    maiorNo = matrixSize(components)
    Gn, I = zeroMatrix(maiorNo)
    w = determineFrequency(components)
    buildMatrix(Gn, I, w, components)
    e = solveCircuit(Gn, I)
    print("----------------------------------------------")
    print("Matriz Gn")
    for lines in Gn:
        print(lines)
    print("")
    print("*")
    print("")
    print("Vetor e")
    print(e)
    print("")
    print("=")
    print("")
    print("Vetor I")
    print(I)
    print("----------------------------------------------")

    return


main()
