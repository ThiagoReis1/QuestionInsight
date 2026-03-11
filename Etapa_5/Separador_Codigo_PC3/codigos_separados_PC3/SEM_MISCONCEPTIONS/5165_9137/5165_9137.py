peso = float(input("digite o peso: "))
quantidade_diaria = float(input("Digite a quantidade: "))


total = (quantidade_diaria * 6)
quantidade = peso - total

print(round(quantidade, 4))