from numpy import*
v = array(eval(input("numero de alunos: ")))
a = 0
for i in range(0,(size(v)-1)):
	if(v[i]%3==0):
		a = a + 1
		print(i)
print(a)