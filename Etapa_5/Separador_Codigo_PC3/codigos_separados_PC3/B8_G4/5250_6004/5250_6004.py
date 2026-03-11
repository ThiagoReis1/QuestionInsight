v = float(input("velocidade do trem:  "))
t = float(input("tempo de viagem: "))

if (v<=0):
   print("Entrada", v,"km/h", "e", t,"h")
   print("Dados invalidos")
elif (v>=100):
	print("Entrada", v,"km/h", "e", "t","h")
	print("Proxima parada")