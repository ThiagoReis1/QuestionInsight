peso = float(input("Peso da racao?: "))
quantidade = float(input("Quantidade de racao?: "))

consumo = quantidade * 7 

total = peso - consumo 

print(round(total, 2))