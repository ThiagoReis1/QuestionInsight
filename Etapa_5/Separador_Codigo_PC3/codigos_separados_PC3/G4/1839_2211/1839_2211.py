#equação de calyperon

#pressao - (p) dada em atm

#volume - (v)

#temperatura absoluta - (T) dada em graus

#Numero de mols - (n)

#p.V=n.R.T

#R= constante universal dos gases perfeitos... é 
#0,082atm*litro*K**-1*mol**-1


#v=529.966 p=0.05 n=1 t=50 (323,15)
#v/p=10599,32

p=float(input("Pressao em atm:"))
n=int(input("Número de mols de um gás:"))
T=float(input("Temperatura em graus Celsius"))
R=0.082
V=(n*R*(T+273.15))/p

print (V) #em litros

