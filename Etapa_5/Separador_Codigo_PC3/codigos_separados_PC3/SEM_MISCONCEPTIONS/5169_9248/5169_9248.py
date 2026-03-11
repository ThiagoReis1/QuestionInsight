peso = float(input("peso do saco de ração: "))
dose = float(input("quantidade de ração dada: "))

resto = peso - dose * 4
print(round(resto, 2))
