q0 = int(input("Quantidade incial de grifos: "))
qx = int(input("Quantidade de novos grifos: "))
qy = int(input("Quantidade de grifos perdidos: "))
t = 0
q = q0

while(q>0):
	q = q + qx - qy
	t = t + 1
print(t)