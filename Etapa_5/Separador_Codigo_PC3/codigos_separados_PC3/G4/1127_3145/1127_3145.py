cl=input()
gent=["pentoshi","bravosiano","liseno","qohorik","norvoshi","myrano","tyroshi","volantino","lorathi"]
if cl=="Pentos":
	g=gent[0]
elif cl=="Bravos":
	g=gent[1]
elif cl=="Lys":
	g=gent[2]
elif cl=="Qohor":
	g=gent[3]
elif cl=="Norvos":
	g=gent[4]
elif cl=="Myr":
	g=gent[5]
elif cl=="Tyrosh":
	g=gent[6]
elif cl=="Volantis":
	g=gent[7]
elif cl=="Lorath":
	g=gent[8]
else:
	g=2
if g==2:
	print("Entrada",cl,"invalida")
else:
	print(g)