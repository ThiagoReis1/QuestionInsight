from numpy import*

anel = array(eval(input("digite o valor: ")))

i = 0
pont = 10000

while(i <size(anel)):
	if(anel[i] == 1):
		pont = pont * 2
	elif(anel[i] == 2):
		pont = pont 
	elif(anel[i] == 3):
		pont = pont/2
	elif(anel[i]==4):
		pont = pont/4
	i = i + 1
print(round(pont, 2))