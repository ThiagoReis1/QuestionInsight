from numpy import*

n = array(eval(input("Nota do aluno:")))

cont = 0

for i in range(size(n)):
	 if(n[i]>=5):
			cont = cont +1

print(cont)

v2 = zeros(cont, dtype=int)

j = 0

for i in range(size(n)):
	 if(n[i]>=5):
			v2[j]= i
			j = j+1
print(v2)
	