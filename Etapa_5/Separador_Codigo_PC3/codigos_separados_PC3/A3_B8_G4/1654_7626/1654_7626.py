from numpy import*

p= input("").upper().split(",")

m= 0
j=0
x= 0
y=0
z=0
novo= ("")
for i in range(len(p)):
	if p[i] == "AM":
		m +=1
	elif p[i]== "PE":
		j +=1
	elif p[i] == "MG":
		x= x+1
	elif p[i] == "SP":
		y= y + 1
	elif p[i] == "RS":
		z= z+1
	novo= [m, j, x, y, z]
print(max(novo))
print(array(novo))



