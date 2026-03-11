n= int(input())
i= 0
soma=0
while n !=0:
	i= i +1
	if n % 2==0:
		soma = soma + 1
	n= int(input())	
	tt= (soma /i)* 100


print(i)
print(round(tt,2))