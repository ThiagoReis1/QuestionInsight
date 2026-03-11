c=input("")
i=int(input(""))
print("Entradas:",c,",",i)
if(c=="Porto Velho"):
	t=500
elif(c=="Santarem"):
	t=370
elif(c=="Belem"):
	t=600
elif(c=="Tefe"):
	t=360
elif(c=="Tabatinga"):
	t=550

if(i<=2 and i>0 ):
	t=0
	print("Passagem: R$",round(t,2))
elif(i>=3 and i<=12):
	t=t/2
	print("Passagem: R$",round(t,2))
elif(i>12 and i<65):
	t=t
	print("Passagem: R$",round(t,2))
elif(i>65 and i<=150):
	t=t-t*0.3
	print("Passagem: R$",round(t,2))
else:
	print("entradas invalidas")
	