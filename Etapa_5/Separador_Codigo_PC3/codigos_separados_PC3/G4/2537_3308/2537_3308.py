v = float(input("digite a heranca:"))
m = int(input("digite saque mensal:"))
j = float(input("digite juros:"))
saldo= v
t = 0
d = (20/100)*v + v
if(v>0)and(m>0)and(j>0):
	while(saldo<d):
		saldo= saldo + saldo*(j/100)
		saldo = round(saldo,2)
		saldo = saldo - m
		t = t + 1
	print(t)	
else:
	print("Dados incorretos")
