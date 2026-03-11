x = float(input("Digite um numero:"))
k = int(input("Digite a quantidade de termos da serie:"))

soma = 0
cont = 1

while cont <= k:
	soma = soma + x/(2*cont)
	cont = cont + 1
	
print(round(soma,8))