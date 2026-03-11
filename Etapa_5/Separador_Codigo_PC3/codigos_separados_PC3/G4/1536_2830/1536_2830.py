x = float(input())
k = int(input())

i = 1
soma=1

while(i+1 <= k ):
	soma = soma + ((-1)**(i)) *  (((x)**(i+1)) / (i+1))
	i = i+1
print(round(soma,10))