peso = float(input("Peso do saco de racao: "))
quantidade_diaria = float(input("Quantidade diaria: "))

resto = peso - (quantidade_diaria * 7)

print(round(resto,3))