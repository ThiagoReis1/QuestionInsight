item = input("digite C para Coxihas ou E para Esfirras:").upper()
a = int(input("digite a quantidade de coxinhas ou esfirras:"))
s = int(input("digite a quantidade de sucos:"))

c = 2
e =4.5
su = 6


if (item=="C"):
	m = (c*a)+(su*s)
	
	print(round(m, 2))
	
else:
	p=(e*a)+(su*s)
	print(round(p,2))