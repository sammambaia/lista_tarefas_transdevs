# Inicializando variáveis
lista_de_tarefas = []
continuar = True
vazia = False

# Definindo funções
def adicionar_tarefa(tarefa):
    lista_de_tarefas.append(tarefa)
    return lista_de_tarefas

def listar_tarefas():
    if lista_de_tarefas == []:
                print (f"{'-'*25}\nLista de tarefas vazia.")
                vazia = True
                return vazia
    else:
        vazia = False
        print (f"{'-'*25}\nTarefas:")
        indice = 1
        for tarefa in lista_de_tarefas:
            print (f"{indice}: {tarefa}")
            indice += 1
        return vazia

def remover_tarefas(numero_tarefa):
    print (f'{"-"*25}\nTarefa "{lista_de_tarefas[numero_tarefa]}" removida!')
    lista_de_tarefas.pop(numero_tarefa)
    return lista_de_tarefas

def exibir_menu():
    print(
        f"{'-'*25}\nEscolha uma opção:\n" \
        "1 - Inserir nova tarefa.\n" \
        "2 - Listar todas as tarefas.\n" \
        "3 - Remover uma tarefa.\n" \
        "4 - Sair."
          )

def sair():
    print("\nAté a próxima!\n")
    continuar = False; return continuar


# Loop principal
print (f"{'-'*25}\nBoas vindas à sua lista de tarefas!")
while continuar == True:
    exibir_menu()
    
    opcao = input("\nOpção: ")

    if opcao == "1":
        tarefa = input("\nInsira uma nova tarefa: ")
        lista_de_tarefas = adicionar_tarefa(tarefa)
    
    elif opcao == "2": listar_tarefas()

    elif opcao == "3":
            vazia = listar_tarefas()
            
            if vazia == False:
                numero_tarefa = input("\nEscolha o número da tarefa a ser removida: ")

                # Validação de input
                if numero_tarefa.isnumeric() != True: print ("\nEntrada inválida, tente novamente.")
                elif int(numero_tarefa) <= 0 or int(numero_tarefa) > len(lista_de_tarefas): print ("\nEntrada inválida, tente novamente.")
                else: lista_de_tarefas = remover_tarefas(int(numero_tarefa) - 1)
    
    elif opcao == "4":
        # Confirmação de saída
        confirma = input("\nTem certeza? (s/n): ")
        if confirma and confirma.lower() == "n":
            print ("")
        elif confirma and confirma.lower() == "s":
            continuar = sair()
        else: print("\nOpção inválida, tente novamente. (s/n): ")

    else: print("\nOpção inválida, tente novamente.")
