# Paulina Ugalde Carreño

#importamos la libreria math para poder hacer uso de la funcion raiz cuadrada
from math import sqrt 

#-------------------------------------------------METODOS A USAR-------------------------------------

def gramSchmidt(matriz1, base_ortogonal, base_ortonormal, filas, columnas):
    # nuestra matriz va a ser igual a base_ortogonal para que podamos trabajar con ella
    for i in range(columnas):
        for j in range(filas):
            base_ortogonal[j][i] = matriz1[j][i]
    
    for i in range(columnas):
        #recordemos que q0 = v0
        if i != 0: 
           productoPunto(matriz1, base_ortogonal, i, filas)

    for i in range(columnas):
        ortonormalizacion(base_ortogonal, base_ortonormal, i, filas)
               
def productoPunto(matriz1, base_ortogonal, i, filas):
    cont=i  
    while(cont>0):
        prod_punt = div = division = escxvect = 0
        for j in range(filas):  
            prod_punt += matriz1[j][i]*base_ortogonal[j][cont-1]
            div += base_ortogonal[j][cont-1]*base_ortogonal[j][cont-1]
        division = float(prod_punt/div)

        for j in range(filas):
            escxvect = division * base_ortogonal[j][cont-1]
            base_ortogonal[j][i] = base_ortogonal[j][i] - escxvect
        cont=cont-1

def ortonormalizacion(base_ortogonal, base_ortonormal, i, filas):
    magnitud = 0
    for j in range(filas):
        magnitud += base_ortogonal[j][i]*base_ortogonal[j][i]
    raiz = sqrt(magnitud)
    
    for j in range(filas):
        base_ortonormal[j][i] = base_ortogonal[j][i]/raiz