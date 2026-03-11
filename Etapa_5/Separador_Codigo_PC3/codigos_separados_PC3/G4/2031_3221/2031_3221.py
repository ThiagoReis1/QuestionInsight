d = int(input())

cont = 0

while ((d!=-1) and (d<=6) and (d >= 1)):
	if (d==6):
		cont = cont + 1
		d = int(input())
	else:
		d = int(input())
print(cont)