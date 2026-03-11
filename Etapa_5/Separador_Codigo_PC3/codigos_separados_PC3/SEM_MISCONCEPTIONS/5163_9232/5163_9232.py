peso = float(input("qual o peso em gramas? "))
diaria = float(input("qual a quantidade diaria em gramas? "))

resto = peso - (diaria * 5)
resto2 = round(resto, 3)

print(resto2)