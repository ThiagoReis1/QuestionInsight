km = float(input("Digite a distancia percorida em Km:"))
total = float(input("Digite o chakra do ninja:"))
x = km * 1000
m = x * 30 / 10

if(total >= m):
	print(round(m,2))
	print("vai conseguir")
else:
	print(round(m,2))
	print("nao vai conseguir")
	
	