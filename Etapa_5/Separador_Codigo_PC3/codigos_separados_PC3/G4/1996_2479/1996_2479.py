amno = input("Aminoácido: ").lower()

if(amno == "aspartato"):
	cal = round((12.011*4)+(1.0079*6)+(14.0067)+(15.9994*4),2)
	print(cal)

elif(amno == "fenilalanina"):
	cal = round((12.011*9)+(1.0079*11)+(32.066)+(15.9994*2),2)
	print(cal)
	
elif(amno == "tirosina"):
	cal = round((12.011*9)+(1.0079*11)+(14.0067)+(15.9994*3),2)
	print(cal)
	
else:
	print("Entrada:",amno)
	print("Dado Invalido")
	