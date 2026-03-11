r= input("Voce gostou do local? ").upper()
por= 0
x= 0


while (r!= "S"):
	if r== "SIM":
		x= x+1
	por= por+1
	r= input("Voce gosta do local? ").upper()
p= (100* x)/por
print(por)
print(round(p, 2))










