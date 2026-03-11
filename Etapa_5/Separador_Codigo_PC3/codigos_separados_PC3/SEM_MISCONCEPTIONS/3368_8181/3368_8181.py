escala= input("escala de temperatura (C/K): ")
val= float(input("valor da temperatura: "))

form = +273.15

if(escala=="C"):
	form= (val+form)
	
else:
	form= (val-form)
print(round(form,2))
	