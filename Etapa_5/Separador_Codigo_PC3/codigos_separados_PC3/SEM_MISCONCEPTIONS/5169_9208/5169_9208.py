a = float(input("insira o peso do saco em gramas"))
b = float(input("insira a quantidade diaria em gramas"))
resultado = (a // b) % 4
print(round(resultado, 2)) 