#As Duas raízes positivas:1 -7 12
#As duas raízes negativas: 1 7 12
#Raiz 1 Positiva e Raiz 2 negativa: 1 -5 -6
#Raiz 2 Positiva e Raiz 1 Negativa: -1 5 6
#Raiz real nao  existente: 1 -1 12 | 0 -1 12


from math import sqrt
from sys import exit
a: float
b: float
c: float
delta: float

def ler_coeficientes():
	global a 
	global b 
	global c
	
	a = float(input("Coeficiente A: "))
	b = float(input("Coeficiente B: "))
	c = float(input("Coeficiente C: "))

def valida_delta():
	if(delta < 0 or a == 0):
		print("Nao possuem raízes reais para X")
		exit()

def calcula_raizes():
	global delta 
	x: float

	delta = (b*b - 4*a*c)
	valida_delta()
	x =  (-b + sqrt(delta)) / (2*a)
	print("Raiz 1:", x)
	x = (-b - sqrt(delta)) / (2*a)
	print("Raiz 2:", x)

def main():
	ler_coeficientes()
	calcula_raizes()
main()

