import time
import random


# ALGORITMO CYK (O(n^3))

def cyk(grammar, string):
    n = len(string)
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Inicialización
    for i in range(n):
        for lhs, rules in grammar.items():
            for rule in rules:
                if len(rule) == 1 and rule[0] == string[i]:
                    table[i][i].add(lhs)

    # Llenado de la tabla
    for l in range(2, n + 1):  # longitud de subcadena
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for lhs, rules in grammar.items():
                    for rule in rules:
                        if len(rule) == 2:
                            B, C = rule
                            if B in table[i][k] and C in table[k+1][j]:
                                table[i][j].add(lhs)

    return 'S' in table[0][n-1]


# Gramática en CNF
grammar_cyk = {
    'S': [('A', 'B'), ('B', 'C')],
    'A': [('B', 'A'), ('a',)],
    'B': [('C', 'C'), ('b',)],
    'C': [('A', 'B'), ('a',)]
}



# PARSER DESCENDENTE SIMPLE (O(n))

# Gramática tipo LL(1)
# S -> a S b | ε

def parse_linear(s):
    def S(i):
        if i < len(s) and s[i] == 'a':
            i = S(i + 1)
            if i < len(s) and s[i] == 'b':
                return i + 1
            else:
                return -1
        return i  # epsilon

    result = S(0)
    return result == len(s)



# CADENAS


def generate_string(n):
    return ''.join(random.choice(['a', 'b']) for _ in range(n))


# COMPARACIÓN DE TIEMPOS


def compare():
    sizes = [5, 10, 15, 20, 25]

    print(f"{'n':<5}{'CYK (s)':<15}{'Lineal (s)':<15}")
    print("-" * 35)

    for n in sizes:
        test_string = generate_string(n)

        # CYK
        start = time.time()
        cyk(grammar_cyk, test_string)
        cyk_time = time.time() - start

        # Lineal
        start = time.time()
        parse_linear(test_string)
        linear_time = time.time() - start

        print(f"{n:<5}{cyk_time:<15.6f}{linear_time:<15.6f}")


if __name__ == "__main__":
    compare()