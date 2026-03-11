#Entradas
peso = float(input("Peso do saco em gramas: "))
quantidade = float(input("Quatidade diaria em gramas: "))
#Operacao
op = peso - (quantidade * 7)
#resultado
print(round(op, 3))