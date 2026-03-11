nome = input("insira: ")
des = int(input("insira: "))
d1 = int(input("insira: "))
d2 = int(input("insira: "))
s = d1 + d2
if ((1<=d1) and (d1>=10) and (des>0) and (nome == "CIMITARRA") or (nome == "KATANA") or (nome == "Sabre")):
   if (nome == "CIMITARRA") :
	   print(2*s + 2*des)