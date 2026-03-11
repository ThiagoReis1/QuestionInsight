# faça seu código aqui!
qp=float(input("pratos: "))
s=input("s ou n: ")

rei=qp*40
des=rei*0.05
total=rei-des
if s=="s":
	print(round(total, 2))
else:
	print(round(rei, 2))
	
			