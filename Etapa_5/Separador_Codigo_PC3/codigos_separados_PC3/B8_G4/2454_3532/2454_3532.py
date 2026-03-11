A = float(input())

print("Entradas:", A , "," , B , "," , C)
if(A < B + C and B < A + C and C < A + B ):
	if(A == B and B == C and C == A):
		print("")
	elif(A == B or B == C or C == A):
			print("Tipo de triangulo: isosceles")
	elif(A != B or B != C or C != A):
			print("Tipo de triangulo: escaleno")