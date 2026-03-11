x = float(input("Digite o numero: "))
k = int(input("Digite a quantidade de termos: "))

cont = 0
soma = 0

while ( cont < k):
	soma = soma + (((-1) ** cont) * ( x ** cont))
	cont = cont + 1
print(round(soma, 7))
	
