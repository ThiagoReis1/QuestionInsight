from numpy import*
vet = input("Informe: ").upper().split(',')
res = zeros(5, dtype=int)
xp = 0
xc = 0
xm = 0
xv = 0
xa = 0
for i in range(size(vet)):
	if(xp=='P'):
		res[0] = res[0]+ 1
	elif(xc=='C'):
		res[1] = res[1] + 1
	elif(xm=='M'):
		res[2]= res[2] + 1
	elif(xv=='V'):
		res[3]= res[3] + 1
	elif(xa=='A'):
		res[4]= res[4] + 1
print(max(res))
print(res)