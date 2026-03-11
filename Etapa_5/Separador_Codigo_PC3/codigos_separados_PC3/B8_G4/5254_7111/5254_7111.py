pp= float(input("qual o preco do produto: "))
cod= int(input("qual o codigo da regiao: "))

f1=pp*0.1
f2=pp*0.08
f3=0
f4=pp*0.02
dBF=0.4

if (cod==1):
	VT=(pp - pp * dBF) + pp * (f1/100)
elif (cod==2):
	VT=(pp - pp * dBF) + pp * (f2/100)
elif (cod==3):
	VT=(pp - pp * dBF) + pp * (f3/100)
elif (cod==4):
	VT=(pp - pp * dBF) + pp * (f4/100)
print(round(VT,2))