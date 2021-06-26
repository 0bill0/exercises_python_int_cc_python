#coding: utf-8
#exercicio semana 3
import os, sys
import math

def bhaskara(a,b,c):
	x_linhas = []
	delta = b**2 - 4 * a * c
	if delta == 0:
		x1 = (-b + math.sqrt(delta)) / (2*a)
		x_linhas.append(x1)
		x_linhas.append(delta)
	else:
		if delta < 0:
			x_linhas = None
		else:
			x1 = (-b + math.sqrt(delta)) / (2*a)
			x2 = (-b - math.sqrt(delta)) / (2*a)
			x_linhas.append(x1)
			x_linhas.append(x2)
			x_linhas.sort()
	return x_linhas

if __name__ == "__main__":
	a = float(eval(input("Digite o valor de a: ")))
	b = float(eval(input("Digite o valor de b: ")))
	c = float(eval(input("Digite o valor de c: ")))

	b = bhaskara(a,b,c)
	if b is None:
		print('esta equação não possui raízes reais')
	else:
		if b[1] == 0:
			print('a raiz dupla desta equação é ',b[0])
		else:
			print('as raízes da equação são', str(b[0]) +' e', str(b[1]))