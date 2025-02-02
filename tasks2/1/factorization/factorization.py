from collections import deque
from sys import stdin
from math import sqrt
def factorize(n):
    queue = deque() 
    result = deque() 
    queue.append((n, 2, [])) 
    while len(queue) > 0:
        current, start, current_factors =  queue.popleft()
        if current == 1 and len(current_factors) > 1:
            current_factors_aux = current_factors
            result.appendleft(current_factors_aux)
        else:
            i = start
            while i <= int(sqrt(current)):
                if current % i == 0:
                    queue.appendleft((current // i, i, current_factors + [i]))
                i+= 1

            if current >= start and len(current_factors) > 0:
                result.appendleft(current_factors + [current])
        
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