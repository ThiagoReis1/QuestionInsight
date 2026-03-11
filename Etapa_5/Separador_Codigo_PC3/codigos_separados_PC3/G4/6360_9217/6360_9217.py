from numpy import *
num = eval(input("Digite um numero: "))

for i in range(-1, num, 4):
	print(num)
	num = num - 4
print("Fim da contagem regressiva!")