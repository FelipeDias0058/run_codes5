#Função para converter os minutos em horas e minutos
def conversao(x):
    horas = x // 60
    minutos = x % 60
    return horas, minutos

#Entrada dos minutos a serem convertidos
x = int(input(""))

#Atribui horas/minutos calculados às respectivas variáveis
horas, minutos = conversao(x)

#Mostra na tela as horas e minutos
print(f'{horas}:{minutos}')
