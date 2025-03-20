from sys import stdin
def read_test_case():
    line = stdin.readline()
    case = 1
    while line != "":
        n, m = map(int, line.split())
        capacities = list(map(int, stdin.readline().split()))
        conections = []
        for i in range(m):
            u, v = map(int, stdin.readline().split())
            conections.append((u, v))


        if case == 50:
            print(f'{n} {m}')
            for i in range(len(capacities)):
                print(f'{capacities[i]}', end= " ")
            print()
            for i in range(len(conections)):
                
                print(f'{conections[i][0]} {conections[i][1]}\n', end= "")
            return
        case += 1
        line = stdin.readline()



    
    
    
    return 

# Ejemplo de uso

read_test_case()