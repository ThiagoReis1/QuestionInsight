from numpy import*

BANANA=0.97
BIFE=2.95
FEIJOADA=1.27
OMELETE=1.04
TOMATE=0.2
ali=array(eval(input("n:")))
quant=array(eval(input("n: ")))

if(BANANA and BIFE and FEIJOADA and OMELETE and TOMATE):
	x= ali*quant
	y=sum(x)

	print(round(y,2))