a = float(input("Digite o valor de um numero: "))
b = int(input("Quantidade de termos: "))

soma = 0 #acumuladora
i = 0  #contadora

while (i <= b - 1):
	soma = soma +(a)/(2*i + 1)
	i = i + 1
	
print(round(soma,8))