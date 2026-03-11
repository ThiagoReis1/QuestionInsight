tipo = input().upper()
n_tipo = int(input())
n_acai = int(input())

if tipo == "S":
	total = n_tipo*4 + n_acai*10
else:
	total = n_tipo*5.5 + n_acai*10
print(round(total, 2))