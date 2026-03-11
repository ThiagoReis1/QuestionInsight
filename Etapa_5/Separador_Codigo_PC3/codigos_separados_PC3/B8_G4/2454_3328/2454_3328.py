a=float(input("valor: "))
s=input("M ou F:")
if((a<1.0)or(a>=2.5)):
	print("altura invalida")
elif((s!="M")and(s!="F")):
	print("codigo invalido de sexo")
else:
	if((a>1.0)and(a<=2.5)and(s=="M")):
		print(round((72.7*a)-58,2))
	else:
		if((a>1.0)and(a<=2.5)and(s=="F")):
			print(round((62.1*a)-44.7,2))
				
		
