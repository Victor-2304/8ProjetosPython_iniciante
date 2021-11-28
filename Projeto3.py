import PySimpleGUI as sg
import random

class chuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def iniciar(self):
        self.GerarNumAleatorio()
        self.PedirValorAleatorio() 

        while self.tentar_novamente == True:
            if int(self.valor_chute) > self.valor_aleatorio:
                print('Chute um valor mais baixo!')
                self.PedirValorAleatorio() 
            elif int(self.valor_chute) < self.valor_aleatorio:
                print('Chute um valor mais alto!')
                self.PedirValorAleatorio() 
            if int(self.valor_chute) == self.valor_aleatorio:
                self.tentar_novamente = False
                print('Parabéns você acertou!!')


    def PedirValorAleatorio(self):
        self.valor_chute = input('Chute um número: ')
    def GerarNumAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = chuteONumero()
chute.iniciar()