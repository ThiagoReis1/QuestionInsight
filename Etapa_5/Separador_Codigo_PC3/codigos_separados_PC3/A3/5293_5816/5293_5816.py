n = int(input(": "))
fim = 0
contp = 0
conti = 0
while(n != 0):
	if(n % 2 == 0):
		contp = contp + 1
	else:
		conti = conti + 1
	n = int(input(": "))
p = (contp / (contp + conti)) * 100
print(contp + conti)
print(round(p,2))