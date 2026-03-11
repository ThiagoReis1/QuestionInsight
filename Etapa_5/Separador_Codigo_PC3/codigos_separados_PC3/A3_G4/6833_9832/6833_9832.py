c = input("Digite a secao dos produtos comprados: ").upper()

i = 0
t = 0
tf = True

while ( i < len(c) ) :
	if (not c[i] in "MPR") :
		tf = False
		break
	elif (c[i] == "M") :
		t += 7.25
	elif(c[i] == "P") :
		t += 4.75
	else :
		t += 3.5
	
	i += 1
	
if (tf == True) :
	print(round(t,2))
	
else :
	print("Bobo")