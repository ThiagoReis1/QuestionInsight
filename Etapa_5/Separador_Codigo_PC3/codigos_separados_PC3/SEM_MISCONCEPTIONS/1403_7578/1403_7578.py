nomedaarmadura=input("nome da armadura")
fd=int(input("valor entre 1 e 8"))

if(nomedaarmadura=="malha"):
	r=15*fd-1
else:
	r=20*fd-18
print(r)