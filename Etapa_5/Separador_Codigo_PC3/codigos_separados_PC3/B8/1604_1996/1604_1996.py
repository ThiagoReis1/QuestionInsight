from numpy import *

aneisac = array(eval(input("Digite o vetor que corresponde aos aneis acertados pelo jogador: ")))

i = 0

while(i <= aneisac[-1]):
	
	i = i + 1

if (aneisac[0] == 1):
	aneisac[0] = 80
elif (aneisac[0] == 2):
	aneisac[0] = 40
elif (aneisac[0] == 3):
	aneisac[0] = 20
elif (aneisac[0] == 4):
	aneisac[0] = 10
	
if (aneisac[1] == 1):
	aneisac[1] = 80
elif (aneisac[1] == 2):
	aneisac[1] = 40
elif (aneisac[1] == 3):
	aneisac[1] = 20
elif (aneisac[1] == 4):
	aneisac[1] = 10
	
	
if (aneisac[2] == 1):
	aneisac[2] = 80
elif (aneisac[2] == 2):
	aneisac[2] = 40
elif (aneisac[2] == 3):
	aneisac[2] = 20
elif (aneisac[2] == 4):
	aneisac[2] = 10	
	
	
if (aneisac[3] == 1):
	aneisac[3] = 80
elif (aneisac[3] == 2):
	aneisac[3] = 40
elif (aneisac[3] == 3):
	aneisac[3] = 20
elif (aneisac[3] == 4):
	aneisac[3] = 10		
	
total = (aneisac[0] + aneisac[1] + aneisac[2] + aneisac[3])

print(int(total))


