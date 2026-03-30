# 41. Mostre todas as possibilidades de 2 dados de forma que a
#soma tenha como resultado 7.

#declarar
d1: int
d2: int
i: int
j: int

#inicio
d1 = 1
d2 = 6

while(d1 <= d2):
	print(d1, d2, '=', d1 + d2)
	d1 += 1
	d2 -= 1
d1 = 6
d2 = 1
while(d1 >= d2):
	print(d1, d2, '=', d1 + d2)
	d1 -= 1
	d2 += 1
