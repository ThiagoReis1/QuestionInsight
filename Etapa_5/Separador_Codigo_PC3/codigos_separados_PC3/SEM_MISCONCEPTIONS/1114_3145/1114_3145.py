velt=float(input())
tempv=float(input())
print("Entradas:", velt,"Km/h e",tempv,"h")
disp=velt*tempv

if disp<100:
		pp="Bravos"
elif disp<100+100:
		pp="Castamere"
elif disp<100+100+200:
		pp="Doriath"
elif disp<100+100+200+200:
		pp="Edoras"
elif disp<100+100+200+200+150:
		pp="Fangorn"
elif disp<100+100+200+200+150+400:
	pp="Gondor"
elif disp>=100+100+200+200+150+400:
	pp="Hogsmead"
if(velt<=0):
	print
print("Proxima parada:",pp)

	print("Dados invalidos")