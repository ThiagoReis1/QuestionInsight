from numpy import*
v= array(eval(input("VETOR: ")))
i=1
cont=1
for i in v:
	res=(i+1)*(cont)
	cont+=1
print(res)
