num = int(input(""))

cont = 0
k = 0

while (num != 0):
	k = k +1
	
	if (num >= 1):
		cont = cont + 1
	num = int(input(""))

total = (cont*100)/k
print(k)
print(round(total,2))