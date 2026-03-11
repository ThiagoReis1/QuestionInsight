#Entrada
consumo = float(input("Consumo do mes: "))
#Operações
valor = ((consumo * 0.37) + 15) * 0.35
total = valor + ((consumo * 0.37) + 15)
#Resultado
print(round(total, 2))
