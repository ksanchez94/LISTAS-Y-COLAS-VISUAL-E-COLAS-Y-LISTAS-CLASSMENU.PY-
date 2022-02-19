class Menu:
    def _init_(self, nm, opc):
        self.nombreMenu= nm
        self.opciones= opc

    
    def menus(self):
        print(self.nombreMenu)
        for opcion in self.opciones:
            print(opcion)
        opc=int(input("Elija la opción del 1 al {} que desea escoger: ".format(len(self.opciones))))
        while   opc < 1 or  opc > len(self.opciones) :
            opc=int(input("Ingrese una opcion que sea valida: "))
        return opc
        from lista import Lista
        from cola import Cola
        from pila import Pila
        from menu import Menu
        import os


opcion= 1
while opcion != 4:
    men = Menu("Menú Principal",["1) Pilas", "2) Colas", "3) Listas", "4) Salir"])
    opcion= men.menus()
    os.system ("cls")

    if opcion == 1:
        print('             Haz ingresado al menú "PILAS"')
        canti=int(input("Por favor, ingresa la cantidad maxima de valores de tu Pila: "))
        while canti < 1:
            print("No puedes crear una Pila de longitud",canti)
            canti=int(input("Por favor Ingresa una longitud válida: "))
        os.system ("cls")
        pil = Pila(canti)
        opc= 1
        while opc != 6:
            men = Menu("Menú Pilas", ["1) Push", "2) Pop", "3) Show", "4) Empty", "5) Longitud", "6) Salir"])
            opc= men.menus()
            os.system ("cls")
            if opc == 1:
                n=input("Ingrese su {}º valor: ".format(pil.longitud()+1))
                pil.push(n)
                input("Presione ¨ENTER¨ para volver al menú Pilas ")
                os.system ("cls")
            if opc == 2:
                sacar= pil.pop()
                if sacar == -1: print("ERROR DE EGRESO: La pila está vacía")
                else: print("El valor [{}] ha sido egresado".format(sacar))
                input("Presione ¨ENTER¨ para volver al menú Pilas ")
                os.system ("cls")
            if opc == 3:
                pil.show()
                input("Presione ¨ENTER¨ para volver al menú Pilas ")
                os.system ("cls")
            if opc == 4:
                if pil.empty() == True: print("La lista está vacía")
                else: print("La lista no está vacía")
                input("Presione ¨ENTER¨ para volver al menú Pilas")
                os.system ("cls")
            if opc == 5:
                print('Longitud de Pila: "{}"'.format(pil.longitud()))
                input("Presione ¨ENTER¨ para volver al menú Pilas")
                os.system ("cls")
    
    if opcion == 2:
        print('             Haz ingresado al menú "COLAS"')
        canti=int(input("Por favor, ingresa la cantidad maxima de valores de tu Cola: "))
        while canti < 1:
            print("No puedes crear una Cola de longitud",canti)
            canti=int(input("Por favor Ingresa una longitud válida: "))
        os.system ("cls")
        col = Cola(canti)
        opc= 1
        while opc != 6:
            men = Menu("Menú Colas", ["1) Push", "2) Pop", "3) Show", "4) Empty", "5) Longitud", "6) Salir"])
            opc= men.menus()
            os.system ("cls")
            if opc == 1:
                n=input("Ingrese su {}º valor: ".format(col.longitud()+1))
                col.push(n)
                input("Presione ¨ENTER¨ para volver al menú Colas ")
                os.system ("cls")
            if opc == 2:
                sacar= col.pop()
                if sacar == -1: print("ERROR DE EGRESO: La pila está vacía")
                else: print("El valor [{}] ha sido egresado".format(sacar))
                input("Presione ¨ENTER¨ para volver al menú Colas ")
                os.system ("cls")
            if opc == 3:
                col.show()
                input("Presione ¨ENTER¨ para volver al menú Colas ")
                os.system ("cls")
            if opc == 4:
                if col.empty() == True: print("La lista está vacía")
                else: print("La lista no está vacía")
                input("Presione ¨ENTER¨ para volver al menú Colas ")
                os.system ("cls")
            if opc == 5:
                print('Longitud de Cola: "{}"'.format(col.longitud()))
                input("Presione ¨ENTER¨ para volver al menú Colas ")
                os.system ("cls")
    
    if opcion == 3:
        print('                  Haz ingresado al menú "LISTAS"')
        canti=int(input("Por favor, ingresa la cantidad maxima de valores de tu Lista: "))
        while canti < 1:
            print("No puedes crear una Lista de longitud",canti)
            canti=int(input("Por favor Ingresa una longitud válida: "))
        os.system ("cls")
        lis = Lista(canti)
        opc= 1
        while opc != 7:
            men = Menu("Menú Listas", ["1) Append", "2) Obtener", "3) Buscar", "4) Insertar", "5) Eliminar", "6) Mostrar", "7) Salir"])
            opc= men.menus()
            os.system ("cls")
            if opc == 1:
                n=input("Ingrese el valor que desea agregar a la lista: ")
                lis.append(n)
                input("Presione ¨ENTER¨ para volver al menú Listas ")
                os.system ("cls")
            if opc == 2:
                pos= input("Ingrese la posición que desea obtener: ")
                valor= lis.obtener(pos)
                if valor == -1: print("Posición no encontrada ")
                else: print("El valor [{}] se encuentra en la posición {}".format(valor,pos))
                input("Presione ¨ENTER¨ para volver al menú Listas ")
                os.system ("cls")
            if opc == 3:
                n=input("Ingrese el valor que desea encontrar: ")
                pos= lis.buscar(n)
                if pos == -1: print("El valor [{}] no se encuantra en su lista ".format(n))
                else: print("el valor {} se encuentra en la posición {}".format(n,pos))
                input("Presione ¨ENTER¨ para volver al menú Listas ")
                os.system ("cls")
            if opc == 4:
                n= input("Ingrese el dato que desee agregar a su lista:  ")
                pos= lis.insertar(n)
                if pos == -1: print("No se insertó el dato porque ya existe en la lista")
                input("Presione ¨ENTER¨ para volver al menú Listas ")
                os.system ("cls")
            if opc == 5:
                n=input("Ingrese el dato que desee eliminar: ")
                pos = lis.eliminar(n)
                if pos == -1: print("ERROR DE ELIMINACIÓN: El dato ingresado no se encuentra en la lista")
                else: print("El dato se ha eliminado correctamente")
                input("Presione ¨ENTER¨ para volver al menú Listas ")
                os.system ("cls")
            if opc == 6:
                orden=input(('1) Presentar en orden "Ascendente" \n2) Presentar en orden "Descendente"\n: '))
                lis.mostrar(orden)
                input("Presione ¨ENTER¨ para volver al menú Listas ")
                os.system ("cls")
    
    else: print("Gracias por su visita")
    class Pila:
        def _init_(self,tamaño):
        self.__lista=[]
        self.__tope=0
        self.__size=tamaño

    def empty(self):
        return self.__tope==0

    def push(self,dato):
        if self.__tope < self.size:
            self.__lista+= [dato]
            self.__tope+= 1
            print("El valor {} ha sido ingreado".format(dato))
        else: print("ERROR DE INGRESO: La lista está llena")
    
    def pop(self):
        if self.empty(): return -1
        else:
            top= self.__lista[-1]
            self.__tope-= 1
            self._lista= self._lista[:-1]
            return top

    def show(self):
        if self.empty(): print("No hay valores para mostrar")
        else:
            for top in range(self.__tope-1,-1,-1):
                print("[{}]".format(self.__lista[top]))
        
    def longitud(self):
        return self.__tope
    class Cola:
        def _init_(self,tamaño):
        self,__lista=[]
        self,__tope=0
        self,size=tamaño

    def empty(self):
        return self.__tope==0

    def push(self,dato):
        if self.__tope < self.size:
            self.__lista+= [dato]
            self.__tope+= 1
            print("El valor {} ha sido ingreado".format(dato))
        else: print("ERROR DE INGRESO: La lista está llena")
    
    def pop(self):
        if self.empty(): return -1
        else:
            top= self.__lista[0]
            self.__tope-= 1
            self._lista= self._lista[1:]
            return top
    
    def show(self):
        if self.empty(): print("No hay valores para mostrar")
        else:
            for ele in range(0,self.__tope):
                print("[{}]".format(self.__lista[ele]))
    
    def longitud(self):
        return self.__tope
    class Lista:
        def _init_(self,tamanio):
        self.lista = []
        self.longitud=0
        self.size = tamanio
        
    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud += 1
            print("El valor {} ha sido ingresado correctamente".format(dato))
        else:
            print("ERROR DE INGRESO: La lista esta llena")
    
    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return -1
        else:
            valor = self.lista[pos]
            listaAux= self.lista[0:pos]
            for indice in range (pos,self.longitud-1):
                listaAux+= [self.lista[indice+1]]
            self.longitud -= 1
            self.lista= listaAux
            return valor 
            
    def buscar(self,dato):
        ban = False
        for a in range(0,self.longitud):
            if dato == self.lista[a]:
                ban = True
                break
        if ban: return a
        else: return -1
            
    def insertar(self,dato):
        if self.buscar(dato) == -1:
            self.append(dato)
        else: return -1
                     
    def eliminar(self,dato):
        pos = self.buscar(dato)
        if pos != -1:
            self.obtener(pos)
            #self.lista = self.lista[0:pos] + self.lista[pos+1:]
            #self.longitud -= 1
        else: return -1                 
            
    def mostrar(self,orden):
        if orden == 1:
            for pos in range(0,self.longitud):
                print("[{}]".format(self.lista[pos]))
        else:
            for pos in range(self.longitud-1,-1,-1):
                print("[{}]".format(self.lista[pos]))