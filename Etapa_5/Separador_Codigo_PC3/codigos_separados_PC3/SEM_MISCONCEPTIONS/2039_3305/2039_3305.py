sq = input("entre com a letra:").upper()
acumuladora = 0
while((sq != "S")):
	if(sq == "A"):
		acumuladora = acumuladora + 1
	sq =  input("entre com a letra:")
else:
		print(acumuladora)