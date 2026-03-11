Ninicial = int(input(""))
taxa = float(input(""))
newcel = int(input(""))

quinzenas = 0
t = taxa/100
x = 500000
while(Ninicial <= x):
	Ninicial = Ninicial - (Ninicial * t)
	c = Ninicial + newcel
	Ninicial = c
	quinzenas = quinzenas + 1
print(quinzenas)