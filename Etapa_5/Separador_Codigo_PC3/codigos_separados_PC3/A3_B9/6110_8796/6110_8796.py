qtde_c = int(input())
total = 0

if qtde_c < 17.5:
	total = qtde_c + 10.5
elif qtde_c >= 17.5 and qtde_c < 35:
	total = qtde_c + 14
elif qtde_c >= 35 and qtde_c < 50:
	total = qtde_c + 18.6
else:
	total = qtde_c + 24.5
print(round(total, 1))