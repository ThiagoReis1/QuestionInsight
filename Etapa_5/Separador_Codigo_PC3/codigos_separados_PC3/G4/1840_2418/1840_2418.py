m= float(input("Numero de mols:" ))
v= float(input("Volume do gás:" ))
t= float(input("Temperatura do gás:" ))
t2=t+273,1
p=(m*0.082057*t2)/ v
print(float(p))