from numpy import*

a = array(eval(input("Insira os Valores de Entrada: ")))

n = 0

for i in range(size(a)):
	if(a[i] == 0):
		n = 0
	else:
		n = n + a[i]
		
print(n)