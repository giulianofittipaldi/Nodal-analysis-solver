from math import e


class Res:

    id = "R"
    no1 = int
    no2 = int
    valor = float

    def __init__(self, line):
        line = line.split()
        self.no1 = int(line[1])
        self.no2 = int(line[2])
        self.valor = float(line[3])

    def addToMatrix(self, matrix):
        matrix[self.no1][self.no1] += 1 / (self.valor)
        matrix[self.no1][self.no2] += -1 / (self.valor)
        matrix[self.no2][self.no1] += -1 / (self.valor)
        matrix[self.no2][self.no2] += 1 / (self.valor)


class Cap:

    id = "C"
    no1 = int
    no2 = int
    valor = float

    def __init__(self, line):
        line = line.split()
        self.no1 = int(line[1])
        self.no2 = int(line[2])
        self.valor = float(line[3])

    def addToMatrix(self, matrix, w):
        matrix[self.no1][self.no1] += 1j * w * (self.valor)
        matrix[self.no1][self.no2] += -1j * w * (self.valor)
        matrix[self.no2][self.no1] += -1j * w * (self.valor)
        matrix[self.no2][self.no2] += 1j * w * (self.valor)


class Ind:

    id = "L"
    no1 = int
    no2 = int
    valor = float

    def __init__(self, line):
        line = line.split()
        self.no1 = int(line[1])
        self.no2 = int(line[2])
        self.valor = float(line[3])

    def addToMatrix(self, matrix, w):
        matrix[self.no1][self.no1] += 1 / (1j * w * (self.valor))
        matrix[self.no1][self.no2] += -1 / (1j * w * (self.valor))
        matrix[self.no2][self.no1] += -1 / (1j * w * (self.valor))
        matrix[self.no2][self.no2] += 1 / (1j * w * (self.valor))


class Transf:

    id = "K"
    no1 = int  # nós 1,2,3,4 -> a,b,c,d da estampa
    no2 = int
    no3 = int
    no4 = int
    M = float
    L1 = float
    L2 = float

    def __init__(self, line):
        line = line.split()
        self.no1 = int(line[1])
        self.no2 = int(line[2])
        self.no3 = int(line[4])
        self.no4 = int(line[5])
        self.M = float(line[7])
        self.L1 = float(line[3])
        self.L2 = float(line[6])

    def addToMatrix(self, matrix, w):

        T11 = self.L2 / (self.L1 * self.L2 - self.M ** 2)
        T12 = -self.M / (self.L1 * self.L2 - self.M ** 2)
        T22 = self.L1 / (self.L1 * self.L2 - self.M ** 2)

        matrix[self.no1][self.no1] += T11 / (1j * w)
        matrix[self.no1][self.no2] += -T11 / (1j * w)
        matrix[self.no1][self.no3] += T12 / (1j * w)
        matrix[self.no1][self.no4] += -T12 / (1j * w)
        matrix[self.no2][self.no1] += -T11 / (1j * w)
        matrix[self.no2][self.no2] += T11 / (1j * w)
        matrix[self.no2][self.no3] += -T12 / (1j * w)
        matrix[self.no2][self.no4] += T12 / (1j * w)
        matrix[self.no3][self.no1] += T12 / (1j * w)
        matrix[self.no3][self.no2] += -T12 / (1j * w)
        matrix[self.no3][self.no3] += T22 / (1j * w)
        matrix[self.no3][self.no4] += -T22 / (1j * w)
        matrix[self.no4][self.no1] += -T12 / (1j * w)
        matrix[self.no4][self.no2] += T12 / (1j * w)
        matrix[self.no4][self.no3] += -T22 / (1j * w)
        matrix[self.no4][self.no4] += T22 / (1j * w)


class GmV:  # fonte de corrente controlada por tensão

    id = "G"  # nós 1,2,3,4 -> a,b,c,d da estampa
    no1 = int
    no2 = int
    no3 = int
    no4 = int
    valor = float

    def __init__(self, line):
        line = line.split()
        self.no1 = int(line[1])
        self.no2 = int(line[2])
        self.no3 = int(line[3])
        self.no4 = int(line[4])
        self.valor = float(line[5])

    def addToMatrix(self, matrix):
        matrix[self.no1][self.no3] += self.valor
        matrix[self.no1][self.no4] += -self.valor
        matrix[self.no2][self.no3] += -self.valor
        matrix[self.no2][self.no4] += self.valor


class Is:  # fonte de corrente independente

    id = "I"
    tipo = str
    no1 = int
    no2 = int
    valor = int
    amp = float
    w = float
    fase = float

    def __init__(self, line):
        line = line.split()
        self.no1 = int(line[1])
        self.no2 = int(line[2])
        if line[3] == "DC":
            self.tipo = "DC"
            self.valor = float(line[4])
        else:
            self.tipo = "AC"
            self.amp = float(line[4])
            self.w = float(line[5])
            self.fase = float(line[6])

    def addToMatrix(self, I, w):
        if self.tipo == "DC":
            I[self.no1] += -self.valor
            I[self.no2] += self.valor
        else:
            I[self.no1] += -self.amp * e ** (1j * self.fase)
            I[self.no2] += self.amp * e ** (1j * self.fase)


dicComponents = {  # dicionário que associa a id de cada classe à própria classe
    Res.id: Res,
    Cap.id: Cap,
    Ind.id: Ind,
    Transf.id: Transf,
    GmV.id: GmV,
    Is.id: Is,
}
