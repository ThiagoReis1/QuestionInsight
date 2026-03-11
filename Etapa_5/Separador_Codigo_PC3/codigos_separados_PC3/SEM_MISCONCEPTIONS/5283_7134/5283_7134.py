num = int(input("numero: "))
numn = 0
nump = 0

while num != 0:
	if num > 0:
		nump = nump + 1
	else:
		numn = numn +1
	num = int(input("numero: "))
	
total1 = nump + numn
total = ((100/total1)*nump)
	
print(total1)
print(round(total, 2))
	