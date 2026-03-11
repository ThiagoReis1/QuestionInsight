m = int(input("Massa em g: "))
aux = 0
cont = 0 

while m > 0.5:
	aux = m * 0.1
	m = m - aux
	cont = cont + 1
print(round(cont,2))
	
