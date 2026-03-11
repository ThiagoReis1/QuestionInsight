from numpy import*
tipo = array(eval(input("Sorotipo: ")))
vt = zeros(4, dtype=int)

for i in tipo:
	if(i == 1):
		vt[0] = vt[0] + 1
	elif(i == 2):
		vt[1] = vt[1] + 1
	elif(i == 3):
		vt[2] = vt[2] + 1
	elif(i == 4):
		vt[3] = vt[3] + 1
print(vt)