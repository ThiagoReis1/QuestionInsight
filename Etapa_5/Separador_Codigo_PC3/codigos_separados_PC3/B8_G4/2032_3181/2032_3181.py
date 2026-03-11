res = int(input(" "))
cont = 0
while(res != -1):
	if(res == -1):
		break
	elif(res == 5):
		cont = cont + 1
	res = int(input(" "))
print(cont)