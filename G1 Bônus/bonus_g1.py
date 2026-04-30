'''
    Atividade Bônus G1 --> Questões práticas cobradas na G1 de 5N
'''

def remover_posteriores(self, valor): #LDDE
    if self.quant == 0: #verifica se a lista está vazia e retorna null se a condição for verdadeira
        return
    else:
        aux = self.prim #cria um auxiliar q vai iniciar apontando para o primeiro No da lista
        cont = 1 #cria um contador que inicia com 1
        while aux != None and aux.info != valor: #o loop continua enquanto o aux não apontar pra None e o aux.info for diferente do valor inserido
            aux = aux.prox #aux passa a apontar para o proximo No
            cont += 1 #contador aumenta em 1
        
        if aux == None: #verifica se aux aponta para None, se verdadeiro, retorna Null
            return
        else:
            aux.prox = None #aux.prox aponta pra None, assim os próximos Nos da lista seram excuídos automaticamente
            self.ult = aux #self.ult passa a apontar para o aux (passa a ser o novo ultimo item da lista)
    self.quant = cont #quant recebe a quantidade de itens presentes na lista

def inserir_antes(self, valor1, valor2): #LDDEC
    if self.quant == 0: #verifica se a lista está vazia e retorna null se a condição for verdadeira
        return
    else:
        aux = self.prim #cria um auxiliar q vai iniciar apontando para o primeiro No da lista
        while aux.prox != self.prim and aux.info != valor2: #o loop continua enquanto o aux.prox não for o primeiro No da lista e o aux.info for diferente do valor2 inserido
            aux = aux.prox #aux passa a apontar para o proximo No
        
        if aux.info == valor2: #verifica se o aux.info é igual ao valor2 inserido 
            aux.ant.prox = aux.ant = No(aux.ant, valor1, aux) #cria um No que aponta para os Nos na ordem correta e, também, os Nos vizinhos apontam devidamente para o No criado
            if aux == self.prim: #verifica se o aux é o primeiro valor da lista
                self.prim = aux.ant #se verdadeiro, o novo No inserido passa a ser apontado por self.prim (se torna o primeiro No da lista)
        else:
            return #se percorrer a lista inteira e não encontrar o No com o valor2, entra em else e retorna Null
        self.quant += 1 #a lista incrementa em 1