num = int(input("escreva o numero"))
numA = num // 100000
restoA = num % 100000
numB = restoA // 10000
restoB = restoA % 10000
numC = restoB // 1000
restoC = restoB % 1000
numD = restoC // 100
restoD = restoC % 100
numE = restoD // 10
restoE = restoD % 10
numF = restoE // 1

var = ((numA * 100 + numB * 10 + numC) + (numD * 100 + numE * 10 + numF))**2
if(var == num):
	print(num, "atende a propriedade")
else:
	print(var)