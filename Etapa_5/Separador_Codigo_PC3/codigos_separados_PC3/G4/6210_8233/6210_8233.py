n = int(input("numero:"))
cont = 0
while(n != -1):
	if(n>=35) and (n<=95):
		cont= cont + 1
	n = int(input("numero:"))
print(cont)