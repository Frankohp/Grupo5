from lista_enlazada.lista_ehnlazada_simple import ListaEnlazada

def main():
    lista = ListaEnlazada()
    
    lista.insertar_inicio(10)
    lista.insertar_inicio(20)
    lista.insertar_inicio(30)
    
    lista.recorrer()
    
    print(lista)
    print("hola_mundo")

if __name__ =="__main__":
    main()