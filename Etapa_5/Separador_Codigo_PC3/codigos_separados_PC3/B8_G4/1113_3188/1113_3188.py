#Idade (ida)
ida=int(input("Idade:"))
#Peso(ps)
ps=float(input("Peso"))
print("Entrada: ", ida, "anos e" , ps, "kg")
if(ida>0 or ida<=130)and(ps>0 or ps<=550):
	if(ida<=20) and (ps<=60):
		gr="9"
	elif(ida<=20 and ps>60 or ps<=90):
		gr="8"
	elif((ida<=20) and (ps>90)):
		gr="7"
	elif((ida>20 or ida<=50) and ps<=60):
		gr="6"
	elif((ida>20 or ida<=50)and (ps>60 or ps<= 90)):
		gr="5"
	elif((ida>20) or (ida<=50 and ps>90)):
		gr="4"
	elif((ida>50)) and (ps<=60):
		gr="3"
	elif((ida>50) and (ps>60) or (ps<=90)):
		gr="2"
	elif((ida>50) and (ps>90)):
		gr="1"
	print("Grupo de Risco: ", gr)
else:
	print("Dados invalidos")