from numpy import*
s= input("Digite"). upper()
v = a.split(',')
be = 0
es = 0
fr = 0
it = 0
pt = 0

for i in range(len(v)):
	if v[i] == "BE":
		be += 1
	elif v[i] == "ES":
		es +=1
	elif v[1] == "FR":
	   fr +=1
	elif v[1] == "IT":
	   it +=1
	elif v[1] == "PT":
	   pt +=1

vet_z[0]= be
vet_z[0]= es
vet_z[0]= fr
vet_z[0]= it
vet_z[0]= pt

print(max(vet_z))
print(vet_z)

	
		
	

