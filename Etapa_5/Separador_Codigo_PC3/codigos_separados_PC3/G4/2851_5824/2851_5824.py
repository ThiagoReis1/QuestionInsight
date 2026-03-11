from numpy import * 

num=array(eval(input("O numro: ")))
soma=0
for i in range(size(num)):
	if num[i]!=99:
		soma=soma+num[i]
	else: 
		soma=soma*2
print(soma)