kubo = int(input("numero:"))
cont = 0
while(kubo != -1):
	if (kubo>=26)and (kubo<=85):
		cont= cont + 1
	kubo = int(input("numero:"))
print(cont)