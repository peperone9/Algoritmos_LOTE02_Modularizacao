n1: float
n2: float

def ler_numeros():
	global n1
	global n2
	n1 = float(input())
	n2 = float(input())
	
def mostra_maior():
	if(n1 != n2):
		if(n1 > n2):
			print("maior:", n1)
		else:
			print("maior:", n2)
	else:
		print("os numeros são iguais")

def main():
	ler_numeros()
	mostra_maior()

main()
