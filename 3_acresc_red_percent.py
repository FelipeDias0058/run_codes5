valor = float(input(""))
porcentagem = float(input(""))

acrescimo = valor * porcentagem / 100
v_acrescimo = valor + acrescimo

desconto = valor * porcentagem / 100
v_desconto = valor - desconto

print(f'{v_acrescimo:.2f}')
print(f'{v_desconto:.2f}')