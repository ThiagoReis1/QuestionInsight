from numpy import*
v = input("paises: ").upper()
n = len(v)
print(v)
vc = zeros(5, dtype=int)
for i in range(0, n):
	if(v[i]=="BE"):
		vc[0] = v[0] + 1
	elif(v[i]=="ES"):
		vc[1] = v[1] + 1
	elif(v[i]=="FR"):
		vc[2] = v[2] + 1
	elif(v[i]=="IT"):
		vc[3] = v[3] + 1
	elif(v[i]=="PT"):
		vc[4] = v[4] + 1
k = max(vc)
print(k)
print(vc)