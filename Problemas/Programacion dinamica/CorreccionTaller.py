import math, random
#=============Algoritmo evidente=============
def MinPartition(E):
    return MinPartition_Aux(E, len( E ), 0, sum( E ))

def MinPartition_Aux(E, i, c, D ):
    if i == 0:
        return abs( D - ( 2 * c ) )
    else:
        a = MinPartition_Aux( E, i - 1, c, D)
        b = MinPartition_Aux( E, i - 1, c + E[ i - 1 ], D)
        if a < b:
            return a
        else:
            return b

#=============Algoritmo memorizado=============
def MinPartitionMem(E):
    D = sum(E)
    M = [[math.inf for i in range( D + 1 )] for j in range( len(E) + 1 )]
    return MinPartitionMem_Aux(E, len( E ), 0, D, M)

def MinPartitionMem_Aux(E, i, c, D, M ):
    if M[i][c] == math.inf:
        if i == 0:
            M[i][c] = abs( D - ( 2 * c ) )
        else:
            a = MinPartitionMem_Aux( E, i - 1, c, D, M)
            b = MinPartitionMem_Aux( E, i - 1, c + E[ i - 1 ], D, M)
            if a < b:
                M[i][c] = a
            else:
                M[i][c] = b
    return M[i][c]

#=============Algoritmo Bottom Up=============
def MinPartitionBU(E):
    D = sum(E)
    M = [[math.inf for i in range( D + 1 )] for j in range( len(E) + 1 )]
    for c in range(D+1):
        M[0][c] = abs( D - ( 2 * c ) )

    for i in range (1, len(E) + 1):
        for c in range (D, -1, -1):  #Empieza en d por que al generar la matriz esta se hace hasta D y hasta len(E)+1
            a = math.inf
            if c + E[ i - 1] < D+1:
                a = M[i - 1][ c + E[ i - 1 ]]
            b = M[i - 1][c]
            if a < b:
                M[i][c] = a
            else:
                M[i][c] = b
    return M[len(E)][0]
#=============Algoritmo Backtracking=============
def MinPartitionB(E):
    D = sum(E)
    M = [[math.inf for i in range( D + 1 )] for j in range( len(E) + 1 )]
    B = [["B" for i in range( D + 1 )] for j in range( len(E) + 1 )]
    for c in range(D+1):
        M[0][c] = abs( D - ( 2 * c ) )

    for i in range (1, len(E) + 1):
        for c in range (D, -1, -1):
            a = math.inf
            if c + E[ i - 1] < D+1:
                a = M[i - 1][ c + E[ i - 1 ]]
            b = M[i - 1][c]
            if a < b:
                M[i][c] = a
                B[i][c]="A"
            else:
                M[i][c] = b

    A=[]
    C=[]
    i=len(E)
    c=0

    while i>0:
        if B[i][c] == "A":
            A.append( E[ i -1 ])
            c = c + E[ i -1 ]
        else:
            C.append( E[ i -1 ])
        i =i-1
    return [M[len(E)][0], A, C]


#=============Pruebas=============
#E = [ 1,2,3,4,5,6,34,567,65,2235 ]
E = [ 4, 5, 7, 10, 300 ]
random.shuffle( E )

print( E )
#print( MinPartition(E) )
#print( MinPartitionMem(E) )
#print( MinPartitionBU(E) )
print( MinPartitionB(E) )
