from numpy import*
turmas=array(eval(input()))
v5 = 0
i=0
j = 0
v = ""
for i in range(size(turmas)):
	if(turmas[i]%5 == 0):
		v5 = v5 +1
for i in range(size(turmas)):
	if(turmas[i]%5 == 0):
		v[i] = i
i = i +1
		
print(v5)
print(v)	