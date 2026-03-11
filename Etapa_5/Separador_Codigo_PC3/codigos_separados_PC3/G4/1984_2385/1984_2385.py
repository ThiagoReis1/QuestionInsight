a=input()
b=input()
if(((a.upper()=="CAMPEAO")and (b.upper()=="11-VEZES")) or ((a.upper()=="CAMPEAO")and (b.upper()=="05-VEZES")) or ((a.upper()=="VICE-CAMPEAO")and (b.upper()=="01-VEZ")) or ((a.upper()=="VICE-CAMPEAO")and (b.upper()=="04-VEZES")) ):
	if((a.upper()=="CAMPEAO")and (b.upper()=="11-VEZES") ):
		print("REAL MADRID")
	if((a.upper()=="CAMPEAO")and (b.upper()=="05-VEZES")):
		print("BARCELONA")
	if((a.upper()=="VICE-CAMPEAO")and (b.upper()=="01-VEZ")):
		print("CHELSEA")
	if((a.upper()=="VICE-CAMPEAO")and (b.upper()=="04-VEZES")):
		print("MILAN")
	
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")