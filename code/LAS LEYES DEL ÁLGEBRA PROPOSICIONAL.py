import itertools

# Definir las operaciones lógicas básicas
def NOT(a):
    return not a

def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

# Generar la tabla de verdad para una expresión lógica compleja
def truth_table():
    # Variables proposicionales
    variables = ['A', 'B', 'C']
    
    # Todas las combinaciones posibles de valores de verdad (True y False) para las variables
    combinations = list(itertools.product([True, False], repeat=len(variables)))
    
    # Imprimir encabezados
    print(f"{'A':<5}{'B':<5}{'C':<5}{'¬C':<5}{'B ∨ ¬C':<8}{'A ∧ (B ∨ ¬C)':<15}")
    print("-" * 40)
    
    # Evaluar la expresión lógica para cada combinación de valores de verdad
    for comb in combinations:
        A, B, C = comb
        not_C = NOT(C)
        B_or_not_C = OR(B, not_C)
        result = AND(A, B_or_not_C)
        
        # Imprimir fila de la tabla de verdad
        print(f"{A!s:<5}{B!s:<5}{C!s:<5}{not_C!s:<5}{B_or_not_C!s:<8}{result!s:<15}")

# Ejecutar la función para mostrar la tabla de verdad
truth_table()