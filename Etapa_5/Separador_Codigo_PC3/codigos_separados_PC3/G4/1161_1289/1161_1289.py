z=int(input("insira z: "))
h=int(input("insira h: "))
x=int(input("insira x: "))
y=int(input("insira y: "))
dia=1
b=h
while b>h:
	b=h-x
	x=z-y
	dia=dia+1
print(dia)