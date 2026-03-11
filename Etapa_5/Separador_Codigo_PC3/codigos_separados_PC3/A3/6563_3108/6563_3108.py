diaria = 175
estadia = int(input())

if(estadia < 15):
	taxa = 20
if(estadia == 15):
	taxa = 16
if(estadia > 15):
	taxa = 10
	
total = diaria * estadia + taxa
print("total= ", round(total,2))