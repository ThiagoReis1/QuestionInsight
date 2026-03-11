from numpy import*
lista = array(eval(input("Digite os numeros: ")))
n = zeros(37,dtype = int)
q = 0
for i in lista:
	n[i] = n[i] + 1
print(n)
	
	