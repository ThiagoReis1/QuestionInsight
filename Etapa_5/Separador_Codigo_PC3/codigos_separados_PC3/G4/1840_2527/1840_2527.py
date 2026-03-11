n= int(input("n de mols"))
v= float(input("volume"))
t= float(input("temperatura")) + 273.1
r= 0.082057
P= (n*r*t)/v

print (P)
