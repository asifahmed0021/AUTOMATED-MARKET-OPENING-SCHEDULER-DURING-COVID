#imports
import copy
from random import randrange
import random
#taking parameters input
K=int(input())
M=int(input())
T=int(input())
C=float(input())

N=T*M*K
#taking distance matrix input
matrix =[]
for i in range(N):
    matrix.append(list(map(float, input().split())))

#defining population size
populationSize=100

#genrates a member state for population
def generateRandomState():
    list=[]
    for _ in range(N):
        list.append(_)
    ran = [[[0 for k in range(K)] for m in range(M)] for t in range(T)]
    for t in range(T):
        for m in range(M):
            for k in range(K):
                index=randrange(0,len(list))
                num=list[index]
                list.remove(num)
                ran[t][m][k]=num
    return ran

#generates population of size of populationSize
def generateFirstPopulation():
    population=[]
    for i in range(populationSize):
        population.append(generateRandomState())
    return population


#similarity value of a particular market
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

#calculating goodness of particular state
def goodness(matrix,whole):
    return similarityOfWhole(matrix,whole)+C*(distanceOfWhole(matrix,whole))



#sort population in decreasing order according to goodness value
def sortByGoodness(population):
    population.sort(reverse = True, key = lambda x:goodness(matrix,x))


#function to make next generation from parent generation
def makeNextGeneration(parent):
    nextGen=[[]for i in range(populationSize)]
    #first best 10% from parent as it is
    for i in range(int(populationSize/10)):
        nextGen[i]=parent[i]
        
    #for rest 90% population
    for j in range(int(populationSize/10),populationSize):     
        #choosing two parents from first half of parent population list
        firstparent=random.choice(parent[:int(len(parent)/2)])
        secondparent=random.choice(parent[:int(len(parent)/2)])
        #random point for diversion 
        diversion=random.randint(1,T)
        #merging for a new child
        for t in range(diversion):
            nextGen[j].append(copy.deepcopy(firstparent[t]))
        for t in range(diversion,T):
            nextGen[j].append(copy.deepcopy(secondparent[t]))
        
        
        #keeping track of repeated elements
        repeatedtrack=[0]*N
        for t in range(T):
            for m in range(M):
                for k in range(K):
                    repeatedtrack[nextGen[j][t][m][k]]+=1
        didnotcome=[]
        #keeping track of elements which did not come
        for _ in range(N):
            if repeatedtrack[_]==0:
                didnotcome.append(_)
        random.shuffle(didnotcome)
        #removing one from repeated ones and adding the ones which did not come
        q=0
        for t in range(T):
            for m in range(M):
                for k in range(K):
                    if repeatedtrack[nextGen[j][t][m][k]]==2:
                        repeatedtrack[nextGen[j][t][m][k]]-=1
                        nextGen[j][t][m][k]=didnotcome[q]
                        q+=1
    return nextGen

#bringing random changes in the population for some mutation
def change(population):
    for _ in range(50):
        index=random.randint(10,populationSize-1)
        t1=random.randint(0,T-1)
        t2=random.randint(0,T-1)
        m1=random.randint(0,M-1)
        m2=random.randint(0,M-1)
        k1=random.randint(0,K-1)
        k2=random.randint(0,K-1)
        temp=population[index][t1][m1][k1]
        population[index][t1][m1][k1]=population[index][t2][m2][k2]
        population[index][t2][m2][k2]=temp

#main function to optimize the initial population distribution
def optimize(population):
    sortByGoodness(population)
    ansgoodness=goodness(matrix,population[0])
    ans=population[0]
    i=0
    while i<200:
        i+=1
        childPopulation=makeNextGeneration(population)
        sortByGoodness(childPopulation)
        change(childPopulation)
        temp=goodness(matrix,childPopulation[0])
        if(temp>ansgoodness):
            ansgoodness=temp
            ans=childPopulation[0]
        population=childPopulation
    return ans
            
        
#incrementing every value to change from index notation to output preffered one
def increment(arr):
    for t in range(T):
        for m in range(M):
            for k in range(K):
                arr[t][m][k]=arr[t][m][k]+1
#printing the final answer distribution in output format
def printOutput(arr):
    for m in range(M):
        s=""
        for t in range(T):
           s+=" ".join(map(str,arr[t][m])) 
           if(t!=T-1):
                s+=" | "
        print(s)

#initial population distribution
population=generateFirstPopulation()
#final answer state
ans=optimize(population)
#changing to output format and printing
increment(ans)
printOutput(ans)
