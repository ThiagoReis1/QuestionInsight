peso_racao= float(input("Digite o peso do saco de racao:"))
quantidade_diaria= float(input("Digite a quantidade diaria de racao:"))

dia= quantidade_diaria*7

resto= peso_racao-dia

print(round(resto, 3))