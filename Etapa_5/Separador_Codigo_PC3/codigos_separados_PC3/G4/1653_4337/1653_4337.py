x = input()
x = x.split(',')

ar = 0
br = 0
cl = 0
co = 0
uy = 0

for i in x:
	if(i == "AR"):
		ar = ar + 1
	if(i == "BR"):
		br = br + 1
	if(i == "CL"):
		cl = cl + 1
	if(i == "CO"):
		co = co + 1
	if(i == "UY"):
		uy = uy + 1
if(ar > br > cl > co > uy):
	print(ar)
	