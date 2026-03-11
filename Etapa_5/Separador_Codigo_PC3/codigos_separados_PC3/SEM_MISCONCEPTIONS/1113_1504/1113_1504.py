ida = int(input("qual a idade:"))
pes =float(input("qual o peso:"))

print("Entradas:", ida, "anos e", pes ,"kg")
if(ida < 0) and (pes < 0):	
	print("Dados invalidos")
#PESSOAS ATE 20
elif(ida <= 20): 
	if(pes <= 60):
		print("Grupo de risco: 9")	
elif(pes > 60) and (ida <= 20):
		print("Grupo de risco: 8")
else:	
	print("Grupo de risco: 7")
#PESSOAS MAIOR QUE 20
elif(ida > 20): 
elif(pes <= 60):
	print("Grupo de risco: 6")
elif(pes > 60) and (ida > 20):
	print("Grupo de risco: 5")
else:
	print("Grupo de risco: 4")
#MAIOR QUE 50
elif(ida > 50): 
	if(pes <= 60):
		print("Grupo de risco: 3")
elif(pes > 60) 
	if(ida > 50):
		print("Grupo de risco: 2")
else:
	print("Grupo de risco: 1")		