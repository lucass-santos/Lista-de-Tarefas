lista_tarefas = []
lista_tarefas_excluidas = []

def adicionar_escolhendo_popsicao(lista):
        print('******' * 6, 'Adicionar Tarefa', '******' * 6 + '\n')
        tarefa = input('Digite a tarefa a ser incluída:\n')
        posicao = input('Agora digite a posição que deseja colocar a tarefa. Ex. 1, 2 ou 3: ')
        print()
        while posicao.isnumeric() != True:
            posicao = input('Valor inválido. Por favor digite apenas números para a posição: ')
            print()

        if int(posicao) > len(lista)+1 or int(posicao) <= 0:
            print(f'Você possui {len(lista)} itens na sua lista. A posição {posicao}'+
                  f' não corresponde ao nº de tarefas da lista')
            print('Inclusão cancelada\n')
        else:
            lista.insert(int(posicao)-1, tarefa)
            print('A tarefa foi incluída com sucesso!\n')

def adicionar_tarefa(lista_tarefas):
    print('******' * 6, 'Adicionar Tarefa', '******' * 6 + '\n')
    tarefa = input('Digite a tarefa a ser incluída:\n')
    lista_tarefas.append(tarefa)
    print('A tarefa foi incluída com sucesso!\n')

def listar_tarefas(lista_tarefas):
    if len(lista_tarefas) != 0:
       print('******' * 6, 'Lista de Tarefas', '******' * 6 +'\n')
       for indice, tarefa in enumerate(lista_tarefas, 0):
          print(f'* {indice+1}: {tarefa}')
       print()
    else:
        print('Sua lista ainda não possui tarefas...\n')

def desfazer_tarefa(lista_tarefas, lista_tarefas_excluidas):
    if len(lista_tarefas) != 0:
       lista_tarefas_excluidas.append(lista_tarefas.pop())
       print('A última tarefa da lista foi removida com sucesso\n')
    else:
       print('Não há tarefas a serem removidas.\n')

def refazer_tarefa(lista_tarefas, lista_tarefas_excluidas):
    if len(lista_tarefas_excluidas) != 0:
       lista_tarefas.append(lista_tarefas_excluidas.pop())
       print('A última tarefa excluída foi recolocada na lista de tarefas\n')
    else:
       print('Não há tarefas excluídas a serem recuperadas\n')


while True:
    print('******'*6, 'Menu Lista de Tarefas', '******'*6)
    print('Opções:')
    print('[1] Adicionar tarefa\n[2] Listar Tarefas Adicionadas\n[3] Desfazer '+
          'Tarefa\n[4] Refazer Tarefa\n')
    opcao = input('Digite o número da opção desejada: ')
    print()

    if opcao == '1':
        print('******' * 6, 'Adicionar Tarefa', '******' * 6 +'\n')
        print(f'[1] Adicionar tarefa no final da lista\n'+
              f'[2] Adicionar tarefa em uma posição específica\n')
        escolha = input('Digite sua escolha: ')
        print()
        while escolha != '1' and escolha != '2':
            print('******' * 6, 'Adicionar Tarefa', '******' * 6 + '\n')
            print(f'[1] Adicionar tarefa no final da lista\n' +
                  f'[2] Adicionar tarefa em uma posição específica\n')
            escolha = input('Opção inválida. Digite apenas uma das opções acima: ')
            print()
        if escolha == '1':
            adicionar_tarefa(lista_tarefas)
        elif escolha == '2':
            adicionar_escolhendo_popsicao(lista_tarefas)
    elif opcao == '2':
        listar_tarefas(lista_tarefas)
    elif opcao == '3':
        desfazer_tarefa(lista_tarefas, lista_tarefas_excluidas)
    elif opcao == '4':
        refazer_tarefa(lista_tarefas, lista_tarefas_excluidas)
    else:
        print('O que digitou não corresponde às opções listadas...')

