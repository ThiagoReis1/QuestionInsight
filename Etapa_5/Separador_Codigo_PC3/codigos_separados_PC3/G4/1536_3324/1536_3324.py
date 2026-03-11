x= float(input())
k= int(input())

i=1
soma= 0

while(i<=k):
	soma= soma - (((-1)**i) * (x**i)/i)
	i= i+1	
print(round(soma,10))
	