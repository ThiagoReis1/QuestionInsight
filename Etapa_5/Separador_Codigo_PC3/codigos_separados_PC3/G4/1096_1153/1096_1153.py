num= float(input("num"))
p1= num//10000
r1= num%10000
p2= r1//100
r2= p2%100
p3= r2//1
soma=(p1 ** 3) + ((p2-p3) ** 3) + (p3 ** 3)
if(soma == num):
	print(num, "atende a propriedade")
else:
	print(soma)