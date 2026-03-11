#conversao

unit= (input("Digite a unidade de medida K/M:").upper())
med= float(input("Digite o valor da medida:"))

if (unit=="K"):
	
	conversao= med / 1.60934
	
else:
    conversao=  med * 1.60934
		
print(round( conversao, 2))
	      