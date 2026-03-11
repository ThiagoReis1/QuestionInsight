from numpy import*
m=array(eval(input("digite a matriz:")))
menor=-1
for i in range(m.shape[0]):
	mn=min(m[i,:])
	if (menor==-1):
		menor=mn
	else:
		if (menor > mn):
			menor=mn
print(menor)