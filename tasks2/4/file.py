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




def read_test_case2():
    t = int(stdin.readline().strip())
    case = 1
    
    for _ in range(t):
        n, m = map(int, stdin.readline().split())
        cities = []
        connections = []
        
        for _ in range(n):
            name, year = stdin.readline().split()
            cities.append((name, int(year)))
        
        for _ in range(m):
            u, v = stdin.readline().split()
            connections.append((u, v))
        
        if case == 63:
            print(f"{n} {m}")
            for city in cities:
                print(f"{city[0]} {city[1]}")
            for connection in connections:
                print(f"{connection[0]} {connection[1]}")
        
        case += 1

read_test_case2()
