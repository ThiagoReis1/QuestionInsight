from numpy import*
vet = array(eval(input("numeros; ")))
num = int(input("numeros: "))
i = 0
qtd = 0
while(i<size(vet)):
	if(num==vet[i]):
		print(i)
	elif(num>vet[i]):
		qtd = qtd + 1
	i = i + 1
print(qtd)
		