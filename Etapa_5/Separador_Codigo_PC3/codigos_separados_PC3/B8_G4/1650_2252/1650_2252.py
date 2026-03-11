from numpy import*
cor = input("cor:").upper().split(',')
cont = zeros(5, dtype=int)
for x in cor:
	if(x == "P"):
		cont[0] = cont[0] + 1
	elif(x == "C"):
		cont[1] = cont[1] + 1
	elif(x == "R"):
		cont[2] = cont[2] + 1
	elif(x == "L"):
		cont[3] = cont[3] + 1
	elif(x == "B"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)