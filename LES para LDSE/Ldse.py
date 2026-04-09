class No:
    def __init__(self, valor, proximo):
        self.prim = valor
        self.prox = proximo

class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
        self.quant += 1


    def show(self):
            aux = self.prim
            while aux != None:
                print(aux.info, end=' ')
                aux = aux.prox
            print()