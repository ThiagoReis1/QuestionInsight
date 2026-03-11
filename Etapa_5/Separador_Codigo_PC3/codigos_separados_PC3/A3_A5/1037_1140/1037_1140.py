import math 

#ler valores:
quantia = float(input("Digite a quantia que vai converter: "))
cota = 0.26 

#Computar valores: 
valor_real = quantia - 9.0
valor_peso = valor_real / 0.26

rounded = round(valor_peso,2)
print(rounded)