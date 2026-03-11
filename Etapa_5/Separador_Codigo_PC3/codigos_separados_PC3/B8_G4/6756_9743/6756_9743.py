n = int(input("numero de servico:"))

if n < 15:
	a = 175*n+20
elif n == 15:
	a = 175*n+16
elif n > 15:
	a = 175*n+10
print(round(a,2))