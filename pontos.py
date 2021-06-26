#coding: utf-8
import math
def d(x1,y1,x2,y2):
	d = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
	return d

if __name__ == "__main__":
	print("Entre com X1")
	x1 = eval(input())
	print("Entre com Y1")
	y1 = eval(input())
	print("Entre com X2")
	x2 = eval(input())
	print("Entre com Y2")
	y2 = eval(input())

	if d(x1,x2,y1,y2) >= 10:
		print("longe")
	else:
		print("perto")