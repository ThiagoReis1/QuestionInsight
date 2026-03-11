from numpy import*

v = array(eval(input("Tempo de chegada:")),dtype=float)
cont = 0
Max = max(v)
result = 0
while(cont < size(v)):
	if(v[cont] == Max):
		result = cont
	cont += 1
	
print(result)