from numpy import*
qt = array(eval(input("turmas")))
imp = 0
for i in range ( size(qt)):
	if(qt[i]%2 != 0):
		imp = imp + 1
print(imp) 
vet = zeros(imp, dtype = int)
for i in range (size(qt)):
	if(qt[i]%2 != 0):
		vet = i
		
print(vet)
		
	
