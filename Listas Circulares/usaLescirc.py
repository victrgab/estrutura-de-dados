import Lescirc #importa o arquivo Lescirc.py onde a classe foi criada

lista = Lescirc.Lescirc(3) #cria a lista na memória com um tamanho fixo de 3

# criei lista pequena - com tamanho 3 - pra facilitar testes de limite
print('===== Testando lista cheia =====')
lista.inserir_fim('A')
lista.inserir_fim('B')
lista.inserir_fim('C')
print('Lista esperada: A B C ')
lista.show()
print('\n')
lista.inserir_fim('D') # esse aqui deve imprimir: "A lista está cheia"

print('\n===== Circularidade (Testando a circularidade) =====')
# removi do início pra que o inicio avance pro proximo vetor
lista.remover_inicio() # remove A, e inicio vai para 1 - B 
# aqui eu inseri no fim - como o fim tava em 0, ele volta a ocupar a posição inicial
lista.inserir_fim('D') 
print('Após remover o primeiro e inserir D no fim: ')
lista.show() # Esperado: B C D

print('\n===== Inserção no início com volta no Vetor (Testando a circularidade )=====')
# atualmente o inicio está em index 1 (B), o fim em index 1 (D está na posição 0). quant=3
lista.remover_fim() # Remove D
lista.inserir_inicio('Z') # Z deve "dar a volta" para o final do vetor (posição 0)
print('Após remover o fim e inserir Z no início: ')
lista.show()

print('\n===== Verificação dos extremos e limpando a lista =====')
print(f'Primeiro atual: {lista.ver_primeiro()}')
print(f'Último atual: {lista.ver_ultimo()}')

lista.remover_inicio()
lista.remover_inicio()
lista.remover_inicio()
print('Tentando remover da lista já vazia: ')
lista.remover_fim() # esse deve imprimir: "A lista está vazia"