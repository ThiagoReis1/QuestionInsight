comando= input("digite T para torta e P para pastel:" ).lower()
com1= float(input("quantidade de tortas ou pastel:"))
cam2= float(input("quantidae de caputinos: "))

if comando=="p":
	precofinal= com1 * 5 + cam2*4.50
	
else: 
	precofinal= com1 *6 + cam2 * 4.50
	
print(precofinal)

 