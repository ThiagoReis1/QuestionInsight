E = input("bolo ou salgado?: ")
Q = int(input("Quantidade?: "))
QC = int(input("quantidade de cappuccions?: "))

E1 = E.lower()

if ( E1 == "b" ):
	R = Q * 5 + QC * 7.50
else:
	R = Q * 4 + QC * 7.50
	
print(round(R, 1))