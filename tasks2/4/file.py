from sys import stdin
def read_test_case():
    t = int(stdin.readline().strip())
    connec = []
    case = 1
    for i in range (t):
        
        n, m = map(int, stdin.readline().split())
        for i in range(m):
            u, v = map(int, stdin.readline().split())
            connec.append((u,v))
        if case == 43:
            print(f'{n} {m}')
            for i in range(len(connec)):
                print(f'{connec[i][0]} {connec[i][1]}') 
        
        case +=1
        connec = []

read_test_case()