x= float(input())
k=int(input())

soma=0
t=1
sinal= +1

while (t<=k):
	soma= soma + sinal * ((x**t)/t)
	sinal= - sinal
	t= t + 1
print(round(soma,10))
	