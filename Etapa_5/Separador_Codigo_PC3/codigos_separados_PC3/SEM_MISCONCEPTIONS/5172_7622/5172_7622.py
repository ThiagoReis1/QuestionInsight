peso = float(input("peso do saco de racao: "))
qntd_diaria = float(input("quantidade diaria de racao: "))

consumo = qntd_diaria * 5
resto = peso - consumo

print(round(resto, 2))