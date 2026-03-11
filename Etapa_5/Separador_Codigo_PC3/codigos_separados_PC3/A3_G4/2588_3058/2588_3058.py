from numpy import*
v= array(eval(input("Digite o vetor com as velocidades: ")))
soma= 0
j= 0
for i in range(size(v)):
	v1= (v[0] * 20/100) + v[0]
	v2= (v[0] * 50/100) + v[0]
	if(v[i] > v1) and (v[i] < v2):
		soma= soma + 1
		print(i)
print(soma)