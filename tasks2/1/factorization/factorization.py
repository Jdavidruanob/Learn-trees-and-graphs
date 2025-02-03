""" Jose David Ruano Burbano 8982982 """
from collections import deque
from sys import stdin
from math import sqrt
def factorize(n):
    stack = deque() 
    result = deque() 
    stack.append((n, 2, [])) 

    while len(stack) > 0:
        actual, start, actual_factors =  stack.popleft()
        if len(actual_factors) > 1 and actual == 1:
            actual_factors_aux = actual_factors
            result.appendleft(actual_factors_aux)
        else:
            i = start
            while i <= int(sqrt(actual)):
                if actual % i == 0:
                    stack.appendleft((actual // i, i, actual_factors + [i]))
                i+= 1

            if actual >= start and len(actual_factors) > 0:
                result.appendleft(actual_factors + [actual])
        
    return result

def main():
    line = int(stdin.readline().strip()) 
    while line != 0:
        n = line
        factorizations = factorize(n)
        print(len(factorizations))
        for i in range(len(factorizations)):
            for j in range(len(factorizations[i])):
                if j == len(factorizations[i]) - 1:
                    print(factorizations[i][j])
                else:
                    print(factorizations[i][j], end= " ")
            
        line = int(stdin.readline().strip())
main()