float(input("A"))
float(input("S"))
float(input("T"))

qnt_A = A = 12.00
qnt_S = S = 5.00
qnt_T = T = 4.50

if(qnt_A <=1):
	valor1 =qnt_A*A

if(qnt_S <=1):
	valor2= qnt_S*S

if(qnt_T <=1):
	valor3 = qnt_T*T

Valortotal = valor1 or valor2 or valor3
print(round(Valortotal, 2))
