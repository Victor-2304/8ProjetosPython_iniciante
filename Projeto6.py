import random 
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza deve fazer isso!',
            'Não sei, você que sabe',
            'Não faça isso!',
            'Acho que ta na hora certa!'
        ]

    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text('Faça sua pergunta: ')],
            [sg.Input()],
            [sg.Output(size=(20, 10))],
            [sg.Button('Decida por mim')]
        ]
        # criar a janela
        self.janela = sg.Window('Decida por mim', layout=layout)

        while True:
            # Ler os valores 
            self.eventos, self.valores = self.janela.Read()
            # Fazer algo com valores 
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))

            elif self.eventos == sg.WIN_CLOSED:
                break
            

decida = DecidaPorMim()
decida.Iniciar()