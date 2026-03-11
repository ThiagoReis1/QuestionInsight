from numpy import*
qt = array(eval(input("Quantidades de alunos por turma: ")))
nt = 0
v = zeros(size(qt),dtype = int)

for i in range(size(qt)):
	v[i] = qt[i]% 5
	if v[i] == 0:
		nt = nt + 1
		
q = zeros(nt,dtype = int)
j = 0
for i in range (size(qt)):
	v[i] = qt[i]%5
	if v[i] == 0:
		q[j] = i
		j = j+ 1


			
print(nt)
print(q)
	

