face = input("cara ou coroa?").upper()
contadora = 0
while face!="S":
	if face == "CARA":
		contadora = contadora + 1
	face = input("cara ou coroa?").upper()
print(contadora)