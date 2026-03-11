n= int(input("Digite um numero: "))


cont= 0
contt=0
while n!=0:
	if n%2==0:
		cont= cont+1
	n= int(input("digite um numero: "))	
	contt=contt+1	
print(contt)
print(round((cont*100)/contt, 2))





	