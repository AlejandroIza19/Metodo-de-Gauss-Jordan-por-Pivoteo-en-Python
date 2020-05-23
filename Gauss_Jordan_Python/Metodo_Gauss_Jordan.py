import numpy

int(raw_input('Valor de m:'))

int(raw_input('Valor de n:'))

matriz = numpy.zeros((m,n))

vector = numpy.zeros((n))

x=numpy.zeros((m))

print 'Introduce la matriz de coeficientes y el vector solución'

for r in range(0,m):
	for c in range(0,n):
		matriz[(r),(c)]=(raw_input("Elemento a["+str(r+1)+","+str(c+1)+"] "))
	vector[(r)]=(raw_input('b['+str(r+1)+']: '))
print(matriz)

//pivote
for k in range (0,m);
	for r in range(k+1,m):
		factor=(matriz[r,k]/matriz[k,k])
		vector[r]=vector[r]-(factor*vector[k])
		for c in range(0,n):
			matriz[r,c]=matriz[r,c]-(factor*matriz[k,c])
//ceros abajo de la diagonal principar

#sustitución hacia atrás

x[m-1]=vector[m-1]/matriz[m-1,m-1]
print x[m-1]

for r in range(m-2,-1,-1):
	suma=0
	for c in range(0,n):
		suma=suma+matriz[r,c]*x[c]
	x[r]=(vector[r]-suma)/matriz[r,r]

print 'Resultado matriz'
print(matriz)
print 'Resultado del vector'
print(vector)
print 'Resultados: '
print(x)