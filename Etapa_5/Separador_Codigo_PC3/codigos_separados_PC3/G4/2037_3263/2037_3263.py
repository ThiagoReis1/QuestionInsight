idad = int(input("idade: "))

pes = 0

while(idad != -1):
	idad = int(input("idade: "))
	if(idad <= 18 and idad > 0):
		pes = pes + 1
	else:
		pes = pes + 0
		
print(pes)