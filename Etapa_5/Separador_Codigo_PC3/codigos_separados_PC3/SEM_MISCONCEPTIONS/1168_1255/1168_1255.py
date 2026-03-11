n = int(input("Digite n:"))
#contadora
count= 1
#acumulara
resultado = 0
sinal= 1
base = 1
num=1
while(count>=n):
	resultado = resultado - ((pow(num,3) / (8 + base))) 
	sinal =  sinal * -1 
	base = base + 2
	num = num + 1
	count = count + 1
print(round(resultado,5))
									 