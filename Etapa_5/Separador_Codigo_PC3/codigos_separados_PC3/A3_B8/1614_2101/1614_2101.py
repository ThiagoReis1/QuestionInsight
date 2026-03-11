from numpy import*

alim = array(eval(input("digite um alimento:").upper()))
quant = array(eval(input("digite a quantidade:")))
i = 0
calo1=0
calo2=0
calo3=0
calo4=0
calo5=0
while (i < size(alim) ):
	
	if (alim[i] == "BANANA"):
		calo1 = quant[i] * 0.97
	elif (alim[i]=="BIFE"):
		calo2 = quant[i]* 2.95
	elif (alim[i]=="FEIJOADA"):
		calo3 = quant[i] * 1.27
	elif (alim[i]== "OMELETE"):
		calo4 = quant[i] *1.04
	elif (alim[i] == "TOMATE"):
		calo5 = quant[i] *0.2	
	i=i+1

soma = calo1 + calo2 +calo3 + calo4 +calo5

print(round(soma, 2))	