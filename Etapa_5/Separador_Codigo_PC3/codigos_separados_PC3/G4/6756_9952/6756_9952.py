d = float(input("dias:"))
if d < 15:
	soma = 175 * d + 20
elif d == 15:
	soma = 175 * d + 16
else:
	soma = 175 * d + 10
print(soma)