from numpy import*

num= int(input("Insira um numero para a contagem regressiva: "))

for i in range(num, -1, -1):
	if i >= 4:
		print(i)
		
print("Fim da contagem regressiva!")