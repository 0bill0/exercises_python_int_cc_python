#coding: utf-8
import time
import timeit
import numpy as np
from random import randint, uniform
from csv import writer

def iniciar_matriz_randomicamente(tamanho):
	M = []
	for i in range(tamanho):
		#for (j=0;j<N;j++){
		linha=[]
		for j in range(tamanho):
			#x=rand()%10;
			x = randint(0,10)
			if x<5:
				linha.append(0)
			elif x<8:
				linha.append(1)
			else:
				linha.append(2)
		M.append(linha)

	return M

def dividir(matriz):
	linha, coluna = matriz.shape #retorna o tamanho de linhas e coluna
	linha_metade, coluna_metade = linha//2, coluna//2 #prof. a barra simples dupla, faz uma divisao desconsiderando fracao
	return matriz[:linha_metade, :coluna_metade], matriz[:linha_metade, coluna_metade:], matriz[linha_metade:, :coluna_metade], matriz[linha_metade:, coluna_metade:]

def conquistar_mult(x, y):
	#multiplicando matriz AxB de forma recursiva, dividindo e conquistando
	if len(x) == 1:
		return x * y

	a, b, c, d = dividir(x)
	e, f, g, h = dividir(y)

	p1 = conquistar_mult(a, f - h)
	p2 = conquistar_mult(a + b, h)
	p3 = conquistar_mult(c + d, e)
	p4 = conquistar_mult(d, g - e)
	p5 = conquistar_mult(a + d, e + h)
	p6 = conquistar_mult(b - d, g + h)
	p7 = conquistar_mult(a - c, e + f)
	
	c11 = p5 + p4 - p2 + p6
	c12 = p1 + p2            
	c21 = p3 + p4   
	c22 = p1 + p5 - p3 - p7

	c = np.vstack((np.hstack((c11, c12)), np.hstack((c21,c22))))

	return c

if __name__ == "__main__":

	grade = lambda: round(uniform(0.0, 10.0), 2)
	data = ((i + 1, grade(), grade()) for i in range(10))

	with open("Tmp_Exe.csv", "w") as f:
		w = writer(f)
		w.writerow([" - ", "N", "Divide_Conquer_T_Exec"])
		N = [32, 64, 128, 256, 512, 1024]

		for i in range(len(N)):
			print N[i]

			A = np.array(iniciar_matriz_randomicamente(32))
			B = np.array(iniciar_matriz_randomicamente(32))
			inicio = timeit.default_timer()
			c = conquistar_mult(A,B)
			fim = timeit.default_timer()
			w.writerow([i, N[i], (fim - inicio)])

			if N[i] == 64:
				print("Matriz A")
				print(A)
				print("\n")
				print("Matriz B")
				print(B)
				print("\n")
				print("Matriz C")
				print(c)