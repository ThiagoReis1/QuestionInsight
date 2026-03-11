#ADRIANO CARELLI 
#AV 4

a = float(input("Digite o numero: "))

soma = 0 
j = 0

while(j < a):
	soma = soma + ((-1)** ( j +1)) * ((j+1)**3) / (9+(2*j+3))
	j = j + 1
print(round(soma, 8))
	