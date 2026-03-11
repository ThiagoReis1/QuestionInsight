p = float(input("Pressao:"))
n = float(input("Mols:"))
T = float(input("Temperatura:"))

R = 0.082
t_aux = T + 273.15

V = (n*R*t_aux) / p

print(V)