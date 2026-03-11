x = int(input("insira a idade: "))
c = 0
while(x !=-1):
	if(x<18):
		c = c+1
		x = int(input("insira a idade: "))
	else:
		x = int(input("insira a idade: "))
print(c)