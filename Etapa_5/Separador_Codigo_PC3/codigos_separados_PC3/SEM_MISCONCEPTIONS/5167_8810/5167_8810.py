
peso = float(input("Digite o peso do saco de racao em gramas:"))
quantidade = float(input("Digite a quantidade de racao em gramas:"))

resto = peso - (quantidade*7)

print(round(resto,3))