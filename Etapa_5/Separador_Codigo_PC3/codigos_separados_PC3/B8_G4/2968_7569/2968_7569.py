a = input("L/S: ")
b = float(input("q_lanche ou salgado: "))
c = float(input("q_refri: "))
if(a=="L"):
	t=5*b+(c*4)
	print(round(t,2))
elif(a=="S"):
	t=3.50*b+(c*4)
	print(round(t,2))
