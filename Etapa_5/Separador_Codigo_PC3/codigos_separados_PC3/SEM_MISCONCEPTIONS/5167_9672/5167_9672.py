peso_saco= float(input("Insira o peso do saco de racao em gramas: "))
quantidade_racao= float(input("Insira a quantidade de racao diaria em gramas: "))

resto= peso_saco - (quantidade_racao * 7)

print(round(resto, 3))
