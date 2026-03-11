v = array(eval(input("V:")))
i = 0
soma = 0
while (i<size(v)):
	if(v[i]==1):
		soma=soma + 80
		i=i+1
	elif(v[i]==2):
		soma=soma + 40
		i=i+1
	elif(v[i]==3):
		soma=soma + 20
		i=i+1
	elif(v[i]==4):
		soma=soma + 10
		i=i+1
print(soma)

