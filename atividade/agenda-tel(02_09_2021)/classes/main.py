from .agenda import Agenda
from .contato import Contato
from .tarefa import Tarefa

class Main:
    def __init__(self):
        self.em_execucao = True
        self.agenda = agenda()
        self.agenda.set_proprietario('Edu')
        self.agenda.set_ano(2077)

    def mostrarmenu(self):
        print('')
        print("e" * 32)
        print("     A G E N D A")
        print("e" * 32)
        print("Digite um dos número como escolha: ")
        print('1. cadastrar contato')
        print('')