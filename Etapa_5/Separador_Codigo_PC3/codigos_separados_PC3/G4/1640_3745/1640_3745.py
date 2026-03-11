from numpy import*
a = array(eval(input("Digite a quantidade de alunos: ")))
c = 0
for i in range(size(a)):
	if(a[i] % 2 != 0):
		c = c + 1
v = zeros(c,dtype=int)
j = 0
for i in range(size(a)):
	if(a[i] % 2 != 0):
		v[j] = i
		j = j + 1
print(c)
print(v)