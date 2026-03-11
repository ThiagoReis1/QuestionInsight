from numpy import*
vet = array(eval(input()))

for i in range(size(vet)):
	if(vet(i) >= 1) and (vet(i) <= 9):
		vet(i) = ((vet(i) - 1) ** (3))
	elif(vet(i) == 0):
		vet(i) == ((9) ** (3))

print(vet)