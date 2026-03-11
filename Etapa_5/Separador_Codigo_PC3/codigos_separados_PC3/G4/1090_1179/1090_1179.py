c1=float(input ("c1: "))
c2=float(input ("c2: "))
c3=float(input ("c3: "))
c4=float(input ("c4: "))
limite = float (input("limite: "))
soma= round(c1+c2+c3+c4, 2)
if(soma <= limite):
	print(soma)
	print("Sim")
else:
	print(soma)
	print("Nao")