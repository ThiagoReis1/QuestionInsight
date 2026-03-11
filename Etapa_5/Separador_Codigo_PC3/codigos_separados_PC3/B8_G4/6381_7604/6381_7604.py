from numpy import* 

jog = input("insira a sequencia:").upper().split(',')
cat = zeros(4,dtype = int)

for i in jog:
	if i == "C":
		cat[0] += 1
	elif i == "O":
		cat[1] += 1
	elif i == "P":
		cat[2] += 1
	elif i == "E":
		cat[3] += 1
		
print(cat)
	
