s= input("se e (C/E):").upper()
qec = int(input("quantidade de esfirra ou coxinha:"))
qs = int(input("quantidade de suco:"))

if s == "C":
	z= (qec* 2) + (qs*6)
else: 
	z =(qec*4.50)+(qs*6)
print (z)
