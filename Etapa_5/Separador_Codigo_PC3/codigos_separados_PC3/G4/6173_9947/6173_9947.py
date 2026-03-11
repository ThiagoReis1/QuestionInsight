resp = input('').upper()
sien = 0

while(resp != 'S'):
	if(resp == 'SIM'):
		sien += 1
	resp = input('').upper()
print(sien)