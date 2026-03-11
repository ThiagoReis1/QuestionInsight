from numpy import*
vtempo= array(eval(input("tempo")))
vperc= array(eval(input("percentual")))
i= 0 #contador de percentual
j= 0 #contador de tempo
consumo=0
while(i<size(vperc)):
	consumo= consumo + (vtempo[j]*((vperc[i]/100)*5))
	i= i+1
	j= j+1
print(round(consumo,2))