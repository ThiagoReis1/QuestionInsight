num = int(input("diga um numero: "))

cont = 0

while num != -1:
	if num >= 76 and num <= 100:
		cont+=1
	num = int(input("diga um numero: "))

print(cont)