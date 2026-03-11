Qi = int(input("Qi:"))
Qc = int(input("Qc:"))
Qd = int(input("Qd:"))

c = 0
Ac = Qi
lim = 200

while (Ac<lim):
	Ac += Qc - Qd
	c += 1
print(c)