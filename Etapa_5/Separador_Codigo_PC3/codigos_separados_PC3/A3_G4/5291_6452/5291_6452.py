w=input('sim ou nao').upper()
s=0
i=0
while w=="S" or w=="SIM" or w=="NAO":
	i=i+1
	if w=="SIM":
		s=s+1
	perc=(s/i)*100
	if w == "S":
		print(i-1)
		print(round(((s/(i-1))*100),2))
		break
	w=input(" ").upper()
		

		
		