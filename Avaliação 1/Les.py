
class Les:
    def __init__(self, tamanho):
        self.tamanho_max = tamanho
        self.vetor = [None] * self.tamanho_max
        self.quant = 0

    def get_prim(self):
        return self.vetor[0]

    def get_ult(self):
        return self.vetor[self.quant - 1]

    def get_quant(self):
        return self.quant

    def get_capacidade(self):
        return self.tamanho_max

    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1

    def remover(self, valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                for j in range(i, self.quant - 1):
                    self.vetor[j] = self.vetor[j + 1]
                self.quant -= 1

    def inserir_apos(self, valor1, valor2):
        if self.quant < self.tamanho_max:
            for i in range(self.quant):
                if self.vetor[i] == valor1:
                    for j in range(self.quant - 1, i, -1):
                        self.vetor[j + 1] = self.vetor[j]
                    self.vetor[i + 1] = valor2
                    self.quant += 1
                    return

    def inserir_antes(self, valor1, valor2):
        if self.quant < self.tamanho_max:
            for i in range(self.quant):
                if self.vetor[i] == valor1:
                    for j in range(self.quant, i, -1):
                        self.vetor[j] = self.vetor[j - 1]
                    self.vetor[i] = valor2
                    self.quant += 1
                    return

    def remover_anteriores(self, valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                idx_valor = i

                for j in range(i, self.quant):
                    self.vetor[j - idx_valor] = self.vetor[j]
                self.quant -= idx_valor
                return

    def remover_posteriores(self, valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                cont = i + 1
                for j in range(cont, self.quant):
                    self.vetor[j] = None
                self.quant = cont

    def get_index(self, valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                return f'Valor: {self.vetor[i]} - indice: {i}'
        return -1

    def get_all_index(self):
        for i in range(self.quant):
            print(f'valor: {self.vetor[i]} - endereco: {i}')
        print()

    def get_valor(self, indice):
        if self.vetor[indice]:
            return f'Valor: {self.vetor[indice]} - indice: {indice}'
        else:
            return False

    def show_reverso(self):
        for i in range(self.quant - 1, - 1, -1):
            print(self.vetor[i], end=' ')
        print()

    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=' ')
        print()

    def existe(self, valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                return True
        return False