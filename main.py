from models import *

# --- PERSONAS ---
p1 = Persona(1001, "Leo", "leo@mail.com")
p2 = Persona(1002, "Nina", "nina@mail.com")
p3 = Persona(1003, "John", "john@mail.com")
p4 = Persona(1004, "Alice", "alice@mail.com")
p5 = Persona(1005, "Paula", "paula@mail.com")
p6 = Persona(1006, "Emma", "emma@mail.com")
p7 = Persona(1007, "Oscar", "oscar@mail.com")
p8 = Persona(1008, "Bob", "bob@mail.com")
p9 = Persona(1009, "Clara", "clara@mail.com")
p10 = Persona(1010, "David", "david@mail.com")

# --- CLIENTES ---
c1 = Cliente("C001", "Daniel Vega", "daniel@gmail.com", 60, [])
c2 = Cliente("C002", "Luis Perez", "luis@gmail.com", 200, [])
c3 = Cliente("C003", "Sofia Ramirez", "sofia@gmail.com", 75, [])
c4 = Cliente("C004", "Carlos Diaz", "carlos@gmail.com", 300, [])
c5 = Cliente("C005", "Ana Lopez", "ana@gmail.com", 120, [])
c6 = Cliente("C006", "Pedro Gomez", "pedro@gmail.com", 180, [])
c7 = Cliente("C007", "Maria Torres", "maria@gmail.com", 90, [])
c8 = Cliente("C008", "Miguel Castro", "miguel@gmail.com", 220, [])
c9 = Cliente("C009", "Valeria Ortiz", "valeria@gmail.com", 140, [])
c10 = Cliente("C010", "Laura Ruiz", "laura@gmail.com", 50, [])

# --- EMPLEADO ---
e1 = Empleado("P001", "E001", "Lucia Herrera", "lucia@cafe.com", "MESERO")
e2 = Empleado("P002", "E002", "Jorge Martinez", "jorge@cafe.com", "BARISTA")
e3 = Empleado("P003", "E003", "Gabriela Soto", "gabriela@cafe.com", "BARISTA")
e4 = Empleado("P004", "E004", "Patricia Luna", "patricia@cafe.com", "BARISTA")
e5 = Empleado("P005", "E005", "Raul Mendoza", "raul@cafe.com", "MESERO")
e6 = Empleado("P006", "E006", "Elena Sanchez", "elena@cafe.com", "MESERO")
e7 = Empleado("P007", "E007", "Fernando Rios", "fernando@cafe.com", "MESERO")
e8 = Empleado("P008", "E008", "Diana Vargas", "diana@cafe.com", "GERENTE")
e9 = Empleado("P009", "E009", "Andres Pineda", "andres@cafe.com", "BARISTA")
e10 = Empleado("P010", "E010", "Ricardo Flores", "ricardo@cafe.com", "GERENTE")

# --- PRODUCTOS BASE ---
bp1 = Producto_base("BP001", "Sandwich", 55)
bp2 = Producto_base("BP002", "Bagel", 40)
bp3 = Producto_base("BP003", "Croissant", 45)
bp4 = Producto_base("BP004", "Barra de Granola", 25)
bp5 = Producto_base("BP005", "Copa de Yogur", 35)
bp6 = Producto_base("BP006", "Tazón de Fruta", 50)
bp7 = Producto_base("BP007", "Barra Energética", 30)
bp8 = Producto_base("BP008", "Tostada", 20)
bp9 = Producto_base("BP009", "Sandwich de Jamón", 65)
bp10 = Producto_base("BP010", "Sandwich de Queso", 60)

# --- BEBIDAS ---
d1 = Bebida("D001", "Espresso", 40, "CHICO", "CALIENTE", [])
d2 = Bebida("D002", "Latte", 60, "MEDIANO", "CALIENTE", [])
d3 = Bebida("D003", "Cappuccino", 65, "MEDIANO", "CALIENTE", [])
d4 = Bebida("D004", "Mocha", 70, "GRANDE", "CALIENTE", [])
d5 = Bebida("D005", "Americano", 50, "MEDIANO", "CALIENTE", [])
d6 = Bebida("D006", "Cold Brew", 75, "GRANDE", "FRÍO", [])
d7 = Bebida("D007", "Iced Latte", 70, "GRANDE", "FRÍO", [])
d8 = Bebida("D008", "Caramel Macchiato", 80, "GRANDE", "CALIENTE", [])
d9 = Bebida("D009", "Flat White", 65, "MEDIANO", "CALIENTE", [])
d10 = Bebida("D010", "Vanilla Latte", 75, "GRANDE", "CALIENTE", [])

