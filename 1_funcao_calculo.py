#Entrada de Dados
a = float(input(""))
b = float(input(""))
c = float(input(""))


#Função para o cálculo da expressão numérica
def calcular (a, b, c):
    return (2 * a) + (5 * b) - c


#Chamada da função "calcular"
r = calcular(a, b, c)

#Exibição do resultado da expressão
print(r)
