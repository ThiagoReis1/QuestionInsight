peso = float(input("digite o peso do saco de racao em gramas: "))
quantidade = float(input("digite a quantidade de racao em gramas: "))

consumo = quantidade * 5
resto = peso - consumo 

print(round(resto, 3))
