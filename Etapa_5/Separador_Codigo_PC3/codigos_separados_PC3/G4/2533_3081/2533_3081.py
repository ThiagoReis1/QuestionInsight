V = float(input("Indenizacao: "))
C = float(input("Saque mensal: "))
J = float(input("Taxa de juros: "))
J = J/100
t = 0
i = V/2
if(V<= 0 or C<= 0 or J <= 0):
	print("Dados incorretos")
else:
	while(i<V):
		saldo = V * J
		V = saldo + V -C
		V = round(V,2)
		t = t + 1
	print(t)
		
		