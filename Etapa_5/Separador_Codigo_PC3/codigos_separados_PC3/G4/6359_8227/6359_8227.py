import time

N = int(input("digite um numero: "))


for i in range(N, -1, -3):
	print(i)
	time.sleep(3)
	
print("Fim da contagem regressiva!")