tipo_ataque = (input(":"))
sorteio = int(input(":"))
turno = int(input(":"))				
if (tipo_ataque == "cauda"):
	pontos = sorteio * turno
else:
	pontos = 2 * sorteio * turno
print (pontos)