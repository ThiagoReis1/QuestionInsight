from numpy import*

aula = array(eval(input("Digite a porcentagem de aulas frequentadas: ")))

aprov = 0 
for i in range(size(aula)):
	if aula[i] >= 70:
		aprov += 1
print(aprov)

l = zeros(aprov,dtype=int)
aux = 0
for i in range(size(aula)):
	if aula[i] >= 70:
		l[aux] = i
		aux += 1

print(l)