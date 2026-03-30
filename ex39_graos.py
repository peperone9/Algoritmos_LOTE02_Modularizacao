
casa: int
graos: int
total_graos: int

total_graos = 0
casa = 0
while(casa < 64):
	grao = 2**casa
	total_graos += grao
	casa += 1
print("\ntotal de graos: ", total_graos)
