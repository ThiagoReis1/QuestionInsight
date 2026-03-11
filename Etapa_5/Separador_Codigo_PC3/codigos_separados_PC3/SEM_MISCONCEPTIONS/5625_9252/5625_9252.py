TouS = input("tapioca(T) ou salgado(S): ").upper()

qtdeTouS = int(input("Quantidade(T)ou(S): "))

qtdeA = int(input("Acai: "))

if(TouS == "T"):
	total = qtdeTouS*5.5 + qtdeA*10
else:
	total = qtdeTouS*4 + qtdeA*10
	
print(round(total,2))	

