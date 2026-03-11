a = input("aminoacido: ").lower()
O= 15.999
C= 12.011
N= 14.006
H= 1.007
arginina = (C*6) + (H*15) + (N*4) + (O*2)
tirosina = (C*11) + (H*11) + (N) + (O*3)
triptofano = (C*11) + (H*11) + (N*2) + (O*2)
if(a=="arginina"):
   print(round(arginina,2))
elif(a=="tirosina"):
    print(round(tirosina,2))
elif(a=="triptofano"):
    print(round(triptofano,2))
else:
	print("Entrada:", a)
	print("Dado Invalido")