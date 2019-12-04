import sys
#Problema del maximo subarreglo

a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

#Funcion encontrar subarreglo en el cruce
def findMaxCrossSubArray(a,low,m,high):
    leftSum = -999999999
    suma = 0
    maxLeft = 0
    for i in range(m,low-1,-1):
        suma = suma + a[i]
        if suma > leftSum:
            leftSum = suma
            maxLeft = i
    rightSum = -999999999
    suma = 0
    maxRight = 0
    for j in range(m+1,high):
        suma = suma + a[j]
        if suma > rightSum:
            rightSum = suma
            maxRight = j
    res = [maxLeft, maxRight,leftSum+rightSum]
    return res

#Funcion encontarr maximo subarreglo
def findMaxSubArray(a,low,high):
    if high == low:
        return (low,high,a[low])
    else:
        m = (low+high)//2
        print(m)
        left = findMaxSubArray(a,low,m)
        right = findMaxSubArray(a,m+1,high)
        cross = findMaxCrossSubArray(a,low,m,high)
        if left[2] >= right[2] and left[2] >= cross[2]:
            return (left[0], left[1], left[2])
        elif right[2] >= left[2] and right[2] >= cross[2]:
            return (right[0], right[1], right[2])
        else:
            return (cross[0], cross[1], cross[2])

#Ejecucion funciones
sys.setrecursionlimit(1500)
print(findMaxSubArray(a,0,15))


