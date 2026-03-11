

a=float(input('Peso do produto:'))
b=float(input('Distancia entre o ponto de origem e o ponto de destino:'))
c=int(input('Codigo do estado:'))

j=17.0
k=17.5
l=18.0
m=20.0

if(c==1):
	m=(a*25+b*0.10)*(1+j/100)
	print(round(m,2))
elif(c==2):
	m1=(a*25+b*0.10)*(1+k/100)
	print(round(m1,2))
elif(c==3):
	m2=(a*25+b*0.10)*(1+l/100)
	print(round(m2,2))

elif(c==4):
	m3=(a*25+b*0.10)*(1+m/100)
	print(round(m3,2))
else:
	print('Valores invalidos')