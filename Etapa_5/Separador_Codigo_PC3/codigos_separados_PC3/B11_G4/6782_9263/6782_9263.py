idade=int(input("ano do seu nascimento:  "))
pais=input("em qual pais voce esta ? (B - brasil / E - estados unidos):   ")

pais = pais.upper()

aniv=idade-2023

if(pais == "B") and (aniv>=18):
	print("sim")
	
else:
	n= 18-aniv
	print(n)
	
if(pais == "E") and (aniv >=16):
	print("sim")
	
else:
	n= 16-aniv
	print(n)