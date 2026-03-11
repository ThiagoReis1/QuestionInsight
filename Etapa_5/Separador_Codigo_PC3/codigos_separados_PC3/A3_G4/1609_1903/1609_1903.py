from numpy import*

vp = array(eval(input("ceboles: ")))
pa = input("palavra: ").upper()

i = 0
j = 0
c = pa.replace("R","L")

while(i < size(vp) and c != vp[i]):
	i += 1

if(i < size(vp)):
	print(i)
else:
	print("NAO ENCONTRADA")