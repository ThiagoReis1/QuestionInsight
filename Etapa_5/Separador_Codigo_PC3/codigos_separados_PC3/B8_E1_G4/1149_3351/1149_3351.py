#Entrada
r = input("Insira a regiao: ")
#Condições
if(r.lower() == "ponta tempestade" or r.lower()== "ilha do dragao" or r.lower()=="campina" or r.lower() == "winterfell" or r.lower() == "rochedo casterly" or r.lower() == "pyke" or r.lower() == "correrio" or r.lower() == "ninho da aguia" or r.lower() == "dorne"):
	if(r.lower() == "ponta tempestade"):
		print("Baratheon")
	elif(r.lower()== "ilha do dragao"):
		print("Targaryen")
	elif(r.lower()=="campina"):
		print("Tyrell")
	elif(r.lower() == "winterfell"):
		print("Stark")
	elif(r.lower() == "rochedo casterly"):
		print("Lannister")
	elif(r.lower() == "pyke"):
		print("Greyjoy")
	elif(r.lower() == "correrio"):	
		print("Tully")
	elif(r.lower() == "ninho da aguia"):
		print("Arryn")
	elif(r.lower() == "dorne"):
		print("Martell")
else:
	print("Entrada", r, "invalida")