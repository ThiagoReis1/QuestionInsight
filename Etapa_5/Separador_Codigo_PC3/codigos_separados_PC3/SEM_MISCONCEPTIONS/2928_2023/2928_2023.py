# Conservação do momentum:peixes

mass_g = float(input("digite a massa do peixe grande:"))
volu_g = float(input("digite o volume:"))
mass_p = float(input("digite a massa do peixe pequeno:"))
volu_p = float(input("digite o volume:"))

v_fin = ((mass_g*volu_g)-(mass_p*volu_p))/(mass_g+mass_p)
print(v_fin)