pa=input("Digite o nome do Pais: ")
cid=input("Digite o nome da Cidade: ")
if(pa=="Italia")and(cid=="Roma"):
	print("LATINA".upper())
elif(pa=="Italia")and(cid=="Florenca"):
	print("SIENA".upper())
elif(pa=="Espanha")and(cid=="Frigiliana"):
	print("MALAGA".upper())
elif(pa=="Espanha")and(cid=="Madrid"):
	print("MADRID".upper())
else:
	print("PROVINCIA NAO IDENTIFICADA".upper())