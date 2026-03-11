v = input("Palavra: ")
p = input("Palavra normal: ")
new = v.replace('L', 'R' )

i = 0

while(i < size(v)):
	if(v == p):
		print("a")
	else:
		print("erro")


print(new)