from numpy import*
face = array(eval(input("Face dos dados tiradas pelo jogador: ")))

i = 0
pont = 0
while i < size(face):
	if face[i] == 1:
		pont = pont + 10
		i = i + 1
	elif face[i] ==  2:
		pont = pont + 5
		i = i + 1
	elif face[i] == 3:
		pont = pont + 0
		i = i + 1
	elif face[i] == 4:
		pont = pont + 5
		i = i + 1
	elif face[i] == 5:
		pont = pont + 20
		i = i + 1
	elif face[i] == 6:
		pont = pont + 10
		
print(pont)
		
		