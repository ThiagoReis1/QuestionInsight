from numpy import*
v= array(eval(input("valores do vetor:")))
i=0
cont= "True"
while i < (len(v)-1) :
	if(v[i] + 1) < v[i]:
		cont="False"
	i=i+1
print(cont)

