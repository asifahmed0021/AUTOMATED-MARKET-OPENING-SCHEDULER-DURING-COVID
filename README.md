# AUTOMATED MARKET OPENING SCHEDULER DURING COVID

## GOAL

#### A city has n types of shops. The government wants to create an opening schedule for the markets ensuring the safety of maximum people. Due to the current COVID situation the government wants the people to make minimum movement out of their houses. 
#### The city has m market places which can be opened parallely. In a market place during each time slot the government is planning to open k types of shops. And in a day there are a total of T time slots available. We can assume that n = T.m.k. 

#### For example, in figure below m = 2, T = 3 and k = 4

| Slot:1           | Slot:2           | Slot:3           | 
| ---------------- | ---------------- | ---------------- |
| Type:1,2,3,4     | Type:5,6,7,8     | Type:9,10,11,12  |
| Type:13,14,15,16 | Type:17,18,19,20 | Type:21,22,23,24 | 



## Optimization of Market Opening Schedule

We first define the characteristics of a good schedule. For any good schedule people should make minimum movement and most of the people should feel no conflict about which market they should go for purchasing.
That is:
1) All types of shops opening in one time slot in the same market should sell related items (items generally bought together)
2) All types of shops opening in parallel markets should be as far away as possible to avoid people’s movement to all of the markets (selling items that are generally not bought together) 
To operationalize this intuition let us assume we are given a function representing the distance between two types/categories: d(t1, t2), such that d is between 0 and 1. We can similarly define a similarity between two, s(t1, t2) = 1 - d(t1, t2). 



Now we can define the goodness of a schedule as follows:
Sum(similarities of all pairs within a single time slot in the same market) + C.Sum(distances of all pairs within a single time slot in the parallel market).

In our example, the goodness will be computed as
G(Schedule) = s(1,2) + s(1,3) + s(1,4) + s(2,3) + s(2,4) + s(3,4) + s(5,6) + s(5,7) + s(5,8)
                        + s(6,7) + s(6,8) + s(7,8) + ……. + s(13,14) + …. + s(21,22) + ….. 
  + C x [d(1,13) + d(1,14)… d(2,13) + d(2,14) + … + d(5,17) + d(5,18) + …]
  
  
##Input:
Line 1: k: total types of shops opening in one time slot in one market
Line 2: m: number of parallel markets
Line 3: T: number of time slots
Line 4: C: trade-off constant
Starting on the fifth line we have a space separated list of distances between a type of shop and rest others. Note that d(x,y) = d(y,x). Also, all d(x,x) = 0.

##Sample Input:
2
2
1
1
0 0.4 0.8 1
0.4 0 0.6 0.7
0.8 0.6 0 0.3
1 0.7 0.3 0


##Output Format:
Space separated list of shop ids (i.e, shop’s type ids), where time slots are separated by bars and parallel markets are separated by line.

##Sample Output:
1 2
3 4