# --- POSTRES ---
ds1 = Postre("DS001", "Cheesecake", 90, False, False)
ds2 = Postre("DS002", "Pastel de Chocolate", 85, False, False)
ds3 = Postre("DS003", "Brownie", 50, False, False)
ds4 = Postre("DS004", "Galleta Vegana", 45, True, True)
ds5 = Postre("DS005", "Pay de Manzana", 70, False, False)
ds6 = Postre("DS006", "Pastel de Zanahoria", 80, False, False)
ds7 = Postre("DS007", "Muffin Sin Gluten", 55, False, True)
ds8 = Postre("DS008", "Tiramisu", 95, False, False)
ds9 = Postre("DS009", "Cupcake", 40, False, False)
ds10 = Postre("DS010", "Brownie Vegano", 60, True, True)

# --- COMPRAS ---
pp1 = Compra({"Espresso": 2, "Brownie": 1}, "PENDIENTE")
pp2 = Compra({"Latte": 1, "Cheesecake": 1}, "PENDIENTE")
pp3 = Compra({"Cappuccino": 3}, "PREPARANDO")
pp4 = Compra({"Mocha": 2, "Cupcake": 2}, "ENTREGADO")
pp5 = Compra({"Americano": 1}, "PENDIENTE")
pp6 = Compra({"Cold Brew": 2, "Pay de Manzana": 1}, "PREPARANDO")
pp7 = Compra({"Iced Latte": 1}, "ENTREGADO")
pp8 = Compra({"Caramel Macchiato": 2}, "PENDIENTE")
pp9 = Compra({"Flat White": 1, "Brownie": 2}, "PREPARANDO")
pp10 = Compra({"Vanilla Latte": 3}, "ENTREGADO")

# --- INVENTARIOS ---
i1 = Inventario({"Granos de Café": 100, "Leche": 80, "Azúcar": 120, "Chocolate": 50})
i2 = Inventario({"Granos de Café": 100, "Leche": 80, "Azúcar": 120, "Chocolate": 50})
i3 = Inventario({"Granos de Café": 90, "Leche": 70, "Azúcar": 110, "Chocolate": 45})
i4 = Inventario({"Granos de Café": 85, "Leche": 65, "Azúcar": 105, "Chocolate": 40})
i5 = Inventario({"Granos de Café": 75, "Leche": 60, "Azúcar": 95, "Chocolate": 35})
i6 = Inventario({"Granos de Café": 60, "Leche": 50, "Azúcar": 90, "Chocolate": 30})
i7 = Inventario({"Granos de Café": 55, "Leche": 45, "Azúcar": 80, "Chocolate": 25})
i8 = Inventario({"Granos de Café": 50, "Leche": 40, "Azúcar": 70, "Chocolate": 20})
i9 = Inventario({"Granos de Café": 45, "Leche": 35, "Azúcar": 60, "Chocolate": 18})
i10 = Inventario({"Granos de Café": 40, "Leche": 30, "Azúcar": 55, "Chocolate": 15})

