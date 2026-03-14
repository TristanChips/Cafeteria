class Persona():
    def __init__(self, id_persona, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.id_persona = id_persona

    def iniciar_sesion(self, correo):
        if self.correo == correo:
            print(f"\nBienvenido {self.nombre} a nuestro sistema en línea\n")
        else:
            print(f"\nTu correo es incorrecto o aún no te has registrado\n")

    def actualizar_datos(self, id_persona, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.id_persona = id_persona
        print(f"\nLos datos se actualizaron correctamente\n")

    def imprimir_objeto(self):
        print(f"\nID:{self.id_persona}\t|\t{self.nombre}\t|\t{self.correo}\t\n")

class Cliente(Persona):
    lista_clientes = []
    def __init__(self, id_persona, nombre, correo, puntos_fidelidad, historial_compras):
       super().__init__(id_persona, nombre, correo)
       self.puntos_fidelidad = puntos_fidelidad
       self.historial_compras = historial_compras
       Cliente.lista_clientes.append(self)

    def realizar_compra(self):
        print(f"\nIniciando proceso de compra...\n")
        print(f"\nCliente: {self.nombre} (Puntos: {self.puntos_fidelidad})")
        print(f"\n¿Qué deseas comprar?\n")
        lista_productos_compra = {}
        while True:
            print(f"\nSelecciona una de las siguientes opciones:\n")
            print(f"1. Bebidas")
            print(f"2. Postres")
            print(f"3. Es todo")
            x = int(input("\n"))
            
            match x:
                case 1:
                    print("\nLas bebidas disponibles son:\n")
                    for bebida in Bebida.lista:
                        bebida.imprimir_objeto()
                    x1 = int(input("¿Cuántos tipos de productos diferentes deseas? "))
                    for i in range(x1):
                        lista_productos_compra[i] = 0
                        nombre_ = input("Introduce el nombre del producto: ")
                        z = int(input("¿Cuántos?: "))
                        if nombre_ in lista_productos_compra:
                            lista_productos_compra[nombre_] += z
                            del lista_productos_compra[i]
                        else:
                            lista_productos_compra[nombre_] = lista_productos_compra.pop(i)
                            lista_productos_compra[nombre_] = z
                case 2:
                    print("\nLos postres disponibles son:\n")
                    for postre in Postre.lista:
                        postre.imprimir_objeto()
                    x11 = int(input("¿Cuántos tipos de productos diferentes deseas? "))
                    for i in range(x11):
                        lista_productos_compra[i] = 0
                        nombre_1 = input("Introduce el nombre del producto: ")
                        z1 = int(input("¿Cuántos?: "))
                        if nombre_1 in lista_productos_compra:
                            lista_productos_compra[nombre_1] += z1
                            del lista_productos_compra[i]
                        else:
                            lista_productos_compra[nombre_1] = lista_productos_compra.pop(i)
                            lista_productos_compra[nombre_1] = z1
                case 3:
                    print("Gracias por tu compra")
                    break                 
        nueva_compra = Compra(lista_productos_compra, "SIN PAGAR")
        nueva_compra.calcular_total()
        self.historial_compras.append(nueva_compra)
        print("\nVISUALIZAR COMPRA\n")
        nueva_compra.imprimir_objeto()
        lista_productos_compra.clear()                

    def imprimir_objeto(self):
        print(f"\nID:{self.id_persona}\t|\t{self.nombre}\t|\t{self.correo}\t|\tPUNTOS:{self.puntos_fidelidad}\t\n")

    def consultar_historial(self):
        print(f"\nLas compras actuales son:\n")
        for p in self.historial_compras:
            p.imprimir_objeto()

    def usar_puntos(self):
        print(f"\nBuscando cliente con ID: {self.id_persona}\n")
        if(self.puntos_fidelidad >= 160):
            print(f"¡Puedes obtener un café gratis!")
        else:
            print(f"Necesitas más puntos....")

class Empleado(Persona):
     def __init__(self, id_persona, id_empleado, nombre, correo, rol):
       super().__init__(id_persona, nombre, correo)
       self.rol = rol
       self.id_empleado = id_empleado

     def actualizar_inventario(self, cantidad, producto, inv):
       print(f"Inventario antes de la actualización de {cantidad} {producto}:")
       inv.imprimir_objeto()
       for clave in inv.ingredientes:
           if clave == producto:
                inv.ingredientes[clave] = cantidad
       print("El inventario ha sido modificado")
       inv.imprimir_objeto()

     def cambiar_estatus(self, id_compra_):
         for c in Compra.lista_compras:
             if(c.id_compra == id_compra_):
                 t = input("Introduce el nuevo estatus para esta compra: ")
                 c.estatus = t
                 print("Tu cambio ha sido enviado:")
                 c.imprimir_objeto()

     def imprimir_objeto(self):
        print(f"\nID:{self.id_persona}\t|\t{self.nombre}\t|\t{self.correo}\t|\tID_EMPLEADO:{self.id_empleado}\t|\tROL:{self.rol}\t\n")

class Producto_base():
    lista_productos = []
    def __init__(self, id_producto, nombre, precio_base):
        self.nombre = nombre
        self.id_producto = id_producto
        self.precio_base = precio_base

    def imprimir_objeto(self):
        print(f"\nID:{self.id_producto}\t|\t{self.nombre}\t|\tPRECIO BASE: {self.precio_base}\t\n")

class Bebida(Producto_base):
    lista = []
    modificadores_generales = {"Leche de Almendras": 50, "Leche de Avena": 40, "Leche de Soya": 20, "Azúcar Extra": 10, "Hielo Extra": 80}
    def __init__(self, id_producto, nombre, precio_base, tamano, temperatura, modificadores):
       super().__init__(id_producto, nombre, precio_base)
       self.tamano = tamano
       self.temperatura = temperatura
       self.modificadores = modificadores
       Producto_base.lista_productos.append(self)
       Bebida.lista.append(self)

    def añadir_extra(self):
        print(f"¿Deseas añadir modificadores a tu bebida? (Si/No)")
        t = input()
        if(t.lower() == "si"):
                f = int(input("¿Cuántos? "))
                for i in range(f):
                    print("Los modificadores disponibles son:")
                    for mod, valor in Bebida.modificadores_generales.items():
                        print(f"-{mod}|\t-${valor}\n")
                    g = input("Selecciona uno: ")
                    self.modificadores.append(g)
                print("¡Has seleccionado todos tus extras!")
        else:
            print("¡No te preocupes!, el sabor será delicioso incluso sin extras")

    def calcular_precio_final(self):
        print(f"Tu precio inicial es {self.precio_base}\n")
        for g in self.modificadores:
            if g in Bebida.modificadores_generales:
                self.precio_base += Bebida.modificadores_generales[g]
        
        if(len(self.modificadores) != 0):
            print("Seleccionaste extras:")
            for g in self.modificadores:
                    print(f"Modificador: {g}\n")
            print(f"Todos tus extras fueron añadidos, tu nuevo precio es {self.precio_base}")
        else:
            print("Tu precio sigue siendo el mismo porque no seleccionaste extras")

    def imprimir_objeto(self):
        print(f"\nID:{self.id_producto}  | {self.nombre} | PRECIO BASE: {self.precio_base} | TAMAÑO:{self.tamano} | TEMPERATURA: {self.temperatura}  | MODIFICADORES: {self.modificadores} \n")

class Postre(Producto_base):
  lista = []
  def __init__(self, id_producto, nombre, precio_base, esVegano, sinGluten):
       super().__init__(id_producto, nombre, precio_base)
       self.esVegano = esVegano
       self.sinGluten = sinGluten
       Producto_base.lista_productos.append(self)
       Postre.lista.append(self)

  def imprimir_objeto(self):
         print(f"\nID:{self.id_producto}  | {self.nombre} | PRECIO BASE: {self.precio_base} | ¿ES VEGANO?: {self.esVegano} | ¿SIN GLUTEN?: {self.sinGluten}\n")

class Compra():
    contador = 0
    lista_compras = []
    def __init__(self, productos, estatus):
        Compra.contador += 1
        self.productos = productos
        self.estatus = estatus
        self.total = 0
        self.id_compra = Compra.contador
        Compra.lista_compras.append(self)

    def calcular_total(self):
       for p in self.productos:
           for t in Producto_base.lista_productos:
               if p == t.nombre:
                    self.total += (self.productos[p] * (t.precio_base))
       print(f"Tu total final es {self.total}")
       return self.total

    def verificar_stock(self, inv, ingrediente):
        # Aquí restauré el ciclo for original que tenías para que sea idéntico en longitud
        for clave, valor in inv.ingredientes.items():
            if clave == ingrediente:
                if valor <= 0:
                    print("No hay suficientes ingredientes")
                    return False
                else:    
                    print("Todo está en orden")
                    return True

    def imprimir_objeto(self):
        if self.total == 0:
            for p in self.productos:
                for t in Producto_base.lista_productos:
                    if p == t.nombre:
                        self.total += (self.productos[p] * (t.base_price))
        print(f"\nPRODUCTOS:")
        for p, k in self.productos.items():
            print(f"PRODUCTO {p} : {k} ")
        print(f"ESTATUS {self.estatus} \t|\tTOTAL: {self.total}\t \n")

class Inventario():
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def reducir_stock(self, ing, cantidad):
        print(f"Inventario antes de la reducción de {cantidad} {ing}:")
        self.imprimir_objeto()
        for l, p in self.ingredientes.items():
             if l == ing:
                 self.ingredientes[l] -= cantidad
        print(f"Tu stock ha sido modificado")
        self.imprimir_objeto()

    def notificar_sin_stock(self, ingrediente):
            if self.ingredientes[ingrediente] == 0:
                print(f"No hay stock de {ingrediente}")
            else:
                 print(f"Todavía hay stock de {ingrediente}")

    def imprimir_objeto(self):
         for l, p in self.ingredientes.items():
            print(f"INGREDIENTE:{l}-{p}\t")
         print("\n")