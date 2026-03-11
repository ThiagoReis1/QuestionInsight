ch=1.5
tx=0.02
ps=float(input(""))
tp=float(input(""))

cont=0

while (ps<ch):
	ps+=tp
	ch+=tx
	cont+=1
print(cont)
	