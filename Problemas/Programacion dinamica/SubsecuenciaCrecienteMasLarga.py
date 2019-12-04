import math
#-----------Evidente-------------
def LIS(S):
    return LIS_Aux(S,len(S))

def LIS_Aux(S, i):
    if i == 0:
        print("llego a 0")
        return 0;
    else:
        a = LIS_Aux(S,i-1)
        print("a", a)
        j=i-1

        while j>0 and (not S[j-1]<S[i-1]):
            j=j-1
        #end while

        b=LIS_Aux(S,j)+1
        print("b", b)
        if a<b:
            return b
        else:
            return a
        #end if
    #end if
#end procedure

#-----------Memorizacion-------------
def LISMem(S):
    M =[-math.inf for i in range (len(S)+1)]
    return LISMem_Aux(S,len(S),M)

def LISMem_Aux(S, i, M):
    if M[i] == -math.inf:
        if i == 0:
            print("llego a 0")
            M[i] = 0;
        else:
            a = LISMem_Aux(S,i-1,M)
            print("a", a)
            j=i-1

            while j>0 and (not S[j-1]<S[i-1]):
                j=j-1
            #end while

            b=LISMem_Aux(S,j,M)+1
            print("b", b)
            if a<b:
                M[i]= b
            else:
                M[i]= a
            #end if
        #end if
    #end if
    return M[i]
#end procedure

#-----------Bottom up-------------
def LISBU(S):
    M =[0 for i in range (len(S)+1)]
    for i in range (1,len(M)):
        a = M[i-1]
        j=i-1
        while j>0 and (not S[j-1]<S[i-1]):
            j=j-1
        #end while
        b=M[j]+1
        if a<b:
            M[i]= b
        else:
            M[i]= a
            #end if
    #end for
    return M[len(S)]
#end procedure

#-----------Backtraking-------------
def LISB(S):
    M =[0 for i in range (len(S)+1)]
    for i in range (1,len(M)):
        a = M[i-1]
        j=i-1
        while j>0 and (not S[j-1]<S[i-1]):
            j=j-1
        #end while
        b=M[j]+1
        if a<b:
            M[i]= b
        else:
            M[i]= a
            #end if
    #end for

    L=[]
    for i in range(1, len(M)-1):
        if M[i-1] != M[i]:
            L.append(S[i-1])
    return [M[len(S)], L]
#end procedure


#------------Pruebas-------------

S=[9,2,8,6,3,6,9,7]
#print(LIS(S))
print(LISMem(S))
#print(LISBU(S))
#print(LISB(S))
