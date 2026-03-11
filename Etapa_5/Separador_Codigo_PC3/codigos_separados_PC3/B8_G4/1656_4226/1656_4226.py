from numpy import *
v = input(" >  ").upper()
v = v.split(',')
nat = array([0,0,0,0,0])
L = len(v)

for i in range(L):
	if v[i] == "BE":
		nat[0] += 1
	elif v[i] == "ES":
		nat[1] += 1
	elif v[i] == "FR":
		nat[2] += 1
	elif v[i] == "IT":
		nat[3] += 1
	elif v[i] == "PT":
		nat[4] += 1
print(max(nat))
	
#nat = str(nat)
#nat = nat.replace(",","")
print(nat)