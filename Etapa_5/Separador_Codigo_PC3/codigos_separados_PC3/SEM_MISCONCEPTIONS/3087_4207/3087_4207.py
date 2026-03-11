x= int(input("Insira um numero inteiro: "))

soma=0
i=0 

while(x!=0):
	x= int(input("Insira um numero inteiro: "))
	if(x%2==0):
		i= i + 1
		soma = soma + x
		soma1= soma/(i)
	else:
		soma = soma + x
		i = i + 1
		soma2= soma/(i)

print(round(soma1, 2))
print(round(soma2, 2))