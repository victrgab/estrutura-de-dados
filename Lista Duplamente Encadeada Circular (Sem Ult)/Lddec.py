class No:

    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo

class Lddec:

    def __init__(self):
        self.prim = None
        self.quant = 0
''''

    >> Entregar somente os blocos de métodos abaixo!! <<

    PS: Se for copiar e colar, tome cuidado com os comentários e com a indentação
    pois pode ocorrer de colar automaticamente sem a indentação presente no código.

    PS 2: De prefência, tente entender a dinâmica de todo o código e fazer sozinho,
    se precisar de ajudar, me chama no grupo (O grupo sem o Fabiano).

    PS 3: Refatorando o código eu percebi que ele pode estar meio confuso, 
    se quiser ele mais passo a passo dessas linhas únicas, me chama no grupo tb.

    Bons estudos ;)

'''

def inserir_inicio(self, valor):
    if self.quant == 0: #Verifica se a lista está vazia
        self.prim = No(None, valor, None) #Cria um No que aponta para None em ambos os ponteiros (ant e prox)
        self.prim.prox = self.prim.ant = self.prim #Faz com que ambos os ponteiros apontem para o mesmo No (ant e prox)
    else:
        self.prim.ant.prox = self.prim.ant = No(self.prim.ant, valor, self.prim) #Insere o No antes do primeiro, fazendo a devida referencia de cada ponteiro
        self.prim = self.prim.ant #O novo No inserido passa a ser apontado pelo self.prim (Se torna o primeiro da lista)
    self.quant += 1 #Nunca se esqueça de atualizar o quant

def inserir_fim(self, valor):
    if self.quant == 0: #Verifica se a lista está vazia
        self.prim = No(None, valor, None) #Cria um No que aponta para Nulo em ambos os ponteiros (ant e prox)
        self.prim.prox = self.prim.ant = self.prim #Faz com que ambos os ponteiros apontem para o mesmo No (ant e prox)
    else:
        self.prim.ant.prox = self.prim.ant = No(self.prim.ant, valor, self.prim) # Insere o No depois do último, fazendo a devida referencia de cada ponteiro
    
    self.quant += 1 #Nunca se esqueça de atualizar o quant

def remover_inicio(self):
    if self.quant == 0: #Verifica se a lista está vazia
        return #Retorna nulo se a condição for verdadeira
    elif self.quant == 1: #Verifica se a lista tem somente 1 elemento
        self.prim = None #sel.prim passa apontar pra None, assim o único elemento que estava na lista deixa de existir (Garbage Collector pega ele)
    else:
        self.prim.prox.ant = self.prim.ant #Faz com que o próximo apoós o primeiro passe a apontar para o anterior ao primeiro
        self.prim = self.prim.prox #self.prim passa a apontar para o próximo do antigo primeiro No (Tornando este o novo primeiro da lista)
        self.prim.ant.prox = self.prim #O "Último" passa a apontar para o novo primeiro No
    self.quant -= 1 #Nunca se esqueça de atualizar o quant

def remover_fim(self):
    if self.quant == 0: #Verifica se a lista está vazia
        return #Retorna nulo se a condição for verdadeira
    elif self.quant == 1: #Verifica se a lista tem somente 1 elemento
        self.prim = None #sel.prim passa apontar pra None, assim o único elemento que estava na lista deixa de existir (Garbage Collector pega ele)
    else:
        self.prim.ant = self.prim.ant.ant #O "Último" passa a ser o anterior do "Último" 
        self.prim.ant.prox = self.prim #O novo "Último" passa a apontar para o primeiro.
    self.quant -= 1 #Nunca se esqueça de atualizar o quant

'''

    Pelo amor, não esquece desse quant.
    Deslizes bobos podem tornar seu Código obsoleto.

'''