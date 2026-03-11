from numpy import *
v1= array(eval(input("digite as notas do aluno: ")))
i=1
m=0
nf=m/10
while(i<size(v1)):
	if(i==1):
		m=v1[i]*5.0
		elif(i==2):
			m=v1[i]*3.0
			elif(i==3):
				m=v1[i]*2.0
	m=m+m
	i=i+1
print(round(nf,2))
if(nf>=5.0):
	print("APROVADO")
else:
	print("REPROVADO")
	
