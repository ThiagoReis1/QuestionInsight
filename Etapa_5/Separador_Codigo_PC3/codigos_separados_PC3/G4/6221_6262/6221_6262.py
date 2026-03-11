x = int(input("O valor de x: "))
y = int(input("O valor de y: "))

cont = 0 
while(x <= y):
	if(x % 7) == 0:
		cont += x
	x += 1
print(cont)
