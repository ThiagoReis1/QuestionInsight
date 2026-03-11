num = int(input())
contPos= 0
contNeg = 0
cont = 0

while (num!=0):
	if (num>0):
		contPos = contPos+1
	else:
		contNeg = contNeg+1
	cont = cont+1
	num = int(input())
	
print(cont)
print((contPos/cont)*100)

	
