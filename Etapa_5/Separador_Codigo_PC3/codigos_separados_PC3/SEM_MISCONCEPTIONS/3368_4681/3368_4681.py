a= input("escala:")
b= float(input("temperatura:"))
if (a.upper()=="C"):
   mensagem=(273.15)+b
	
else:
	mensagem=b-(273.15)
print(round(mensagem,2))
	
	