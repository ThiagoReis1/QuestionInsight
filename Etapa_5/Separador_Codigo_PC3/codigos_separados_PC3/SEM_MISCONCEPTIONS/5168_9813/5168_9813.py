peso = float(input("Coloque o valor do saco em gramas: "))
vr1 = float(input("Coloque a quantidade diaria em gramas: "))

resto = peso - (vr1 * 7)

print(round(resto, 4))
