from numpy import*
vt = array(eval(input("")))
vm = array(eval(input("")))

ct = vt*0.005 

if vt[0] == 90:
	msg = "QUENTE"
elif vt[1] == 45:
	msg = "MORNO"
else:
	msg = "FRIO"
	
print(round(ct, 2))

	