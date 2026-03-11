from numpy import*
vt = array(eval(input("Tempo: ")))
vp = array(eval(input("Percentual: ")))
consumo = 0
for i in range(len(vt)):
	ql = (vp[i]/100)*5
	consumo = consumo + ql*(vt[i])
	
	
print(consumo)
