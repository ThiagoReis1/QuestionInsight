consumo= int(input())

if consumo<150:
	conta= consumo*0.60+5
elif consumo>=150 and consumo<250:
	conta= consumo*0.65+8
elif consumo>=250 and consumo<350:
	conta= consumo*0.70+12
elif consumo>350:
	conta= consumo*0.75+16
	
print(round(conta, 2))