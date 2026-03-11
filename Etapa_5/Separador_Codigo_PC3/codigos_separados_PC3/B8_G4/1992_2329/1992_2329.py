aa = input("informe o nome do aa:") 
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
if ((aa.lower() == "glutamina") or (aa.lower() == "histidina") or (aa.lower() == "prolina")):
	if ((aa.lower() == "glutamina") and (aa.lower() != "histidina") and (aa.lower() != "prolina")):
		pm = ((C * 5) + (H * 8) + N + (O * 4))
	elif ((aa.lower() != "glutamina") and (aa.lower() == "histidina") and (aa.lower() != "prolina")):
		pm = ((C * 6) + (H * 10) + (N * 3) + (O * 2))
	elif ((aa.lower()!= "glutamina") and (aa.lower() != "histidina") and (aa.lower() == "prolina")):
		pm = ((C * 5) + (H * 10) + N + (O * 2))
	print(round(pm, 2))
else:
	print("Entrada:", aa)
	print("Dado Invalido")