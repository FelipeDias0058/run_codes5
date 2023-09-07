#Função para calcular a área e perímetro do quadrado
def f_area(q):
    area = q * q
    return area

def f_perimetro(q):
    perimetro = q * 4
    return perimetro

#Valor do lado do quadrado
q = float(input(""))

#Chamada da função
a = f_area(q)
p = f_perimetro(q)

#Exibição dos valores obtidos
print(f'{a:10.4f}')
print(f'{p:10.4f}')
