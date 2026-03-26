class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

class Parser:
    def __init__(self, cadena):
        # Eliminamos espacios para facilitar el análisis
        self.cadena = cadena.replace(" ", "")
        self.pos = 0

    def actual(self):
        return self.cadena[self.pos] if self.pos < len(self.cadena) else None

    def avanzar(self):
        self.pos += 1

    # E -> E opsuma T | T
    def parse_E(self):
        nodo = self.parse_T()
        while self.actual() in ('+', '-'): # opsuma
            op = self.actual()
            self.avanzar()
            nodo = Nodo(op, nodo, self.parse_T())
        return nodo

    # T -> T opmul F | F
    def parse_T(self):
        nodo = self.parse_F()
        while self.actual() in ('*', '/'): # opmul
            op = self.actual()
            self.avanzar()
            nodo = Nodo(op, nodo, self.parse_F())
        return nodo

    # F -> id | num | pari E pard
    def parse_F(self):
        token = self.actual()

        # Regla: F -> pari E pard
        if token == '(': 
            self.avanzar() # pari
            nodo = self.parse_E()
            if self.actual() == ')':
                self.avanzar() # pard
            return nodo

        # Regla: F -> id (letras)
        if token and token.isalpha():
            return self.parse_id()

        # Regla: F -> num (dígitos)
        if token and token.isdigit():
            return self.parse_numero()
        
        return None

    def parse_id(self):
        identificador = ""
        while self.actual() and self.actual().isalpha():
            identificador += self.actual()
            self.avanzar()
        return Nodo(identificador)

    def parse_numero(self):
        num = ""
        while self.actual() and self.actual().isdigit():
            num += self.actual()
            self.avanzar()
        return Nodo(num)

# --- Funciones de visualización (Sin cambios) ---
def altura(nodo):
    if nodo is None: return 0
    return 1 + max(altura(nodo.izquierda), altura(nodo.derecha))

def imprimir_arbol(nodo):
    if not nodo: return
    h = altura(nodo)
    ancho = 2 ** h
    niveles = []
    def llenar(nodo, nivel, pos):
        if len(niveles) <= nivel: niveles.append([" "] * (ancho * 4))
        if nodo:
            niveles[nivel][pos] = str(nodo.valor)
            offset = 2 ** (h - nivel - 2)
            llenar(nodo.izquierda, nivel + 1, pos - offset)
            llenar(nodo.derecha, nivel + 1, pos + offset)
    llenar(nodo, 0, (ancho * 4) // 2)
    for nivel in niveles:
        linea = "".join(nivel).rstrip()
        if linea: print(linea)

if __name__ == "__main__":
   
    while True:
        cadena = input("\nIngresa una expresión (o 'salir'): ")
        if cadena.lower() == "salir": break
        try:
            parser = Parser(cadena)
            arbol = parser.parse_E()
            print("\nÁrbol de sintaxis:")
            imprimir_arbol(arbol)
        except Exception as e:
            print(f"Error al procesar: {e}")
