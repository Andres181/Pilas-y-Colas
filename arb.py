class Nodo():
    def __init__ (self, valor, izq = None, der = None):
        self.valor = valor
        self.izq = izq
        self.der = der

def evaluar(arbol):
        if arbol.valor == '+':
            return evaluar(arbol.izq) + evaluar(arbol.der)
        elif arbol.valor == '-':
            return evaluar(arbol.izq) - evaluar(arbol.der)
        elif arbol.valor == '/':
            return evaluar(arbol.izq) / evaluar(arbol.der)
        elif arbol.valor == '*':
            return evaluar(arbol.izq) * evaluar(arbol.der)
        else:
            return arbol.valor

operacion =raw_input("Ingrese la operacion en posorden: ").split(" ")

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

pila = Pila()

for i in operacion:
    if i=='+' or i=='-' or i=='*' or i=='/':
        izq=pila.desapilar()
        der=pila.desapilar()
        nodo = Nodo(i, izq, der)
        pila.apilar(nodo)
    else:
        nodo=Nodo(int(i), None, None)
        pila.apilar(nodo)

print (evaluar(pila.desapilar()))


