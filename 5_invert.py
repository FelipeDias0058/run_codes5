#Função que inverte os dígitos do número inserido
def f_invert(x):

    #É usada uma função recursiva para chamar a si
    #mesma e inverter os dígitos
    if len(x)==0:
        return x

    return f_invert(x[1:]) + x[0]


def main():
    #Entrada de Dados
    x = int(input(""))
    #Formata dados como string
    x_string = str(x)

    #Chamada da função
    invert = f_invert(x_string)

    #Condicional para que o número inserido
    #obedeça aos parâmetros requisitados
    if 1000 <= x <= 9999:
           print(invert)
    else : print("Insira um número entre 1000 e 9999.")

if __name__ == "__main__":
    main()
