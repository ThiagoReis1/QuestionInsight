from numpy import*

n = input("Pais: ").upper().split(',')
a = zeros(5, dtype=int)

for i in n:
		if(i == "AR"):
			a[0] = a[0] + 1
		elif(i == "BR"):
			a[1] = a[1] + 1
		elif(i == "CL"):
			a[2] = a[2] + 1
		elif(i == "CO"):
			a[3] = a[3] + 1
		elif(i == "UY"):
			a[4] = a[4] + 1
			
print(max(a))
print(a)
		