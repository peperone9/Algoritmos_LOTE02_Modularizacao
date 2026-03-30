#Aprovado: 10 9.5 10
#Exame: 6  6.5 6
#retido: 3 2.5 1
#Nota invalida: -1 2 3 10
from sys import exit
nota1: float
nota2: float
nota3: float
nota4: float

def ler_notas():
	global nota1
	global nota2 
	global nota3
	global nota4

	nota1 = float(input("primeira nota: "))
	nota2 = float(input("segunda nota: "))
	nota3 = float(input("terceira nota: "))
	nota4 = float(input("quarta nota: "))
	
	valida_notas()

def valida_notas():
	if(nota1 < 0 or nota2 < 0 or nota3 < 0 or nota4 < 0):
		print("Não existe nota negativa, por favor executar novamente o programa")
		exit()
	
def calcula_media():
	media: float
	media = (nota1 + nota2 + nota3 + nota4) / 4
	if(media >= 6):
		print("Aprovado")
	elif(media >= 3):
		print("Exame")
	else:
		print("RETIDO")

def main():
	ler_notas()
	calcula_media()

main()
