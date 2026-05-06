from fila_dinamica import FilaDinamica # Importa a classe FilaDinamica do aquivo fila_dinamica.py

class FilaPrioridade:
    def __init__(self):
        self.fila1 = FilaDinamica() # Aqui criamos um espaço de memória para cada fila
        self.fila2 = FilaDinamica()
        self.fila3 = FilaDinamica()
        self.fila4 = FilaDinamica()

    def inserir(self, valor, prioridade): # nessa função, o valor é inserido na lista com sua respectiva prioridade
        if prioridade == 4:
            self.fila4.inserir(valor, prioridade)
        elif prioridade == 3:
            self.fila3.inserir(valor, prioridade)
        elif prioridade == 2:
            self.fila2.inserir(valor, prioridade)
        elif prioridade == 1:
            self.fila1.inserir(valor, prioridade)
        else:
            return # Se a prioridade inserida for diferente das 4 prioridades possíveis, retorna None
    
    def remover(self): # Verifica lista por lista (da maior pra menor prioridade). Remove o primeiro valor com maior prioridade
        if not self.esta_vazia(): # Verifica se todas as listas estão vazias, caso exista algum valor, a condição é verdadeira
            if not self.fila4.esta_vazia():
                self.fila4.remover()
            elif not self.fila3.esta_vazia():
                self.fila3.remover()
            elif not self.fila2.esta_vazia():
                self.fila2.remover()
            elif not self.fila1.esta_vazia():
                self.fila1.remover()
        else:
            return # Se todas as listas estiverem vazias, retorna None
    
    def esta_vazia(self): # Verifica todas as listas. Se todas estiverem vazias, retorna True
        return self.fila4.esta_vazia() and self.fila3.esta_vazia() and self.fila2.esta_vazia() and self.fila1.esta_vazia()
    
    def show(self):
        # O executar do código fica melhor se imprimirmos somente listas que não estejam vazias
        if not self.esta_vazia(): # Caso estejam todas vazias, não entrará na condição
            if not self.fila4.esta_vazia():
                self.fila4.show()
            if not self.fila3.esta_vazia():
                self.fila3.show()
            if not self.fila2.esta_vazia():
                self.fila2.show()
            if not self.fila1.esta_vazia():
                self.fila1.show()
        else:
            print('Todas as listas estão vazias!')
            return # Se chegou até aqui, é porque todas estavam vazias. Retorna None
        