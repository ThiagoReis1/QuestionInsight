from numpy import*
v=array(eval(input("Digite v: ")))
i=0
for cont in range(1,size(v)):
	if(v[cont]>=v[0]):
		print(cont)
		i = i + 1
print(i)