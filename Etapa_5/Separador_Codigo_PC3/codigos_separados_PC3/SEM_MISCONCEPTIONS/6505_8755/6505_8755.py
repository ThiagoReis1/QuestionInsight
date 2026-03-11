# faça seu código aqui!
t= input("tipo de combo: ")
q= int(input("quantidade de combos:"))
vc=30
qd=vc*q

if t.upper()=="a":
	print(round(qd,2))
if t.upper()=="b":
	print(round(qd,2))
else: 
	t.upper()="c"
	d= qd*(0.15)
	qt=qd-d
	print(round(qt,2))
	