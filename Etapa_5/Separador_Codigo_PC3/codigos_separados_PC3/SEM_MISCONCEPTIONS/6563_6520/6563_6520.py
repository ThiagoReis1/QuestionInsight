# faça seu código aqui!

dias=int(input("dias reservados: "))
diaria=175

if dias < 15:
	total=dias*diaria + 20
elif dias == 15:
	total=dias*diaria + 16
else:
	total=dias*diaria + 10
print("total=",total)