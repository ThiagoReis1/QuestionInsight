peso = float(input("digite o peso da racao em gramas:"))
quant = float(input("digite a quantidade de racao em gramas:"))
comeu = quant * 5

result = peso - comeu

print(round(result,3))