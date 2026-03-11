altura_luna = 1.65
taxa_luna = 0.02
height = float(input())
growth = float(input())
anos = 0
while(height < altura_luna):
	altura_luna = altura_luna + taxa_luna
	height = height + growth
	anos = anos + 1
print(anos)