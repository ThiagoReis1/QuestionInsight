#Entrada de variaveis
carg=int(input("qual o codigo do cargo?"))
sal=float(input("qual o salario do ninja?"))
#carg=código do cargo
#sal=salario do ninja atual
if carg==101:
	print(round(sal*(10/100)+sal,2))
	print("Aumento de 10 por cento")
else:
	print(round(sal*(30/100)+sal,2))
	print("Aumento de 30 por cento")