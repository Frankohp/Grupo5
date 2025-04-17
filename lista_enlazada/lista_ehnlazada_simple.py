class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0
        
    def esta_vacia (self):
        return self.cabeza is None
    
    def insertar_inicio (self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.longitud += 1
    
    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1
        
    def recorrer (self):
        if self.esta_vacia():
            print("esta vacia")
            return
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")