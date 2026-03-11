N = int(input())

i = 0 
soma = 0 
while(i<N):
	i = i + 1 
	soma = soma + ((-1)**(i+1))*((i)**2)/(1+(2*i+1))
	
print(round(soma,7))