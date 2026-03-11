va = float(input("investimento A:"))
vb = float(input("investimento B:"))
ja = float(input("juros A:"))/100
jb = float(input("juros B:"))/100
t = 0

if((va>0)and(vb>0)and(ja>0)and(jb>0)and(va>vb)and(ja<jb)):
	while(vb<va):
		va = va + va*ja
		vb = vb + vb * jb
		va = round(va,2)
		vb = round(vb,2)
		t = t+1
	print(t)
else:
	print("Dados incorretos")
