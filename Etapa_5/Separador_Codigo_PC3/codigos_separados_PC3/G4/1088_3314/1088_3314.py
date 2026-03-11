var1 = float(input("Digite a primeira nota: "))
var2 = float(input("Digite a segunda nota: "))
var3 = float(input("Digite a terceira nota: "))
var4 = float(input("Digite a quarta nota: "))
var5 = float(input("Digite a quinta nota: "))
var6 = ((var1+var2+var3+var4+var5)/5)
print(round(var6,2))
if var6 >= 7.00:
	 print("Aprovacao")
else:
	 print("Reprovacao por nota")