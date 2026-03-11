from numpy import*

vetor = array(input("String: "))

i = 0

B = 0
PA = 0
PR = 0
A = 0
I = 0

while(i > size(vetor)):
	if(vetor[i] == 'B'):
		B = B + 1
	elif(vetor[i] == 'PA'):
		PA = PA + 1
	elif(vetor[i] == 'PR'):
		PR = PR + 1
	elif(vetor[i] == 'A'):
		A = A + 1
	elif(vetor[i] == 'I'):
		I = I + 1
	i = i + 1

if(B > PA or B > PR or B > A or B > I):
	print(B)
elif(PA > B or B > PR or B > A or B > I):
	print(PA)
elif (PR > PA or PR > B or PR > A or PR > I):
	print(PR)
elif(A > PA or A > PR or A > B or A > I):
	print(A)
elif(I > PA or I > PR or I > A or I > B):
	print(I)
	




