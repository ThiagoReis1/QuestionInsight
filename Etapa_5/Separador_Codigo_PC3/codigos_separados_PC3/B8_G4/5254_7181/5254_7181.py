pc=float(input("preco:  "))
cd=int(input("regiao:  "))

if(cd==1):
	ft=pc*0.1
elif(cd==2):
	ft=pc*0.08
elif(cd==3):
	ft=0
elif(cd==4):
	ft=pc*0.02


vdv=(pc-(pc*0.4)+pc*(ft/100))

print(round(vdv, 2))