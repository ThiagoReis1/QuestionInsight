E=input("entre com o estado: ") .upper()
C=input("entre com a cidade: ") .upper()

if(E=="amazonas") or (E=="para"):
	if(E=="amazonas"):
		if(C=="Manaus"):
			print("coroado")
		if(C=="parintins"):
			print("palmares")
	if(E=="para"):
		if(C=="belem"):
			print("cidade_velha")
		if(C=="santarem"):
			print("coroado")
			
else:
	print("bairro_nao_identificado")