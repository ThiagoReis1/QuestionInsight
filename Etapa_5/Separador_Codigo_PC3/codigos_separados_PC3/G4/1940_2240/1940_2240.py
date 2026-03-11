aminoacido = input("digite o nome do aminoacido: ").upper()

O = 15.9994
C = 12.011
N = 14.0067
H = 1.00794

 						  
if(aminoacido == "TREONINA"):
   msg = ((C*4)+ (H*9)+ (N) + (O*3))

else:
	msg = ((C*5)+ (H*8)+ (N*1) + (O*4))
	
print(round(msg, 2))
