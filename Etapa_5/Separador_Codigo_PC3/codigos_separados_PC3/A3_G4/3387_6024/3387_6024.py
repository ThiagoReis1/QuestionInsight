#Converter para duas casas decimais
x = input("unidade de medida: ").upper()
y = float(input("valor da medida: "))
M = "Milhas por galão"
K = "Quilômetros por Litro"
a = y/(2.35215)
b = y*2.35215
if x=="M":
	print(round(a,2))
else:
	print(round(b,2))