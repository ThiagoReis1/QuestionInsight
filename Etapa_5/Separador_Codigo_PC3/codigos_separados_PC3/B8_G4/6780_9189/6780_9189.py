nas = int ( input ("digite ano de nascimento: "))
pas =  input ( "B para brasil e C para china: ").upper()
ano = 2023
total = ano - nas

if total > 21 and pas == "B" and not pas == "C":	
	print ("sim")
	dif = total - 21
	print (dif)

elif total < 21 and pas == "B" and not pas == "C":
	print ("nao")
	dif = - (total - 21)
	print (dif)
	
elif total > 24 and pas == "C":
	print ("sim")
	dif =  total - 24
	print (dif)
	
elif total < 24 and pas == "C":
	print ("nao")
	dif = -(total - 24)
	print (dif)
	
if pas != "B" and pas != "C":
	print ("invalido")
	