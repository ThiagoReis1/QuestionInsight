num = int(input("numero: "))
i = 0
p = 0
while(num != 0):
	if(num > 0):
		p = p + 1
	i = i + 1
	num = int(input("numero: "))
print(i)
print(round((p/i)*100, 2))