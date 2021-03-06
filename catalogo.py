class Pila(object):
    
    def __init__(self):
        self.items=[]

    def apilar (self,dato):
        self.items.append(dato)

    def desapilar(self):
        if self.esta_vacia():
            return None
        else:
            return self.items.pop()

    def esta_vacia(self):
        if len(self.items)==0:
            return True
        else:
            return False

class Pelicula :

    def __init__ (self, titulo, genero, protagonista, ano):
        self.titulo = titulo
        self.genero = genero
        self.protagonista = protagonista
        self.ano = ano

def buscar(pilaentrada,dato):
    print("Entrando a buscar al catalogo...")
    pilasalida = Pila()
    while (not pilaentrada.esta_vacia()):
        pelicula=pilaentrada.desapilar()

        if pelicula.titulo==dato or pelicula.genero==dato or pelicula.protagonista==dato or pelicula.ano==dato:
            pilasalida.apilar(pelicula)
            print("agregando pelicula a lista de resultados...")

    return pilasalida

def imprimirpila(pila):

    if pila.esta_vacia():
        print('Dato no encontrado')
    else :
        
        while(not pila.esta_vacia()):
            pelicula = pila.desapilar();
            print('\n')
            print("TITULO : ",pelicula.titulo," GENERO : ",pelicula.genero," PROTAGONISTA : ",pelicula.protagonista," AÑO : ",pelicula.ano)

titanic = Pelicula('TITANIC','DRAMA','Leonardo Di Caprio','1997')
harrypotter = Pelicula('HARRY POTTER','FANTASIA','Daniel Radcliffe','2001')
matrix = Pelicula('MATRIX','CIENCIA FICCION','Keanu Reeves','1999')
matrix2 = Pelicula('MATRIX 2','CIENCIA FICCION','Keanu Reeves','2002')

catalogo = Pila()

catalogo.apilar(titanic)
catalogo.apilar(harrypotter)
catalogo.apilar(matrix)
catalogo.apilar(matrix2)

                       

print("Ingrese el dato a buscar en el catalogo")

busqueda =input()

resultado=buscar(catalogo,busqueda)
imprimirpila(resultado)


