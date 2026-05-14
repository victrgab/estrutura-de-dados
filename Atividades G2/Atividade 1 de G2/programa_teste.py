from fila_prioridade import FilaPrioridade

'''
    Este aqui eu achei mais interessante utilizar exemplos mais reais.
    Nesse caso, imaginei que seria melhor pra visualizar se fosse com
    o exemplo de um hospital - onde tem o nível de emergencia de cada 
    paciente.

    PS: Nesse caso, cada No recebe o nome do paciente como self.info e o
    nível de emergência como self.prior
'''

fp = FilaPrioridade() # cria o objeto 

print('\n===== TESTANDO INSERIR =====') 
fp.inserir("José Matheus", 1) # Utiliza a função inserir no objeto, passando os devidos atributos (valor, prioridade)
fp.inserir("Jordana Mendes", 2)
fp.inserir("Marcelo", 2)
fp.inserir("(PACIENTE NÃO IDENTIFICADO)", 4)

print('\nFilas após as inserções: ')
fp.show() # Utiliza a função show no objeto, mostrando todas as filas que não estão vazias

print('\nVerificar a quantidade de pacientes de cada lista: ') # Também é possível ver o quant de cada lista
print(f'Tamanho da lista 4: {fp.fila4.quant}')
print(f'Tamanho da lista 3: {fp.fila3.quant}')
print(f'Tamanho da lista 2: {fp.fila2.quant}')
print(f'Tamanho da lista 1: {fp.fila1.quant}')

print('\n===== TESTANDO REMOVER =====')
fp.remover() #  Remove o valor com maior prioridade primeiro (prioriade 4)
fp.remover() #  Remove o primeiro valor com maior prioridade atual (a fila2 é a maior prioridade atualmente)

print('\nFilas após as remoções: ')
fp.show()

print('\n===== TESTANDO REMOVER TODOS =====')
while not fp.esta_vazia(): #    O loop continua enquanto todas as listas não estiverem vazias
    fp.remover()

print('\n — O print após a remoção está na próxima sessão :p')

print('\n===== TESTANDO POSSIBILIDADES =====')

print('\n"E se eu tentar imprimir após todas as listas estarem vazias?" ')
print('\n — Ok! Veja o que acontece:\n')
fp.show()

print('\n"Tá. Mas e se eu tentar remover após todas as listas estarem vazias?" ')
fp.remover() 
fp.remover()


print('\n — Nada acontece, pois existe um tratamento de erros para caso o usuário tente isso. Veja:\n')
fp.show()

print('\n"Entendi. E se eu tentar inserir um paciente com a prioridade fora das 4 específicadas?" ')
fp.inserir("Paciente Indesejado", 5)

print('\n — Nada! Também existe um tratamento de erros para caso o usuário tente isso. Veja:\n')
fp.show()

'''
    PS: Para alguns, este código possui muitas linhas desnecessárias,
    visto que a ideia principal era somente testar o código. MASSS
    eu também achei interessante testar possíveis hipóteses de quem
    está lendo o código.

    PS 2: Espero que também tenha ajudado aqueles que não haviam entendido 
    bem o conteúdo. Qualquer coisa, me chama no grupo - sem o Fabiano.
'''
