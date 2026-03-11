p_gas=float(input("pressão do gas "))
mols=float(input("numero de mols "))
temp=float(input( "temperatura "))
t_kelvin=temp+273.15
R=0.082
V=mols*R*t_kelvin/p_gas
print(V)
