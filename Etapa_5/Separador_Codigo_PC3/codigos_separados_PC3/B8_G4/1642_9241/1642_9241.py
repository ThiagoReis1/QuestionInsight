from numpy import*
v= array(eval(input("quantas turmas com grupos de cinco alunos rapaz: ")))

cincum= 0

#contar cincums
for i in range(size(v)):
	if(v[i]%5 ==0):
		cincum+= 1

#vetor com quantidades de cincums
aux= zeros(cincum, dtype= int)

x=0

for i in range(size(v)):
	if i == 0 and v[0] % 5 ==0:
		aux[0]= 0
		x+=1
	elif(v[i] % 5 ==0):
		aux[x]= i
		x += 1
print(cincum)
print(aux)