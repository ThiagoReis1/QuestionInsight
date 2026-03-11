from numpy import*
v = array(eval(input("Numeros reais positivos: ")))
L = 0

for i in range(size(v)):
	
	L = L + log(v[i] + 1) 
	N = size(v)
	M = exp( sum(L) / N ) -1
	
print(round(M, 2))