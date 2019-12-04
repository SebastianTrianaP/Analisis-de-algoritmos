import sys
import random
#Problema mediana de medianas

#Funcion encontrar la mediana de medianas de un arreglo dejando la estructura
#como la especificada en la presentación
def MediansofMedians(S, inicio, fin):
    #Si el arreglo esta vacio o tiene un solo elemento
    if inicio >= fin:
        return [S, -1]
    #Si no, guarda en el arreglo separados los subconjuntos formados
    #dependiendo de la cantidad de elementos en el arreglo, guarda
    #grupos de 5 elementos, con la posible excepción del último
    else:
        nelement = len(S)//5
        separados = []
        lista = []
        j = 0
        for i in range (0, len(S)):
            lista.append(S[i])
            j = j+1
            if j == nelement:
                separados.append(lista)
                lista = []
                j=0
            if i == len(S)-1 and j > 0:
                separados.append(lista)
                lista = []
                
        medianas = []
        #Ordeno los subconjuntos y al mismo tiempo voy almacenando
        #en otro arreglo las medianas de cada subconjunto
        for i in range (0,len(separados)):
            insertionSort(separados[i])
            medianas.append(separados[i][len(separados[i])//2])

        #Llamada a la función select
        x = Select(medianas, separados, 0, len(medianas)-1, len(medianas)//2)
        return [separados, x]


#Funcion encontrar mediana de un arreglo
def Select(S, separados, inicio, fin, k):
    if inicio >= fin:
        return [S, -1]
    else:
        q = Partition_Aleatoria(S, separados, inicio, fin)
        if k == q:
            return S[ k ]
        elif k < q:
            return Select(S, separados, inicio, q-1, k)
        else:
            return Select(S, separados, q+1, fin, k)

#Funcion privote aleatorio ademas cada cambio en el
#arreglo de las medianas lo replica el arreglo de subconjuntos
def Partition_Aleatoria(S, separados, inicio, fin):
    i = random.randint(inicio, fin)
    S[fin], S[i] = S[i], S[fin]
    separados[fin], separados[i] = separados[i], separados[fin]
    return Partion(S, separados, inicio, fin)
#Funcion de particion toma el último elemento como pivote,
#coloca el elemento pivote en su posición correcta en el
#arreglo ordenado y coloca todos los elementos más pequeños
#(más pequeños que el pivote)a la izquierda del pivote y todos
#los elementos mayores a la derecha del pivote
def Partion(S, separados, inicio, fin):
    x = S[ fin ]
    i = inicio-1
    for j in range(inicio, fin):
        if S[j] <= x:
            i = i+1
            S[i], S[j] = S[j], S[i]
            separados[i], separados[j] = separados[j], separados[i]
    S[i+1], S[fin] = S[fin], S[i+1]
    separados[i+1], separados[fin] = separados[fin], separados[i+1]
    
    return i+1

# Funcion para ordenar insertion sort
def insertionSort(S): 
    for i in range(1, len(S)): 
        key = S[i] 
        j = i-1
        while j >= 0 and key < S[j] : 
                S[j + 1] = S[j] 
                j -= 1
        S[j + 1] = key 

#Ejecucion funciones
sys.setrecursionlimit(1500)
S = [95,58,42,1,5,65,47,23,16,93,105,14,258,14,32,97,26,36,61,30,68,34,99,41,3,6,7,90,0]
print(MediansofMedians(S, 0, len(S)-1))

