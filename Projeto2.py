import PySimpleGUI as sg
import random 

class SimuladorDeDado:
    def __init__(self):   #informações que serão utilizadas nas outras funções 
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Voce gostaria de gerar um novo numero? '

        # Layout    Definido como uma lista
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]

    def Iniciar(self):
        
        # cirar uma janela 
        self.janela = sg.Window('Simulador de Dado', layout=self.layout) #Passando o layout e o titulo da janela

        # ler valores da tela
        self.eventos, self.valores = self.janela.Read()

        # fazer alguma coisa com os valores 
        try:
            if self.eventos  == 'sim':
                self.GerarValorDado()
            elif self.eventos  == 'não':
                print('Ok')
            else: 
                print('Favor digitar sim ou não ')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDado(self): #função unica para gerar o valor 
        print(random.randint(self.valor_minimo, self.valor_maximo))

#precisa instanciar a classe 
simulador = SimuladorDeDado()
simulador.Iniciar()