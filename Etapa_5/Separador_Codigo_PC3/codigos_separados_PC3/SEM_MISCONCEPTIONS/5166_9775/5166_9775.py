peso = float(input('Peso do saco em gramas: '))
quan_dia = float(input('Quantidade diaria de racoes: '))

restante = peso - quan_dia * 5

print(round(restante, 2))