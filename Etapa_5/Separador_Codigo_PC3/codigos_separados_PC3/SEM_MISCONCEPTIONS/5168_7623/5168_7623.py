peso = float(input(" Insira o peso do saco de racao em gramas: "))
quantidade = float(input(" Qual a quantidade diaria de racao em gramas: "))

racao_final = (peso) - (quantidade * 7) 

print(round(racao_final, 4))