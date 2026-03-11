pap = float(input("patrinomio:"))
pab = float(input("patrimonio:"))
pcp = float(input("taxa probesco"))
pcb = float(input("taxa bitcoin"))

k = pap
l = pab
m = 0

while (l < k):
	k =  k + (k*pcp/100)
	l = l + (l*pcb/100)
	m = 1 + m
print(m)