peso = float(input("Qual o peso do saco de racao em gramas?: "))
quantidade = float(input("Qual a quantidade diaria de racao em gramas?: "))

resto = peso - (quantidade * 5)

print(round(resto, 2))