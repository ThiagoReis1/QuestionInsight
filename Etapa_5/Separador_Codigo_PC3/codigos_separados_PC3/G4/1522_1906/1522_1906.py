qi = int(input(""))
dm = int(input(""))
qm = int(input(""))
qr = int(input(""))
m = qi - dm + qm - qr
meses = 0
i = 0
while(m<qi):
	meses = meses + qi/(qi-m)
	i = i + 1
print(meses)
	
	


