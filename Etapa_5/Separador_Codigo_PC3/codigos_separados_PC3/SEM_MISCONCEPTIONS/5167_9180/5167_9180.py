peso = float(input('Peso do saco em gramas:'))
diaria = float(input('A quantidade diaria em gramas:'))

restante = peso - (diaria * 7) 

print(round(restante, 3))