Qr = float(input())
Qm = float(input())
Qba = float(input())
Qo = float(input())

r = 7.0
m = 6
ba = 3
o = 5
ryo = 42

pf = (Qr *r)+(Qm*m)+(Qba*ba)+(Qo*o)

if (pf <= ryo):
	Pf = pf - 3.0
if(pf > ryo):
	Pf =pf - (pf*(10/100))
	
print(Pf)