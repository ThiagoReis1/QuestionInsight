p = int(input("Peso: "))
d = int(input("Distancia: ")) 
c = int(input("Codigo: "))

kilo = 25
km = 0.10

if(c==1):
	icms = 17.0
if(c==2):
	icms = 17.5
if(c==3):
	icms = 18
if(c==4):
	icms = 20
	
preco = ((p*kilo)+(d*km))

picms = preco * icms/100
pt = preco + picms

s = ((p*25)+(d*0.10))*(1+icms/100)

print(round(s,2))