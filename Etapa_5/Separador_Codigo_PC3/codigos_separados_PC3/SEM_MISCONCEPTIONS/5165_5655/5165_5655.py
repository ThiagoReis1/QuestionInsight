peso = float(input("peso da racao: "))
quantidade = float(input("quantidade da racao em gramas: "))

resto = peso - (quantidade * 6)

print(round(resto, 4))