# faça seu código aqui!
x = input("entrada de A,B,C,D e E: ")
quan = int(input("quantidade desejada: "))
vt = 25.90*quan

if(x == "B"):
	vt = vt - vt*0.10
	
print(round(vt, 2))