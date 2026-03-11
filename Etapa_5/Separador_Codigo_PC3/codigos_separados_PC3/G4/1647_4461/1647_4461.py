from numpy import*

v = array(eval(input("alunos: ")))

cont = 0
x = zeros(size(v), dtype=int)
for i in range(size(v)):
	if(v[i] >= 70):
		cont += 1
		x[i]=i
print(cont)
print(x)




