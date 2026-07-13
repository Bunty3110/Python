#!/bin/python3

import math
import os
import random
import re
import sys



def dynamicArray(n, queries):
    # Write your code here
    arr=[[] for _ in range(n)]
    lastAnswer=0
    result=[]
    
    for query in queries:
        q, x, y = query
        idx=(x^ lastAnswer)%n
        if q == 1:
            arr[idx].append(y)
        if q == 2:
            lastAnswer = arr[idx][y% len(arr[idx])]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
