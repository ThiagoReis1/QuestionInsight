#Entrada de dados
a= float(input("Qual o consumo de energia durante o mes, em kwh?"))

#Calculo interno
b= (0.43*a) + 10
c= b*1.25

#saida de dados
print(round(c, 2))