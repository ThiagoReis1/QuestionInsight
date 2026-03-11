from numpy import*
est = input().upper().split(',')

a = 0
b = 0
c = 0
d = 0
e = 0
for i in range(size(est)):
	if(est[i] == "az".upper()):
		a = a + 1
	elif(est[i] == "ca".upper()):
		b = b + 1 
	elif(est[i] == "fl".upper()):
		c = c + 1 	
	elif(est[i] == "pa".upper()):
		d = d + 1 
	elif(est[i] == "wi".upper()):
		e = e + 1 
vet = array([a, b,c,d,e])
print(max(a,b,c,d,e))
print(vet)
