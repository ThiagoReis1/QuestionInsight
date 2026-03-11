from numpy import*

estados = input("estados:").upper().split(",")

somas = zeros(5,dtype=int)

for i in range (size(estados)):
	if (estados[i] == "AM"):
		somas[0] = somas[0] + 1
	elif (estados[i] == "PE"):
		somas[1] = somas[1] + 1
	elif (estados[i] == "MG"):
		somas[2] = somas[2] + 1
	elif (estados[i] == "SP"):
		somas[3] = somas[3] + 1
	elif (estados[i] == "RS"):
		somas[4] = somas[4] +1

print(max(somas))
print(somas)

