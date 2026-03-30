#declarar
v1: int
v2: int
v3: int
v4: int

#inicio
def ler_valores():
	global v1 
	global v2 
	global v3

	v1 = int(input())
	v2 = int(input())
	v3 = int(input())

def ordenar4():
	if(v1 > v2 or v2 > v3):
		print("sequencia invalida")
	else:
		v4 = int(input())
		if(v3 < v4):
			print(v1,v2,v3,v4, end=" ")
		elif(v2 < v4):
			print(v1,v2,v4,v3, end=" ")
		elif(v1 < v4):
			print(v1,v4,v2,v3, end=" ")
		else:
			print(v4,v1, v2, v3, end=" ")
	#fim
def main():
	ler_valores()
	ordenar4()
main()