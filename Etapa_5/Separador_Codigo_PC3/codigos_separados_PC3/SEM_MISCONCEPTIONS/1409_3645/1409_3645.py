ataque = input()
val_1 = int(input())
val_2 = int(input())
val_3 = int(input())
val_4 = int(input())
if (ataque == 'espada'):
	kill = 24 + val_1 + val_2 + val_3 + val_4
else:
	kill = (val_1 + val_2 + val_3)* val_4
print(kill)