from numpy import*
v= array(eval(input("Palavras: ")))
p= input("Palavra normal: ")

p1= p.replace("R", "L")
i=0

while(i < size(v)):
	if(p1 == v[i]):
		print(i)
	i= i + 1

print("NAO ENCONTRADA")
		
	