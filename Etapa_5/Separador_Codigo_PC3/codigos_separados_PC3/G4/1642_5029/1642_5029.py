from numpy import *

# = array(eval(input("")))

#v = []
#a = 0

#for alunos in range(size(n)) :
	#if (n[alunos] % 5 == 0) :
		# = a + 1
#print(a)	
#for alunos in range(size(n)) :
	#if (n[alunos] % 5 == 0) :
		#v.append(alunos)
#print(v)	

n = array(eval(input("")))

a = 0
c1 = 0

for alunos in n :
	if (alunos % 5 == 0) :
		a = a + 1
vf = zeros(a, dtype = int)		
for i in range(size(n)) :
	if (n[i] % 5 == 0) :
		vf[c1] = i
		c1 = c1 + 1
print(a)
print(vf)
