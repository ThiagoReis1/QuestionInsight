p = float(input("peso: "))
d = float(input("distancia:  "))
c = int(input("codigo:  "))

kg = p*25.00
km = d*0.10

if(c == 1):
	T =(kg + km)*(1.0 + 17.0/100)
	print(round(T,2))
	
elif( c == 2):
	T = (kg + km)*(1.0 + 17.5/100)
	print(round(T,2))
elif(c == 3):
	T = (kg + km)*(1.0 + 18.0/100)
	print(round(T,2))
elif(c == 4):
	T = (kg + km)*(1.0 +  20.0/100)
	print(round(T,2))
