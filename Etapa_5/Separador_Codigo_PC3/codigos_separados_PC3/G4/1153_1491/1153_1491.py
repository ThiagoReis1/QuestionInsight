pap = float(input("digite o patrimonio atual: "))
pab = float(input("digite o patrimonio atual: "))
pcp = float(input("percentual liquido anual: "))
pcb = float(input("percentual liquido anual: "))

m = 1

a = (pap * (pcp/100)) + pap
b = (pab * (pcb/100)) + pab

while(b < a):
	a = (a * (pcp/100)) + a
	b = (b * (pcb/100)) + b
	m = m + 1
print(m)