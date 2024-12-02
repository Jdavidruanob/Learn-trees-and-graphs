def read_test_case(file_path, case_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    current_case = 0
    index = 0
    while index < len(lines):
        # Leer n y m
        n, m = map(int, lines[index].strip().split())
        index += 1
        
        # Verificar si es el caso de prueba que queremos
        if current_case == case_number:
            test_case = [f"{n} {m}"]
            for _ in range(m):
                test_case.append(lines[index].strip())
                index += 1
            return "\n".join(test_case)
        
        # Saltar las siguientes m líneas
        index += m
        current_case += 1
    
    return "Caso de prueba no encontrado"

# Ejemplo de uso
file_path = 'graff.in'
case_number = int(input("Ingrese el número del caso de prueba que desea: "))
print(read_test_case(file_path, case_number))