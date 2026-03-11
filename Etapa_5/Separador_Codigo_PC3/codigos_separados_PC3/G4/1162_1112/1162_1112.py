n=float(input("Premio:"))
c=float(input("Taxa de rendimento:"))
v=float(input("Valor em reais:"))
soma=n
t=1
fim=0
while(soma>fim):
	rend= soma * c
	saldo= soma+rend 
	soma= saldo-v
	t=t+1
print(t)
	 