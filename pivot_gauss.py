import numpy as np

# saisir la matrice augmentée
A = np.array([  [5,1,5,1],
                [3,-1,2,1],
                [2,5,-2,-1]],
                dtype=float)

def swap_lines(A,i,j):
    l,c = A.shape
    # for k in range(c):
    #     A[i,k], A[j,k] = A[j,k], A[i,k]
    A[i,:],A[j,:] = A[j,:] , A[i,:]

def G(A):
    L,C = A.shape
    i,j = 0,0
    while i<(L-1) and j<(C-1) :
        if A[i:,j].any() : # au moins un elt non nul dans col j
            k=i
            while A[k,j]==0 : k+=1
            if k!=i : swap_lines(A,i,k)
            for k in range(i+1,L):
                A[k,:] = A[k,:]-A[k,j]/A[i,j]*A[i,:]
            #print(A) # decommenter pour avoir les etapes
            i += 1
        j += 1
    return A

def GJ(A):
    L,C = A.shape
    i,j = 0,0
    while i<(L-1) and j<(C-1) :
        if A[i:,j].any() : # au moins un elt non nul dans col j
            k=i
            while A[k,j]==0 : k+=1
            if k!=i : swap_lines(A,i,k)
            A[i,:] = 1/A[i,j]*A[i,:]
            for k in range(0,L):
                if k!=i :
                    A[k,:] = A[k,:]-A[k,j]/A[i,j]*A[i,:]
            #print(A)
            i += 1
        j += 1
    return A

print(G(A))
print(GJ(A))



