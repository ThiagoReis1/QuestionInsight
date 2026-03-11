from numpy import*
num = input("insira: ").upper().split()
cont = zeros(4,dtype=int)

for i in num:
	if (num == 'O'):
		cont[1]= cont[1]+1		
	elif (num== 'D'):
		cont[2] = cont[2]+1		
	elif (num == 'N'):
		cont[3] = cont[3]+1		
	elif (num == 'C'):
		cont[4] = cont[4]+1
print(cont)		

		