from numpy import*
m=input("escreva a palavra: ")
i=0
v=len(m)
d=0
while i < v:
	p=m[i]
	if p.upper() == "M":
		print(i)
		d=d+1
	i=i+1
if d == 0:
	print("nao achei")