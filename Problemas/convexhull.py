class punto:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def convexHull (P):
    for i in range(len(P)):
        for j in range(len(P)):
            ptI = P[i]
            ptJ = P[j]
            if ptI.x != ptJ.x and ptI.y != ptJ.y:
                
                todosLosPuntosEnDerecha = True

                for k in range(len(P)):
                    ptK = P[k]
                    if (ptK.x != ptI.x and ptK.y != ptI.y) and (ptK.x != ptJ.x and ptK.y != ptJ.y):
                        d = queLadoDeLaLinea(ptI, ptJ, ptK )
                        if d < 0:
                            todosLosPuntosEnDerecha = False
                            
                if todosLosPuntosEnDerecha == True:
                    print("segment " + str(i) + " to " + str(j))
                    a = ptI
                    b = ptJ
                    print("De "+str(a.x)+str(a.y)+" a "+str(b.x)+str(b.y))

def queLadoDeLaLinea(lineEndptA, lineEndptB, ptSubject):
    return ((ptSubject.x - lineEndptA.x) * (lineEndptB.y - lineEndptA.y)) - ((ptSubject.y - lineEndptA.y) * (lineEndptB.x - lineEndptA.x))

p1 = punto(2,1)
p2 = punto(2,2)
p3 = punto(3,1)
p4 = punto(0,3)
#p5 = punto(2.5,1)

P = [p1,p2,p3,p4]

convexHull(P)
