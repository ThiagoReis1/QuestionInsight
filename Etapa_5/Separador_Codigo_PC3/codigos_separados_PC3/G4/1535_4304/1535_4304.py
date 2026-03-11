x= float(input("um numero real: "))
k= int(input("quantidade de termos: "))
t=0
soma=0
i=1
sinal= 1
while(t<k):
	soma= soma+(((x)**i)/i)*sinal
	sinal= sinal*(-1)
	i= i+2
	t= t+1
print(round(soma,6))
	