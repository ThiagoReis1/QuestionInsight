v = float(input("Valor "))
c = float(input("Saque "))
tx = float(input("Juros "))

j = tx/100

saldo = (v - c)*j

while(saldo >= v/2):
	if (v < 0) or (c < 0) or (tx < 0):
		print("Dados incorretos")
	else:
		t = 0 
		t = t + 1
print(t)