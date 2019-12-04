import sys
import random
#----------------------------------------------
#Funcion encontrar elemento en la kesima estadistica
def median_of_medians(S, i):
    sublistas = []
    for j in range(0, len(S), 5):
        sublistas.append(S[j:j+5])
    
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublistas]
    print(sublistas)
    print(medians)
    
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)//2]
    else:
        #the pivot is the median of the medians
        pivot = Select(medians,0, len(medians)-1, int(len(medians)/2))
    #partitioning step

    print(pivot)
    low = [j for j in S if j < pivot]
    high = [j for j in S if j > pivot]

    print(low)
    print(high)
    k = len(low)
    print(k)
    if i < k:
        print("Entra menor")
        return median_of_medians(low,i)
    elif i > k:
        print("Entra mayor")
        print(i-k-1)
        return median_of_medians(high,i-k-1)
    else: #pivot = k
        return pivot
    

#Funcion encontrar mediana de un arreglo
def Select(S, inicio, fin, k):
    if inicio >= fin:
        return S[inicio]
    else:
        q = Partition_Aleatoria(S, inicio, fin)
        if k == q:
            return S[ k ]
        elif k < q:
            return Select(S, inicio, q-1, k)
        else:
            return Select(S, q+1, fin, k)

#Funcion privote aleatorio ademas cada cambio en el
#arreglo de las medianas lo replica el arreglo de subconjuntos
def Partition_Aleatoria(S, inicio, fin):
    i = random.randint(inicio, fin)
    #S[fin], S[i] = S[i], S[fin]
    aux=S[fin]
    S[fin]=S[i]
    S[i]=aux
    return Partion(S, inicio, fin)
#Funcion de particion toma el último elemento como pivote,
#coloca el elemento pivote en su posición correcta en el
#arreglo ordenado y coloca todos los elementos más pequeños
#(más pequeños que el pivote)a la izquierda del pivote y todos
#los elementos mayores a la derecha del pivote
def Partion(S, inicio, fin):
    x = S[ fin ]
    i = inicio-1
    for j in range(inicio, fin):
        if S[j] <= x:
            i = i+1
            S[i], S[j] = S[j], S[i]
    S[i+1], S[fin] = S[fin], S[i+1]
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


#Here are some example lists you can use to see how the algorithm works
A = [1,2,3,4,5,1000,8,9,99]
#B = [1,2,3,4,5,6]
print (median_of_medians(A, 7)) #should be 1
#print median_of_medians(A,7) #should be 99
#print (median_of_medians(B,4)) #should be 5
