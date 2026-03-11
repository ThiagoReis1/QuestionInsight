amino = input () .lower()

if (amino == "cisteina"):
	x = 12.011*3 + 7*1.00794 + 14.0067 + 2*15.9994 + 32.066
	print (round (x,2))
elif (amino == "isoleucina"):
	x = 12.011*6 + 13*1.00794 + 14.0067 + 2*15.9994 
	print (round (x,2))
elif (amino == "metionina"):
	x = 12.011*5 + 11*1.00794 + 14.0067 + 2*15.9994 + 32.066
	print (round (x,2))
else:
	print ("Entrada: ", amino)
	print ("Dado Invalido")
	