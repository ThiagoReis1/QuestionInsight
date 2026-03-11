from numpy import*
face = array(eval(input("face: ")))

cont= 0
acumulador = 0
							
while(cont < size(face)):
		if(face[cont] == 1):
			acumulador +=  10
		elif(face[cont] == 2):
			acumulador +=  5
		elif(face[cont] == 3):
			acumulador += 10
		elif(face[cont] == 4):
			acumulador += 5
		elif(face[cont] == 5):
			acumulador += 10
		elif(face[cont] == 6):
			acumulador += 5
			
		cont += 1

print(acumulador)

					