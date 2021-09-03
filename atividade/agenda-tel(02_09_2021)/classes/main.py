from .agenda import Agenda
from .contato import Contato
from .tarefa import Tarefa

class Main:
    def __init__(self):
        self.em_execucao = True
        self.agenda = agenda()
        self.agenda.set_proprietario('Edu')
        self.agenda.set_ano(2077)

    def mostrar_menu(self):
        print('')
        print("e" * 32)
        print("e" * 16 + " A G E N D A " + "e" * 13)
        print("e" * 32)
        print("Digite um dos número como escolha: ")
        print('1. Cadastrar Contato')
        print('2. Listar   Contatos')
        print('3. Excuir    Contato')
        print('4. Cadastrar  Tarefa')
        print('5. Listar    Tarefas')
        print('6. Excluir    Tarefa')
        print('7. Concluir  Tarefas')
        print('8. Definir Tarefas como "Pendentes"')
        print('0. Sair do Programa')

    def ler_opcao_menu(self):
        opcao = input(" x ")

        if(opcao = "0"):
            print("Até logo, desligando agenda. . .")
            self.em_execucao = False
            return
        elif(opcao = "1"):
            self.cadastrar_contato()
        elif(opcao = "2"):
            self.listar_contatos()
        elif(opcao = "3"):
            self.excluir_contatos()
        elif (opcao = "4"):
            self.cadastrar_tarefa()
        elif (opcao = "5"):
            self.listar_tarefas()
        elif (opcao = "6"):
            self.excluir_tarefa()
        elif (opcao = "7"):
            self.concluir_tarefas()
        elif (opcao = "8"):
            self.definir_tarefas_pendentes()
