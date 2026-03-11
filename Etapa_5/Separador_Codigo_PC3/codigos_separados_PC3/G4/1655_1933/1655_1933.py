from numpy import*
v = str(input("pessoas:"))
vet = array(ones(6))
i = 0
AC = 0
AM = 0
PA = 0
RO = 0
RR = 0
while( i < size(v)):
	if(v[i] == 0):
		AC = AC + 1
	if(v[i] == 1):
		AM = AM + 1
	if(v[i] == 2):
		PA = PA + 1
	if(v[i] == 3):
		RO = RO + 1
	if(v[i] == 4):
		RR = RR + 1
vet[0] = AC
vet[1] = AM
vet[2] = PA
vet[3] = RO
vet[4] = RR
print(max(vet))
print(vet)

	