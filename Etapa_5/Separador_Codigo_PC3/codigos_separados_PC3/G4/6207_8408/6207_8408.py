cont = 0
num = int(input("digite um numero: "))

while (num > 0):
	if(num >= 26 and num <= 50):
		cont = cont+1
		
	num = int(input("digite um numero: "))
		
print(cont)