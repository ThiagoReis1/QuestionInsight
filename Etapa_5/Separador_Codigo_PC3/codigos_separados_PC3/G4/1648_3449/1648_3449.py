from numpy import*
v=array(eval(input("Alunos reprovados: ")))
s=0
for i in v:
	if (i<70):
		s=s +1
print(s)

t= zeros(s, dtype=int)
c= 0
b= 0

for l in v:
	if	(l < 70):
		t[c]= t[c] + b
		b= b+1
		c= c+1
	else:
		b=b+1
		
print(t)
	


				 