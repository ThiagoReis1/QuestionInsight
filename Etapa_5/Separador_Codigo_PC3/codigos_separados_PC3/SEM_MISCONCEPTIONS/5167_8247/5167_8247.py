peso = float(input("Insira o peso do saco da racao em gramas: "))
quan = float(input("Insira a quantidade diaria de racao em gramas: "))
resto = peso - quan*7
print(round(resto, 3))