x=float(input())
k=int(input())
soma=0
i=0
while(i<k):
	soma=soma+((-1)**i)*((x)**(2*i+1))/(2*i+1)
	i=i+1
print(round(soma,6))