from numpy import*

vet = array(eval(input("Notas: ")))

x = sum(vet)- min(vet)

m= x/3

print(round(m,2))

if(m >= 5):
	print("APROVOU")
else:
	print("REPROVOU")