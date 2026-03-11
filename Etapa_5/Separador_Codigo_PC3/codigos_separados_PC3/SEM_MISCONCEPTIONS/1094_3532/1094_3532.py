senha = int(input("digeti o valor"))

a = (senha//100000)
b = (senha//10000)%100

num=(a+b)**2
if(num==senha):
	recado= "atende"
else:
	recado= "nao atende"
	print(recado)
	
print(num)