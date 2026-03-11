n = int(input())
cont = 0
cont2 = 0
while n != -1:
	cont = cont + 1
	if n == 5:
		cont2=  cont2 + 1
		
	n = int(input())
		
x = (cont2/cont)*100
print(cont)
print(round(x,2))