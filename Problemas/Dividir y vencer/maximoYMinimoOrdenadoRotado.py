# Funcion maximo y minimo 
def findMaxMin(S, low, high):
        if high < low:
                return [S[0], S[0]]
        elif (high == low):
                return [S[low], S[low]]
        else:
                mid = low + (high - low) // 2
                # Check if mid itself is maximum element 
                if (mid < high and S[mid] > S[mid + 1]):
                        return [S[mid], S[mid + 1]]
                
                # Check if element at (mid - 1) is maximum element 
                # Consider the cases like {4, 5, 1, 2, 3} 
                if (mid > low and S[mid - 1] > S[mid]):
                        return [S[mid - 1],  S[mid]]

                # Decide whether we need to go to 
                # the left half or the right half 
                if (S[low] > S[mid]):
                        return findMaxMin(S, low, mid - 1) 
                else:
                        return findMaxMin(S, mid + 1, high) 

# Driver code 
S =(67, 89, 90, 23, 25, 34, 50, 60)
print(findMaxMin(S, 0, len(S) - 1)) 

# This code is contributed by mohit kumar 

