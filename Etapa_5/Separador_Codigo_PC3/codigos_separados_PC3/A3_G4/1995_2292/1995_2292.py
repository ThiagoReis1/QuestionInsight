x = input("aminoacido: ").lower()
o = 15.9994
c = 12.011
n = 14.0067
e = 32.066
h = 1.00794

if(x=="aspartato"):	
	soma = ((c*4) + (h*6) + (n*1) + (o*4))
	print(round(soma, 2))
elif(x=="cisteina"):
	soma = ((c*3) + (h*7) + (n*1) + (o*2) + (s*1))
	print(round(soma, 2))
elif(x=="metionina"):
	soma = ((c*5) + (h*11) + (n*1) + (o*2) + (s*1))
	print(round(soma, 2))
else:
	print("Entrada: X")
	pr