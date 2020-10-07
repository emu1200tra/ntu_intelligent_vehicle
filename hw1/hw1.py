import numpy as np
import math

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
'''
Computing worst-case response time 
'''
for i in range(n):
    B = max(C[i:])
    Q = B
    while True:
        counting = 0.0
        for j in range(i):
            counting += math.ceil((Q+tow)/T[j])*C[j]
        if B+counting+C[i] > T[i]:
            print("not schedulable")
            break
        elif B+counting == Q:
            print(str(i)+":", Q+C[i])
            break
        else:
            Q = B+counting
