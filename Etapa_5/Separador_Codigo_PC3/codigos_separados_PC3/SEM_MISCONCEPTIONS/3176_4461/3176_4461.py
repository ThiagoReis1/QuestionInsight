from numpy import*

v = array(eval(input("palavra: ")))
vo = ["a","e","i","o","u"]
b =0
n=0

for i in range(size(v)):
   for i in range(size(vo)):
		if(v[i]  == vo[i]):
			b =+1
		elif(v[i]!= vo[i]):
			n =+1
		
print(b)
print(n)