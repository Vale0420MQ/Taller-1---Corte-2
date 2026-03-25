class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha


# PARSER

class Parser:
    def __init__(self, cadena):
        self.cadena = cadena.replace(" ", "")
        self.pos = 0

    def actual(self):
        if self.pos < len(self.cadena):
            return self.cadena[self.pos]
        return None

    def avanzar(self):
        self.pos += 1

    def parse_E(self):
        nodo = self.parse_T()
        while self.actual() in ('+', '-'):
            op = self.actual()
            self.avanzar()
            nodo = Nodo(op, nodo, self.parse_T())
        return nodo

    def parse_T(self):
        nodo = self.parse_F()
        while self.actual() in ('*', '/'):
            op = self.actual()
            self.avanzar()
            nodo = Nodo(op, nodo, self.parse_F())
        return nodo

    def parse_F(self):
        if self.actual() == '(':
            self.avanzar()
            nodo = self.parse_E()
            if self.actual() == ')':
                self.avanzar()
            return nodo
        return self.parse_numero()

    def parse_numero(self):
        num = ""
        while self.actual() and self.actual().isdigit():
            num += self.actual()
            self.avanzar()
        return Nodo(num)



# DIBUJAR ÁRBOL 

def altura(nodo):
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.izquierda), altura(nodo.derecha))


def imprimir_arbol(nodo):
    h = altura(nodo)
    ancho = 2 ** h

    niveles = []

    def llenar(nodo, nivel, pos):
        if len(niveles) <= nivel:
            niveles.append([" "] * ancho)

        if nodo:
            niveles[nivel][pos] = str(nodo.valor)
            llenar(nodo.izquierda, nivel + 1, pos - 2 ** (h - nivel - 2))
            llenar(nodo.derecha, nivel + 1, pos + 2 ** (h - nivel - 2))

    llenar(nodo, 0, ancho // 2)

    for nivel in niveles:
        print("".join(nivel))



# MAIN

if __name__ == "__main__":
    while True:
        cadena = input("\nIngresa una expresión (o 'salir'): ")

        if cadena.lower() == "salir":
            break

        parser = Parser(cadena)
        arbol = parser.parse_E()

        print("\nÁrbol de sintaxis:\n")
        imprimir_arbol(arbol)
