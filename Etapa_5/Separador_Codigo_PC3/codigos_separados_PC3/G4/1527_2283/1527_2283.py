qf = int(input("A quantidade INICIAL de seg. de FORSETI: "))
ql = int(input("A quantidade INICIAL de seg. de LOKI: "))
pf = float(input("Percentual ANUAL e crec. dos segu. de FORSETI: "))
pl = float(input("Percentual ANUAL e crec. dos segu. de LOKI: "))

t = 0

while(ql < 2 * qf ):
		ql = (pf + (pf*pl))/100
		ql = t
		t = t + 1
	
print(t)