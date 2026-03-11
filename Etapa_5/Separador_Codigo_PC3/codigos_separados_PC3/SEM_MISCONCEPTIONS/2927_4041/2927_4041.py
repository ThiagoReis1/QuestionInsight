valor = float(input("insira o valor de sua bebida: "))
quantidade = int(input("insira a quantidade de esfirras: "))

esfirra = float(quantidade*1.5)

total = valor + esfirra
print(round(total,2))