from numpy import*
m= array(eval(input()))
lin= shape(m)[0]
col= shape(m)[1]
indice= 0
maior= 0
for i in range(lin):
	for j in range(col):
		if(m[i][j]> maior):
			indice= 1
			maior= m[i][j]
		else:
			j=j+1
print(maior)