while True:
    print("\n--SISTEMA DE MENÚ DE LA CAFETERÍA 'JUANITO ALCACHOFA'--\n")
    print("1. PERSONA")
    print("2. CLIENTE")
    print("3. EMPLEADO")
    print("4. PRODUCTOS BASE")
    print("5. BEBIDAS")
    print("6. POSTRES")
    print("7. COMPRAS")
    print("8. INVENTARIO")
    print("9. SALIR")

    x = int(input("\nSELECCIONA UNA CLASE PARA VER SUS OBJETOS Y MÉTODOS\n"))
    match x:
        case 1:
            print("\n--------PERSONA--------\n")
            print("\n¿Qué quieres hacer?\n")
            print("\n1.Ver OBJETOS\n")   
            print("\n2.Probar inicio de sesión\n")  
            print("\n3.Probar Actualizar Datos\n")  
            x1 = int(input())
            match x1:
                case 1:
                    print("\n--------VER OBJETOS--------\n")
                    p1.imprimir_objeto()
                    p2.imprimir_objeto()
                    p3.imprimir_objeto()
                    p4.imprimir_objeto()
                    p5.imprimir_objeto()
                    p6.imprimir_objeto()
                    p7.imprimir_objeto()
                    p8.imprimir_objeto()
                    p9.imprimir_objeto()
                    p10.imprimir_objeto()
                case 2:
                    print("\n-----USO DE INICIO DE SESIÓN----- \n")
                    p1.iniciar_sesion("leo@mail.com")
                case 3:
                    print("\n-----USO DE ACTUALIZAR DATOS----- \n")
                    print("\nUSUARIO ORIGINAL:\n")
                    p3.imprimir_objeto()
                    p3.actualizar_datos(1011, "Ricardo", "ricardo@mail.com")
                    print("\nNUEVOS DATOS DEL USUARIO:\n")
                    p3.imprimir_objeto()
                case _:
                    print("OPCIÓN NO VÁLIDA")
                    
        case 2:
            print("\n-------CLIENTE--------\n")
            print("\n¿Qué quieres hacer?\n")
            print("\n1.Ver OBJETOS\n")   
            print("\n2.REALIZAR COMPRA\n")  
            print("\n3.CONSULTAR HISTORIAL\n")  
            print("\n4.USAR PUNTOS\n")  
            x1 = int(input())
            match x1:
                case 1:
                    print("\n--------VER OBJETOS--------\n")
                    c1.imprimir_objeto()
                    c2.imprimir_objeto()
                    c3.imprimir_objeto()
                    c4.imprimir_objeto()
                    c5.imprimir_objeto()
                    c6.imprimir_objeto()
                    c7.imprimir_objeto()
                    c8.imprimir_objeto()
                    c9.imprimir_objeto()
                    c10.imprimir_objeto()
                case 2:
                    print("\n-----USO DE REALIZAR COMPRA---- \n")
                    c1.realizar_compra()  
                case 3:
                    print("\n-----USO DE CONSULTAR HISTORIAL-----\n ")
                    c1.consultar_historial()
                case 4:
                    print("\n-----USO DE USAR PUNTOS----- \n")
                    c3.usar_puntos()
                case _:
                    print("\nOPCIÓN NO VÁLIDA\n")
                    
        case 3:
            print("\n--------EMPLEADO--------\n")
            print("\n¿Qué quieres hacer?\n")
            print("\n1.Ver OBJETOS\n")   
            print("\n2.ACTUALIZAR INVENTARIO\n")  
            print("\n3.CAMBIAR ESTATUS\n")   
            x1 = int(input())
            match x1:
                case 1:
                    print("\n--------VER OBJETOS--------\n")
                    e1.imprimir_objeto()
                    e2.imprimir_objeto()
                    e3.imprimir_objeto()
                    e4.imprimir_objeto()
                    e5.imprimir_objeto()
                    e6.imprimir_objeto()
                    e7.imprimir_objeto()
                    e8.imprimir_objeto()
                    e9.imprimir_objeto()
                    e10.imprimir_objeto()
                case 2:
                    print("\n-----USO DE ACTUALIZAR INVENTARIO-----\n ")
                    e1.actualizar_inventario(2, "Leche", i1)
                case 3:
                    print("\n-----CAMBIAR ESTATUS-----\n ")
                    e1.cambiar_estatus(1)
                case _:
                    print("\nOPCIÓN NO VÁLIDA\n")
                    
        case 4:
            print("\n-------PRODUCTOS BASE--------\n")
            print("\n¿Qué quieres hacer?\n")
            print("\n1.Ver OBJETOS\n")   
            x1 = int(input())
            if x1 == 1:
                print("\n--------VER OBJETOS--------\n")
                bp1.imprimir_objeto()
                bp2.imprimir_objeto()
                bp3.imprimir_objeto()
                bp4.imprimir_objeto()
                bp5.imprimir_objeto()
                bp6.imprimir_objeto()
                bp7.imprimir_objeto()
                bp8.imprimir_objeto()
                bp9.imprimir_objeto()
                bp10.imprimir_objeto()    
                
        case 5:
            print("\n--------BEBIDAS-------\n")
            print("\n¿Qué quieres hacer?\n")
            print("\n1.Ver OBJETOS\n")   
            print("\n2.AÑADIR EXTRA\n")  
            print("\n3.CALCULAR PRECIO FINAL\n")  
            x1 = int(input())
            match x1:
                case 1:
                    print("\n--------VER OBJETOS------\n")
                    d1.imprimir_objeto()
                    d2.imprimir_objeto()
                    d3.imprimir_objeto()
                    d4.imprimir_objeto()
                    d5.imprimir_objeto()
                    d6.imprimir_objeto()
                    d7.imprimir_objeto()
                    d8.imprimir_objeto()
                    d9.imprimir_objeto()
                    d10.imprimir_objeto()
                case 2:
                    print("\n-----USO DE AÑADIR EXTRA---- \n")
                    d1.añadir_extra()
                case 3:
                    print("\n-----USO DE CALCULAR PRECIO FINAL-----\n ")
                    d1.calcular_precio_final()
                case _:
                    print("\nOPCIÓN NO VÁLIDA\n")
                    
        case 6:
            print("\n--------POSTRES-------\n")
            print("\n¿Qué quieres hacer?\n")
            print("\n1.Ver OBJETOS\n")   
            x1 = int(input())
            if x1 == 1:
                print("\n--------VER OBJETOS--------\n")
                ds1.imprimir_objeto()
                ds2.imprimir_objeto()
                ds3.imprimir_objeto()
                ds4.imprimir_objeto()
                ds5.imprimir_objeto()
                ds6.imprimir_objeto()
                ds7.imprimir_objeto()
                ds8.imprimir_objeto()
                ds9.imprimir_objeto()
                ds10.imprimir_objeto()
                
        case 7:
            print("\n--------COMPRA-------\n")
            print("\n¿Qué quieres hacer?\n")
            print("\n1.Ver OBJETOS\n")   
            print("\n2.CALCULAR TOTAL\n")  
            print("\n3.VERIFICAR STOCK\n")  
            x1 = int(input())
            match x1:
                case 1:
                    print("\n--------VER OBJETOS--------\n")
                    pp1.imprimir_objeto()
                    pp2.imprimir_objeto()
                    pp3.imprimir_objeto()
                    pp4.imprimir_objeto()
                    pp5.imprimir_objeto()
                    pp6.imprimir_objeto()
                    pp7.imprimir_objeto()
                    pp8.imprimir_objeto()
                    pp9.imprimir_objeto()
                    pp10.imprimir_objeto()
                case 2:
                    print("\n-----USO DE CALCULAR TOTAL----\n ")
                    pp1.calcular_total()
                case 3:
                    print("\n-----USO DE VERIFICAR STOCK-----\n ")
                    pp2.verificar_stock(i1, "Leche")
                case _:
                    print("OPCIÓN NO VÁLIDA")
                    
        case 8:
            print("\n--------INVENTARIO-------\n")
            print("\n¿Qué quieres hacer?\n")
            print("\n1.Ver OBJETOS\n")   
            print("\n2.REDUCIR STOCK\n")  
            print("\n3.NOTIFICAR SI NO HAY STOCK\n")  
            x1 = int(input())
            match x1:
                case 1:
                    print("\n--------VER OBJETOS--------\n")
                    i1.imprimir_objeto()
                    i2.imprimir_objeto()
                    i3.imprimir_objeto()
                    i4.imprimir_objeto()
                    i5.imprimir_objeto()
                    i6.imprimir_objeto()
                    i7.imprimir_objeto()
                    i8.imprimir_objeto()
                    i9.imprimir_objeto()
                    i10.imprimir_objeto()
                case 2:
                    print("\n-----USO DE REDUCIR STOCK---- \n")
                    i1.reducir_stock("Leche", 5)
                case 3:
                    print("\n-----NOTIFICAR SI NO HAY STOCK----- \n")
                    i1.notificar_sin_stock("Leche")
                case _:
                    print("\nOPCIÓN NO VÁLIDA\n")
                    
        case 9:
            print("\n¡GRACIAS POR HABER USADO NUESTRO PROGRAMA!\n")
            break
            
        case _:
            print("\nOPCIÓN NO VÁLIDA\n")