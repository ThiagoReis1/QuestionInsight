from math import *
#Captura de dados
b = radians(float(input("Informe o valor de b: ")))
c = radians(float(input("Informe o valor de c: ")))
alpha = float(input("Informe o valor do angulo alfa entre b e c: "))

#Processamento
alpha = radians(alpha)

a = sqrt((b**2) + (c**2) - (2 * b * c * (cos (alpha))))
	  
#Saída
print(a)