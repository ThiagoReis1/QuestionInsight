from numpy import*

somatoria=array(eval(input("")))
soma=0 

for i in range(size(somatoria)):	
	if somatoria[i] == 88:
		soma=(soma)/2
	else:
		soma=soma+somatoria[i]
		
print(soma)