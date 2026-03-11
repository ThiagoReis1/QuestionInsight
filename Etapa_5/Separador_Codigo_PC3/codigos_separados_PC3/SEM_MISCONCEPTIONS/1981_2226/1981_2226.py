x=input("quem sao campeoes: ").upper()
y=int(input("quem sao vice campeoes: ")

if(x=="Campeao") or (y=="Vice-campeao")):
	if(x=="Campeao"):
		xa=((x*6)+(3*x))
		print("CORINTHIANS")
		print("SANTOS")
	elif(y=="Vice-campeao"):
		xb=((y*1)+(6*y))
		print("FLAMENGO")
		print("INTERNACIAL")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")
		
