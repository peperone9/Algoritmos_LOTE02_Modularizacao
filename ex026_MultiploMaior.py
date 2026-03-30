n1: int
n2: int

def ler_numeros():
	global n1
	global n2
	n1 = int(input())
	n2 = int(input())
	
def verifica_multiplo():
	if(n1 > n2):
		if(n2 != 0 and n1 % n2 == 0):
			print(n1,"e multiplo de", n2)
		else:
			print(n1,"nao e multiplo de", n2)
	else:
		if(n1 != 0 and n2 % n1 == 0):
			print(n2,"e multiplo de", n1)
		else:
			print(n2,"nao e multiplo de", n1)

def main():
	ler_numeros()
	verifica_multiplo()
main()