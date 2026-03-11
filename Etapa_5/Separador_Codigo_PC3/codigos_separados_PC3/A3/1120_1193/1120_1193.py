casa = input("casa: ")
resultado = ""
if (casa == "Baratheon"):
   resultado = "Ponta Tempestade"
elif(casa == "Tagaryen"):
	resultado = "Ilha do Dragao"
elif(casa =="Tyrell"):
	resultado = "Campina"
elif(casa =="Stark"):
	resultado ="Winterfell"
elif(casa =="Lannister"):
	resultado ="Rochedo Casterly"
elif(casa =="Greyjoy"):
	resultado ="Pyke"
elif(casa =="Tully"):
	resultado ="Correrio"
elif(casa =="Arryn"):
	resultado ="Ninho da Aguia"
elif(casa =="Martell"):
	resultado ="Dorne"
else:
	print("Entrada",casa,"invalida")
print(resultado)