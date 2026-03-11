num = int(input(":"))

cont = 0 

while num != -1:
	if (num > 26 and num < 50):
		num = num + cont
		cont += 1 
	num = int(input(":"))

print(cont)