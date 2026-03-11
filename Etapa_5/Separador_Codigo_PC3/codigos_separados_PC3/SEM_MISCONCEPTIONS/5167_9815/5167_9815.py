peso = float(input("Insira o Peso do Saco de Racao em Gramas: "))
diaria = float(input("Insira a Quantidade Diaria de Racao em Gramas: "))

resto = round(peso - (diaria * 7), 3)

print(resto)