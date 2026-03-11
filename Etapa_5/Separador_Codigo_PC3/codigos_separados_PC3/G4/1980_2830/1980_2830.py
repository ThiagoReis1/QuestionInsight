ne = input().upper()
nc = input().upper()

if( ( (ne == "AMAZONAS") or (ne == "PARA") ) and ((nc == "MANAUS") or (nc == "PARINTINS") or (nc == "BELEM") or (nc == "SANTAREM"))):
	if( (ne == "AMAZONAS") and (nc == "MANAUS") ):
		print("COROADO")
	elif((ne == "AMAZONAS") and (nc == "PARINTINS")):
		print("PALMARES")
	elif((ne == "PARA") and (nc == "BELEM")):
		print("CIDADE VELHA")
	elif((ne == "PARA") and (nc == "SANTAREM")):
		print("CENTRO")
	else:
		print("BAIRRO NAO IDENTIFICADO")
else:
	print("BAIRRO NAO IDENTIFICADO")
		
