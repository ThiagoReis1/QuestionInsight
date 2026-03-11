altura_max = 1.75
taxa_max = 0.01

a = float(input())
b = float(input())

cont = 0 
while (a >= altura_max):
	cont = cont + 1 
	a = a + b 
	altura_max = altura_max + taxa_max
	
print(cont)