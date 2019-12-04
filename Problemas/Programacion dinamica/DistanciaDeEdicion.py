import math
#---------------Evidente-----------------
def EditDistance (X,Y):
    return EditDistance_Aux(X,Y,len(X),len(Y))

def EditDistance_Aux(X,Y,i,j):
    if i==0 or j==0:
        print(i,j)
        return max(i,j)
    else:
        if X[i-1]==Y[j-1]:
            return EditDistance_Aux(X,Y,i-1,j-1)
        else:
            a = EditDistance_Aux(X,Y,i-1,j)
            print("a",a)
            b = EditDistance_Aux(X,Y,i,j-1)
            print("b",b)
            c = EditDistance_Aux(X,Y,i-1,j-1)
            print("c",c)
            return 1 + min([a,b,c])

#---------------Memorizacion-----------------
def EditDistanceMem (X,Y):
    E = [[math.inf for i in range(len(X)+1)] for j in range(len(Y) + 1)]
    return EditDistanceMem_Aux(X,Y,len(X),len(Y), E)

def EditDistanceMem_Aux(X,Y,i,j,E):
    if E[i][j] == math.inf:
        if i==0 or j==0:
            print(i,j)
            E[i][j] = max(i,j)
        else:
            if X[i-1]==Y[j-1]:
                E[i][j] = EditDistanceMem_Aux(X,Y,i-1,j-1,E)
            else:
                a = EditDistanceMem_Aux(X,Y,i-1,j,E)
                print("a",a)
                b = EditDistanceMem_Aux(X,Y,i,j-1,E)
                print("b",b)
                c = EditDistanceMem_Aux(X,Y,i-1,j-1,E)
                print("c",c)
                E[i][j] = 1 + min(a,b,c)
            #End if
        #End if
    #End if
    return E[i][j]
#End procedure

#---------------Button-up-----------------
def EditDistanceBU(X,Y):
    E = [[math.inf for i in range(len(X)+1)] for j in range(len(Y) + 1)]
    for i in range(len(Y)+1):
        E[i][0] = i
    for j in range(len(X)+1):
        E[0][j] = j

    for i in range( 1,len(X)+1):
        for j in range(1, len(Y)+1):
            if X[i-1]==Y[j-1]:
                E[i][j] = E[i-1][j-1]
            else:
                a = E[i-1][j]
                b = E[i][j-1]
                c = E[i-1][j-1]
                E[i][j] = 1 + min(a,b,c)
            #End if
        #End for
    #End for
    return E[len(X)][len(Y)]
#End procedure

#---------------backtracking-----------------
def EditDistanceB(X,Y):
    E = [[math.inf for i in range(len(X)+1)] for j in range(len(Y) + 1)]
    for i in range(len(Y)+1):
        E[i][0] = i
    for j in range(len(X)+1):
        E[0][j] = j

    for i in range( 1,len(X)+1):
        for j in range(1, len(Y)+1):
            if X[i-1]==Y[j-1]:
                E[i][j] = E[i-1][j-1]
            else:
                a = E[i-1][j]
                b = E[i][j-1]
                c = E[i-1][j-1]
                E[i][j] = 1 + min(a,b,c)
            #End if
        #End for
    #End for
    return E[len(X)][len(Y)]
#End procedure

#---------------pruebas-----------------
X="tigre"
Y="trigo"
#print(EditDistance (X,Y))
#print(EditDistanceMem (X,Y))
#print(EditDistanceBU (X,Y))
