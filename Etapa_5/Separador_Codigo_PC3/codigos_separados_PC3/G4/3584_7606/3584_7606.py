from numpy import*

c = array(eval(input("digite o vetor")))
b = 0
i = 0
while i < size(c):
	#i = 1
	
	#estou aqui
	if c[i] > 200:
		b = b + c[i] * 0.15
		t = sum(c) - b
	i = i + 1
	
	#pulo para ca
print(round(t, 2))
						

	
	
