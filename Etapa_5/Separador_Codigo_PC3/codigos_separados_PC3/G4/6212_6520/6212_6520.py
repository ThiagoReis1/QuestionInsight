n=int(input("intervalo saudavel: "))
cont=0
while n != -1:
	if n >= 26 and n <= 85:
		cont=cont+1
	n=int(input("intervalo saudavel: "))
print(cont)