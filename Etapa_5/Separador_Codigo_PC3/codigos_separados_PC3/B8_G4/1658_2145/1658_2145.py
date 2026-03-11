from numpy import*
pais = input("Digite os paises: ").split(',')
pess = zeros(5, dtype = int)
for i in range(size(pais)):
	if pais[i].upper() == "CHN":
		pess[0] = pess[0] + 1
	elif pais[i].upper() == "JPN":
		pess[1] = pess[1] + 1
	elif pais[i].upper() == "KOR":
		pess[2] = pess[2] + 1
	elif pais[i].upper() == "MGL":
		pess[3] = pess[3] + 1
	elif pais[i].upper() == "THA":
		pess[4] = pess[4] + 1
		
print(max(pess))
print(pess)