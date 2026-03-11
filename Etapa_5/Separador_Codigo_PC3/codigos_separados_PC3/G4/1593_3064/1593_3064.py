from numpy import*

vetn= array(eval(input("Informe as notas do aluno: ")))
v=0
i=0
s=0
d=1
while (i<size(vetn)):
	s= s+(vetn[i]*(d))
	v= d+v
	i=i+1
	d=d+1

	
k=s/v
print(round(k,2))