quant=int(input())
acom=input()
acom=acom.lower()
if (acom.lower()=="rede" or acom.lower()=="camarote" or  acom.lower()=="suite"):
	if (acom.lower()=="rede"):
		valor= 500.00 * quant
		print(round(valor,2))
	elif (acom.lower()=="camarote"):
		soma= 1200.00 * quant
		print(round(soma,2))
	elif (acom.lower()=="suite"):
		soma1= 1500.00 * quant
		print(round(soma1,2))
else:
	print("acomodacao invalida")