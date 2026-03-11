peso = float(input("Digite o peso do saco de racao: "))
quant = float(input("Digite a quantidade diaria de racao: "))

diaria = (quant * 6)
rest = peso - diaria

print(round( rest, 4 ))