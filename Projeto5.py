import random 
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso!',
            'Acho que ta na hora certa!'
        ]

    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()