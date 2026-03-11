time = input("quem ganhou (A/B/E)")
cont = 0

while time.upper() != "X":

	
	if time.upper() == "A":
		cont +=1
		time = input("quem ganhou (A/B/E)")
	
	if time.upper() == "E":
		time = input("quem ganhou (A/B/E)")
		
	if time.upper() == "B":
	#print("vai tnc B")
	 	time = input("quem ganhou (A/B/E)")

	if time.upper() == "X":
		print(cont)
		break
