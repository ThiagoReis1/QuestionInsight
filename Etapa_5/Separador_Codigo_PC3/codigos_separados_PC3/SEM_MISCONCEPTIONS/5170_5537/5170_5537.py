peso = float(input("Digite o peso do saco de racao: "))
quantidade = float(input("Digite a quantidade de racao diaria: "))
total = peso - quantidade * 7
print(round(total,3))