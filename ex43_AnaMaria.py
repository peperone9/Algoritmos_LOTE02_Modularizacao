#Calcule e mostre quantos anos serão necessários para que
#Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3
#cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.

#declarar
a_ana: float #em metros
a_maria: float #em metros
anos: int

#converte cm em metros
C_ANA = 3/100 #crescimento ana
C_MARIA = 2/100 #crescimento maria
#inicio
a_ana = 1.10
a_maria = 1.5
anos = 0

print(f"ana: {a_ana:.2f} metros")
print(f"maria: {a_maria:.2f} metros")
print("QUANTO TEMPO ANA ULTRAPASSA A ALTURA MARIA? \n")

while(a_ana < a_maria):
	a_ana += C_ANA
	a_maria += C_MARIA
	anos += 1
print(f"tempo: {anos} anos")
#fim
