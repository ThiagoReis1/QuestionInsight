qo = int(input(""))
d_mensal = int(input(""))
M = int(input(""))
R = int(input(""))
qf = (qo + M)-(d_mensal + R)
q = qo
mes = 1
while(qf > 0):
	q = q + 1
	mes = mes + 1	
	
print(mes)