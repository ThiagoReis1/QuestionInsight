p = int(input("prato"))
s = int(input("sobremesa"))
b = int(input("bebida"))
cp= 0
cs = 0 
cb = 0
print("Entradas:", p,",",s,",",b)
if (p==1):
	cp = cp+180
elif(p==2):
	cp = cp+230
elif(p==3):
	cp= cp+250
elif(p==4):
	cp =cp+350
if (s==1):
	cs = cs+75
elif(s==2):
	cs = cs+110
elif(s==3):
	cs= cs+170
elif(s==4):
	cs =cs+200	
if (b==1):
	cb =cb+20
elif(b==2):
	cb = cb+70
elif(b==3):
	cb= cb+100
elif(b==4):
	cb =cb+65
C = cp+cs+cb	
if(p<1 or p>4 or s<1 or s>4 or b<1 or b>4):
	print("Dados invalidos")	
else:
	print("Calorias:", C,"cal")



