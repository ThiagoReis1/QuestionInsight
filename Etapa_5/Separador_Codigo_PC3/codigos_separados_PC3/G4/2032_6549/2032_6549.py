dado = int(input(""))
face = 0  # variavel acumuladora

while (dado != -1):
	if dado >= 1 and dado <= 10:
		if dado == 5:
			face = face + 1
		dado = int(input(""))	
print(face)