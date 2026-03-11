num=int(input("Digite o numero: "))
j=0 #contador do laço
y=0
sinal=-1
while(j<=num):
	y = y-sinal*(j**3)/(9+2*j+1)
	sinal=-sinal
	j = j+1
print(round(y,8))