class No:
    def __init__(self, valor, prioridade, proximo): # Classe No quase idêntica ao que usamos em LDSE...
        self.info = valor
        self.prior = prioridade # Com exceção dessa linha, já que o No também recebe seu nível de prioridade
        self.prox = proximo

'''
    Todos os arquivos estão com explicações simples de cada linha importante.
    Caso fique com dúvidas, me chama no grupo - sem o Fabiano.

    PS: Os nomes das classes estão no padrão PascalCase. Já os arquivos, métodos
    e funções estão no padrão snake_case. Seguindo assim o
    PEP-8 (Basicamente o guia de estilo oficial do Python).
'''

class FilaDinamica: # O mesmo de sempre - quem não souber, volta um pouco nos arquivos que eu explico lá
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserir(self, valor, prioridade):
        if self.quant == 0: #Se a lista estiver vazia, insere como primeiro da fila
            self.prim = self.ult = No(valor, prioridade, None)
        else:
            self.ult.prox = self.ult = No(valor, prioridade, None) # Caso não esteja, é adicionado no fim da fila
        self.quant += 1 # Incrementa 1 ao quant
    
    def remover(self):
        if self.esta_vazia():
            return # Se a lista estiver vazia, retorna None
        elif self.quant == 1:
            self.prim = self.ult = None # Se houver somente 1 na fila, self.prim e self.ult apontam pra None
        else:
            self.prim = self.prim.prox # Caso tenha mais q 1 valor, remove o primeiro da lista e passa o self.prim ao próximo
        self.quant -= 1


    def esta_vazia(self):
        return self.quant == 0 # Caso a lista esteja vazia, retorna True

    def show(self):
        aux = self.prim # Auxiliar começa apontando para o primeiro da fila
        while aux != None: # O loop só acaba quando o auxilar for None
            print(f'Valor: {aux.info}, Prioridade: {aux.prior}', end=' | ') # Imprime as informações de cada No
            aux = aux.prox # O auxiliar passa para o próximo da fila
        print() # Imprime um espaço em branco - para deixar o terminal mais legivel na execução