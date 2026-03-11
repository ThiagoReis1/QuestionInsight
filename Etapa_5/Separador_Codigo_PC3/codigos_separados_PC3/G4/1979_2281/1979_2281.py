r = input("Qual o resultado da selecao: ")
v = (input("Quantas vezes tal resultado: "))

if(r!= "Campeao" and r!="Vice-Campeao") or (v!= "05-vezes" and v!="04-vezes" and v!="03-vezes"):
	print("selecao nao identificada".upper())
elif(r =="Campeao" and v=="05-vezes"):
	print("brasil".upper())
elif(r=="Campeao" and v=="04-vezes"):
	print("italia".upper())
elif(r=="Vice-Campeao" and v=="04-vezes"):
	print("alemanha".upper())
else:
	print("argentina".upper())