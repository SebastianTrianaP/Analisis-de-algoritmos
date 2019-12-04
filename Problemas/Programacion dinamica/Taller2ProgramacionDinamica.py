import math
#---------Algoritmo Evidente---------
def mejorParticion(S):
  return mejorParticion_Aux(S,len(S)-1,sum(S)//2,0)
#end def

def mejorParticion_Aux(S,i,sumaTotal,suma):
  if i==0:
    print("(",sumaTotal," - ", suma,")-",suma)
    return math.fabs(sumaTotal*2-2*suma)
  else:
    print("Entra", i)
    x=mejorParticion_Aux(S,i-1,sumaTotal,suma+S[i-1])
    print("x: ",x)
    y=mejorParticion_Aux(S,i-1, sumaTotal, suma)
    print("y: ",y)
    if x < y:
      return x
    else:
      return y
  #end if
#end def

#---------Algoritmo Memorización---------
def mejorParticionMem(S):
    m = [ [ math.inf for i in range( sum(S)//2 +2)] for j in range(  len(S) + 1) ]
    mejorParticionMem_Aux(S,len(S)-1,sum(S)//2 ,0, m)
    for fila in m:
        print(fila)
#end def

def mejorParticionMem_Aux(S,i,sumaTotal,suma, m):
  if m[i][suma] == math.inf:
    if i==0:
      print("(",sumaTotal*2," - ", suma,")-",suma, i)
      m[i][suma] = math.fabs(sumaTotal*2-2*suma)
    else:
      print("Entra", i)
      x=mejorParticionMem_Aux(S,i-1,sumaTotal,suma+S[i-1], m)
      print("x: ",x)
      y=mejorParticionMem_Aux(S,i-1, sumaTotal, suma, m)
      print("y: ",y)
      if x < y:
        m[i][suma] = x
      else:
        m[i][suma] = y
  return m[i][suma]
  #end if
#end def
#---------Algoritmo Bottom up---------
def mejorParticionBU(S):
  m = [ [ math.inf for i in range( sum(S)//2 +2)] for j in range(  len(S) + 1) ]
  for i in range(len(S) + 1):
    m[i][0] = 0
  for j in range(1, sum(S)//2 +2):
    m[0][j] = 0
  for i in range(len(S) + 1):
    for j in range(1, sum(S)//2 +2):
      print("Entra", i)
      m[i][j]=m[i-1][j]
      if S[i-1] <= j:
        m[i][j]= m[i-1][j - S[i-1]]

  return m[i][j]
  #end if
#end def
#---------PRUEBAS---------
S = [ 4, 5, 7, 10, 300 ]
print(mejorParticion(S))
#print("---------------------------------")
#print(mejorParticionMem(S))
#print(mejorParticionBU(S))
