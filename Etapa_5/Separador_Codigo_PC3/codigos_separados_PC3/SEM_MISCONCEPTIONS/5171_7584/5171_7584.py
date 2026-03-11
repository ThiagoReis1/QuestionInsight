#entrada
peso = float(input("Qual o peso do saco de racao em gramas? "))
qnt = float(input("Qual a quantidade diaria de racao em gramas? "))

#calculo total de racao que sobrou da semana e o resto
total = qnt*7 
resto = peso - total

#saida
print(round(resto, 2))