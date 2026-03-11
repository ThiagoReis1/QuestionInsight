p = float(input("Pressão:"))
n = float(input("Mols:"))
c = float(input("Temperatura:"))

t = c + 273.15
v = (n*0.082*t)/p
print(v)