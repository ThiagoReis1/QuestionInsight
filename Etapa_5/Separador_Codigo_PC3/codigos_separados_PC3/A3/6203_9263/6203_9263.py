#-------leao-----------------------------------------------
leaoat=float(input("altura atual: "))
leaotx=float(input("percentual de crescimento ao ano: "))
#------macaco----------------------------------------------
altura_macaco = 1.4
taxa_macaco = 0.06
#----------------------------------------------------------
macaco=altura_macaco+taxa_macaco
leao=leaoat+leaotx

l=0

while(leao>macaco):
	if(leao>macaco):
		l=leao+leaotx
	else:
		print("cresca")
	leaoat=float(input("altura atual: "))
	leaotx=float(input("percentual de crescimento ao ano: "))

print(l)