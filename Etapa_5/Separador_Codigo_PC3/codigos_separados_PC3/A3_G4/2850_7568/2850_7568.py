from numpy import*
x=array(eval(input("")))
soma=0
a=0
for i in range(size(x)):
	soma = soma +x[i]
	if(soma>=55):
		soma = 0
print(soma)
		
		
