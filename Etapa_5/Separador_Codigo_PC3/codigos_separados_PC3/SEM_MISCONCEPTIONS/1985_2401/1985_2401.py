regiao=input()
estado=input()
if(regiao=="Norte"and estado=="Amazonas"):
	print("Universidade Federal Do Amazonas".upper())
elif(regiao=="Norte"and estado=="Roraima"):
	print("Universidade Federal De Roraima".upper())
elif(regiao=="Sul"and estado=="Parana"):
	print("Universidade Federal Do Parana".upper())
elif(regiao=="Sul"and estado=="Santa Catarina"):
	print("Universidade Federal De Santa Catarina".upper())
else:
	print("universidade nao identificada".upper())
	