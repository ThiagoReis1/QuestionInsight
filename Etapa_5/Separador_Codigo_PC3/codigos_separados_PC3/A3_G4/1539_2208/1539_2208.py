x=float(input("Digite o valor de x: "))
n=int(input("Informe a quantidade de termos que você deseja: "))

to=1
t=1 # Variavel Contadora
p=1 # Variavel Acumuladora
while(p<n):
	to=to+(x**p)*(-1)**p
	p=p+1
	
print(round(to,7))