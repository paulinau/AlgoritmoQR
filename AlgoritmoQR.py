# Algoritmo QR para una matriz cuadrada

from GramSchmith import *

#Declaramos nuestras matrices vacias
matriz = []    
base_ortogonal = []
base_ortonormal = []
matriz_transpuesta = []
r = []
a0 = []
a1 = []
R = []

print ("Matriz mxm")
filas = int(input("Ingresa el valor de m: "))
#igualamos el numero de columnas con el numero de filas al ser una matrix mxm
columnas = filas

for i in range(filas):
    matriz.append([0]*columnas)
    base_ortogonal.append([0]*columnas)
    base_ortonormal.append([0]*columnas)
    matriz_transpuesta.append([0]*columnas)
    r.append([0]*columnas)
    a0.append([0]*columnas)
    a1.append([0]*columnas)
    R.append([0]*columnas)

# Pediremos los valores de la matriz por te clado
for j in range(columnas):
    for i in range(filas):
        matriz[i][j] = float(input("Ingresa la componente del vector "+str(j)+" posicion "+str(i)+": "))

#imprimir la matriz
def imprimirMatriz(matriz, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            #imprime el numero redondeado por 5 cifras
            print("[",round(matriz[i][j], 5), end=" ]") 
        print()

# Mandamos a llamar a la funcion para imprimir nuestra matriz
imprimirMatriz(matriz, filas, columnas)


#-------------metodos para FACTORIZACION QR
def matrizTranspuesta(matriz_transpuesta, base_ortonormal):
    for i in range(filas):
        for j in range(columnas):
            matriz_transpuesta[i][j] = base_ortonormal[j][i]
 
def multiplicacionMatrices(matriz1, matriz2, matriz3):
    for i in range(filas):
        for j in range(columnas):
            for k in range(filas):
                matriz3[i][j] += matriz1[i][k]*matriz2[k][j]

def comprobacionTriangularSuperior(matriz, filas):
    cont=0
    respuesta=True
    i=1
    while(i<filas):
        cont=cont+1
        for j in range(cont):
            if(matriz[i][j]>0.0000000001 or matriz[i][j]<-0.0000000001):
                respuesta=False
                break
        i=i+1
    return respuesta
                

def algoritmoQR(matriz,base_ortogonal,base_ortonormal,matriz_transpuesta):
    #definir variables
    triangular=False
    contador = 0

    #paso 1: A0=A
    for j in range(columnas):
        for i in range(filas):
            a0[i][j] =matriz[i][j]

    #paso 2: Repetir hasta que A1 sea matriz triangular superior
    #c)
    while(triangular==False):
        #a)
        #sacar la base_ortonormal de a0
        gramSchmidt(a0, base_ortogonal, base_ortonormal, filas, columnas)

        #sacamos R de a0
        #primero sacar la transpuesta de base_ortonormal -> matriz_transpuesta
        matrizTranspuesta(matriz_transpuesta, base_ortonormal)
        #multiplicar R=(matriz_transpuesta)(A)
        multiplicacionMatrices(matriz_transpuesta, a0, R)

        print("\nIteracion: "+str(contador),end="")
        #mostrar la factorización a0=base_ortonormal*R para cada iteracion
        print("\n A"+str(contador)+" = Q"+str(contador)+"*R"+str(contador))
        for i in range(filas):
            for j in range(columnas):
                print("[", round(a0[i][j], 5), end=" ]")
            print("\t", end = '') 
            if(i==0):
                print(" = ",end='')
            else:
                print(" \t  ",end='')
            for j in range(columnas):
                print("[", round(base_ortonormal[i][j], 5), end=" ]")
            print("\t", end = '') 
            if(i==0): #solo imprime una vez el * 
                print(" *\t ",end='')
            else:
                print("\t",end='')
            for j in range(columnas):
                print("[",round(R[i][j], 5), end=" ]")
            print()

        #b)
        #sacar A1 = (R)(Q)
        multiplicacionMatrices(R, base_ortonormal, a1)

        #comprobamos si la a1 ya es diagonal superior
        if(comprobacionTriangularSuperior(a1,filas)):
            triangular=True #si es así, salimos de las iteraciones
        else:#si no lo es, repetimos el proceso, ahora A1 es la nueva A0
            contador = contador + 1
            for j in range(filas):
                for i in range(columnas):
                    a0[i][j] = a1[i][j]
                    #limpiamos la matriz resultado y la Ai_mas_1
                    R[i][j]=0
                    a1[i][j]=0

    print("Iteraciones totales: "+str(contador))
    #los eigenvalores son los elementos de la diagonal
    for i in range(filas):
        print(str(a1[i][i]), ", ")
    


#imprimimos los valores y mandamos a llamar a las funciones

# Imprimir matriz original
print("Matriz Original (A): ")
imprimirMatriz(matriz,filas, columnas)

print ("\n Base ortogonal con GramSchmidt: ")
gramSchmidt(matriz, base_ortogonal, base_ortonormal, filas, columnas)
imprimirMatriz(base_ortogonal,filas,columnas)

print("\n Base ortonormal: ")
imprimirMatriz(base_ortonormal, filas,columnas)

print("\n eigenvalores: ")
algoritmoQR(matriz,base_ortogonal,base_ortonormal,matriz_transpuesta)