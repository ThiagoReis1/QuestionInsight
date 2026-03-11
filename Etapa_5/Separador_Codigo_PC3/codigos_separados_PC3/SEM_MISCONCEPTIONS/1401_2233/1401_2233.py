nome=input("nome do dragao")
baforadas=int(input("quantidade"))
if(nome=="maritimo"):
	print("Viserion")
	dano=baforadas*40
else:
	print("Drogon")
	dano=baforadas*150

print(dano)
