#Funções para cálculo de porcentagem, acréscimo e desconto
def percent(valor, valor_percent):
    porcentagem = valor * valor_percent / 100
    return porcentagem

def acr(valor, valor_percent):
    acrescimo = valor + porcentagem
    return acrescimo

def desc(valor, valor_percent):
    desconto = valor - porcentagem
    return desconto

#Entrada de dados
valor = float(input(""))
valor_percent = float(input(""))

#Chamada das Funções
porcentagem = percent(valor, valor_percent)
acrescimo = acr(valor, valor_percent)
desconto = desc(valor, valor_percent)

#Exibição do acréscimo e desconto
print(f'{acrescimo:.2f}')
print(f'{desconto:.2f}')
