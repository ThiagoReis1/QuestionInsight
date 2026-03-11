peso = float(input("Digite a quantidade de racao que foi comprada: "))
qnt = float(input("Digite a quantidade de racao que sera usada diariamente: "))

resto = peso - qnt * 6

print(round(resto, 4))
