#input
K=int(input())
M=int(input())
T=int(input())
C=float(input())

N=T*M*K
#input of distance matrix
matrix =[]
for i in range(N):
    matrix.append(list(map(float, input().split())))
arr = [[[0 for k in range(K)] for m in range(M)] for t in range(T)]



#functions..............................................................
#similarity value between two markets
def similarityOfMarket(matrix,market):
    ans=0
    for i in market:
        for j in market:
            if(i==j):
                continue
            ans+=1-matrix[i][j]
    return ans/2
#similarity value of whole state
def similarityOfWhole(matrix,whole):
    ans=0
    for timeslot in whole:
        for market in timeslot:
            ans+=similarityOfMarket(matrix,market)
    return ans

#distance value between two markets
def distanceInTwoMarkets(matrix,market1,market2):
    ans=0
    for m1 in market1:
        for m2 in market2:
            ans+=matrix[m1][m2]
    return ans
#distance value of whole state
def distanceOfWhole(matrix,whole):
    ans=0
    for timeslot in whole:
        for m1 in timeslot:
            for m2 in timeslot:
                if(m1==m2):
                    continue
                ans+=distanceInTwoMarkets(matrix,m1,m2)
    return ans/2

#goodness value of a state
def goodness(matrix,whole):
    return similarityOfWhole(matrix,whole)+C*(distanceOfWhole(matrix,whole))

#swapping two values in matrix
def swap(arr,t1,m1,k1,t2,m2,k2):
    temp=arr[t1][m1][k1]
    arr[t1][m1][k1]=arr[t2][m2][k2]
    arr[t2][m2][k2]=temp
    return arr

#optimizing the state until convergence
def optimize(matrix,arr):
    initialGoodness=goodness(matrix,arr)
    for t in range(T):
        for m in range(M):
            for k in range(K):
                for t1 in range(T):
                    for m1 in range(M):
                        for k1 in range(K):
                            
                            g=goodness(matrix,arr)
                            swap(arr,t,m,k,t1,m1,k1)
                            if(goodness(matrix,arr)<=g):
                                swap(arr,t,m,k,t1,m1,k1)

    if(initialGoodness==goodness(matrix,arr)):
        increment(arr)
        printOutput(arr)
        return
    optimize(matrix,arr)

#making suitable for ouput by adding one to each value
def increment(arr):
    for t in range(T):
        for m in range(M):
            for k in range(K):
                arr[t][m][k]=arr[t][m][k]+1

#printing in output format  
def printOutput(arr):
    for m in range(M):
        s=""
        for t in range(T):
           s+=" ".join(map(str,arr[t][m])) 
           if(t!=T-1):
                s+=" | "
        print(s)
    
#functions end............................................................

#initialising parent state of 3d array
i=0
for t in range(T):
    for m in range(M):
        for k in range(K):
            arr[t][m][k]=i
            i+=1

#optimization of first state and its printing
optimize(matrix,arr)


