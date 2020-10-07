import numpy as np
import math
import time
import random

'''
worst case response time
'''
def worstCaseCal(n, C, tow, T, P):
    record = []
    for i in range(n):
        B = 0
        for j in range(n):
            if P[i] <= P[j] and B < C[j]:
                B = C[j]

        Q = B

        while True:
            counting = 0.0
            for j in range(n):
                if P[j] < P[i]:
                    counting += math.ceil((Q+tow)/T[j])*C[j]
            if B+counting+C[i] > T[i]:
                #print("not schedulable")
                return []
            elif B+counting == Q:
                #print(str(i)+":", Q+C[i])
                record.append(Q+C[i])
                break
            else:
                Q = B+counting
    return record

'''
cal cost
'''
def cost(n, C, tow, T, P):
    return sum(worstCaseCal(n, C, tow, T, P))

'''
Read in data and pruning
'''
with open("input.dat") as f:
    data = f.read().split('\n')[:-1]
    n = int(data[0])
    tow = float(data[1])
    data = data[2:]
    P = []
    C = []
    T = []
    for i in data:
        tmp = i.split(' ')
        tmp2 = []
        for j in tmp:
            if len(j) != 0:
                tmp2.append(float(j))
        P.append(tmp2[0])
        C.append(tmp2[1])
        T.append(tmp2[2])
    P = np.array(P)
    C = np.array(C)
    T = np.array(T)
'''
config
'''
temp = 1000.0
Sstar = P.copy()
tempMin = 1.0
startTime = time.time()
iterCount = 100
k = 0.95

'''
Main code frame
'''
while (temp > tempMin) and (time.time() - startTime < 15):
    for ite in range(iterCount):
        currCost = cost(n, C, tow, T, P)
        Pnew = P.copy()
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        tmp = Pnew[index1]
        Pnew[index1] = Pnew[index2]
        Pnew[index2] = tmp
        newCost = cost(n, C, tow, T, Pnew)
        if int(newCost) != 0:
            deltaCost = newCost - currCost
            if newCost < cost(n, C, tow, T, Sstar):
                Sstar = Pnew.copy()
            if deltaCost <= 0:
                P = Pnew.copy()
            else:
                prob = math.exp(-(deltaCost/temp))
                if np.random.choice([0,1],1,p=[prob,1-prob])[0] == 1:
                    P = Pnew.copy()
        else:
            #print('cons break')
            continue
        
    temp *= k
    print('next!', "time:", time.time() - startTime)

print('S*:')
for i in Sstar:
    print('\t', int(i))
print('objective value:', cost(n, C, tow, T, Sstar))

