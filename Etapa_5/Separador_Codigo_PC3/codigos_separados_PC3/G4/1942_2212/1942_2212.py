#peso do aminoacido é (PM de cada atomo)
#(C6H10N3O2)Histidina:primeiro aminoacido
#(C5H10NO2)Prolina:Segundo aminoacido
AM = input("Nome do aminoacido:")
am = (AM).lower()
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
HI = (C*6)+(H*10)+(N*3)+(O*2)
PR = (C*5)+(H*10)+(N*1)+(O*2)
if am==("histidina"):
	print(round(HI,2))
else:
	print(round(PR,2))