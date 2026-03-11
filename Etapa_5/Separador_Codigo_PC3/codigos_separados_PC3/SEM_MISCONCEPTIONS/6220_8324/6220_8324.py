skunk=int(input("valor de x:"))
seda=int(input("valor y:"))
soma=0
while (skunk<seda+1):
	if (skunk%3==0):
		soma=soma+skunk
	skunk=skunk+1
print(soma)