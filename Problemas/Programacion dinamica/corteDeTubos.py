import math
#-----------------------------Algoritmo evidente-----------------------------
#Algoritmo recursivo pero repite subproblemas
def Cut_Rod_Evidente(P, n):
    if n == 0:
        return 0
    else:
        q = - math.inf
        for k in range(0, n):
            print("k : ", k, n)
            v = P[k] + Cut_Rod_Evidente(P, n-k-1)
            print("v: ",v,n)
            if q < v:
                q = v
        print("return: ", q)
        return q


#-----------------------------Algoritmo memorizacion-----------------------------
#Algoritmo recursivo pero guarda los elementos que calcula en un arreglo evitando volverlos a calcular
def Cut_Rod_Memorizacion(P, n):
    r = [- math.inf for i in range(0, n+1)]
    print(r)
    return Cut_Rod_Memorizacion_Aux(P,n,r)

def Cut_Rod_Memorizacion_Aux(P, n, r):
    if r[n] < 0:
        if n == 0:
            r[n] = 0
        else:
            q = - math.inf
            for k in range(0, n):
                v = P[k] + Cut_Rod_Memorizacion_Aux(P, n-k-1, r)
                if q < v:
                    q = v
            r[n] = q
    return r[n]

#-----------------------------Algoritmo bottom up-----------------------------
#Vuelve el algoritmo anterior iterativo, inicializa casos base y empieza a construir desde ahi
def Cut_Rod_Bottom_up(P, n):
    r = [0 for i in range(0, n+1)]
    r[0] = 0
    for j in range(1, n+1):
        r[j] = - math.inf
        for k in range(1, j+1):
            v = P[k-1] + r[j-k]
            if r[j] < v:
                r[j] = v
    return r[n]

#-----------------------------Algoritmo backtracking-----------------------------
#Guarda en otro arreglo s los cortes realizados y a partir del ultimo corte se devuelve construyendo los cortes que realizo
def Cut_Rod(P, n):
    r = [0 for i in range(0, n+1)]
    s = [0 for i in range(0, n+1)]
    r[0] = 0
    for j in range(1, n+1):
        r[j] = - math.inf
        for k in range(1, j+1):
            v = P[k-1] + r[j-k]
            if r[j] < v:
                r[j] = v
                s[j] = k
    m = n
    print(r)
    print(s)
    AllCuts =[]
    while m > 0:
        AllCuts. append(s[m])
        m = m - s[m]
    return [r[n], AllCuts]

#-----------------------------Pruebas-----------------------------
P = [1, 5, 8, 9]
#print(Cut_Rod_Evidente(P, len(P)))
#print(Cut_Rod_Memorizacion(P, len(P)))
#print(Cut_Rod_Bottom_up(P, len(P)))
print(Cut_Rod(P, len(P)))
