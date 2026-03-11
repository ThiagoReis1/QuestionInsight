
B=5.00
S=4.00
C=7.50

pedido=input("S ou B: ").upper()
q=int(input("quantidadede?: "))
qc=int(input("quantidade de cappuccinos?: "))

if pedido == "S":
	total = S*q + C*qc
else:
	total = B*q + C*qc

print(round(total,2))