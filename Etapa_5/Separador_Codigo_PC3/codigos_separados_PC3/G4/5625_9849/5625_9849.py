i = input().upper()
qtd= float(input())
qtd_acai= float(input())

T = 5.5
S = 4
A = 10
if (i == "T"):
	valor=qtd*T + qtd_acai*A
else:
	valor=qtd*S + qtd_acai*A
print(round(valor,2))
	