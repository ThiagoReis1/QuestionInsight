v = float(input("Insira o valor do premio:"))
m = float(input("Insira o valor m do saque:"))
i = float(input("Insira a taxa de juros:"))
t = 0
s = v
if v>0 and m>0 and i>0:
	while s<(1.1*v):
		s = round((s*(i/100) + s) - m,2)
		t = t + 1
	print(t)
else:
	print("Dados incorretos")