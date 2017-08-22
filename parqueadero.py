class Cola (object):

    def __init__(self):
        self.items=[]

    def encolar (self,dato):
        self.items.append(dato)

    def desencolar (self):
        if self.esta_vacia():
            return None
        else:
            return self.items.pop(0)

    def esta_vacia(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def mirarElementos(self):
        x=""
        if len(self.items)!=0:
            for i in self.items:
                x+=("-"+i.detalles())
        return x;

    def buscarPlaca(self, p):
        if len(self.items)!=0:
            for i in self.items:
                if i.getPlaca() == p:
                    return "EXISTE: "+i.detalles()
        return "No se encontro la placa";

    def buscarColor(self, p):
        if len(self.items)!=0:
            for i in self.items:
                if i.getColor() == p:
                    return "EXISTE: "+i.detalles()
        return "No se encontro moto con dicho Color";

    def buscarPropietario(self, p):
        if len(self.items)!=0:
            for i in self.items:
                if i.getPropietario() == p:
                    return "EXISTE: "+i.detalles()
        return "No se encontro moto con dicho propietario";
        
        

class Moto:

    def __init__(self, placa, color, propietario):

        self.p = placa
        self.c = color
        self.pr = propietario

    def detalles (self):
        return self.p +" "+ self.c +" "+ self.pr

    def getPlaca (self):
        return self.p+""

    def getColor (self):
        return self.c+""

    def getPropietario (self):
        return self.pr+""

    
def main ():
    q = Cola()

    moto1=Moto("BIP890","Rojo","No se")
    moto2=Moto("S","Verde","Aiuda")

    q.encolar(moto1)
    q.encolar(moto2)

    print(q.mirarElementos())
    
    print(q.buscarPlaca("BIP890"))
    print(q.buscarPlaca("BIP89"))

    print(q.buscarColor("Rojo"))
    print(q.buscarColor("BR"))

    print(q.buscarPropietario("Nas"))
    print(q.buscarPropietario("Aiuda"))
    
    
    #placa = raw_input("Ingrese Placa de la moto")
    #color = raw_input("Ingrese color de la moto")
    #propietario = raw_input("Ingrese propietario de la moto")
    

main()



        
