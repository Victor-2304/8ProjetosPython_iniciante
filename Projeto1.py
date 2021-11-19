import random 

class SimuladorDeDado:
    def __init__(self):   #informações que serão utilizadas nas outras funções 
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Voce gostaria de gerar um novo numero? '
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'Sim'or resposta == 's':
                self.GerarValorDado()
            elif resposta == 'Não'or resposta == 'n':
                print('Ok')
            else: 
                print('Favor digitar sim ou não ')
        except:
            print('Ocorreu um erro ao receber sua resposta  ')

    def GerarValorDado(self): #função unica para gerar o valor 
        print(random.randint(self.valor_minimo, self.valor_maximo))

#precisa instanciar a classe 
simulador = SimuladorDeDado()
simulador.Iniciar()