from models import *

p1 = Person(1001, "John", "john@mail.com")
p2 = Person(1002, "Alice", "alice@mail.com")
p3 = Person(1003, "Bob", "bob@mail.com")
p4 = Person(1004, "Clara", "clara@mail.com")
p5 = Person(1005, "David", "david@mail.com")
p6 = Person(1006, "Emma", "emma@mail.com")
p7 = Person(1007, "Leo", "leo@mail.com")
p8 = Person(1008, "Nina", "nina@mail.com")
p9 = Person(1009, "Oscar", "oscar@mail.com")
p10 = Person(1010, "Paula", "paula@mail.com")


c1 = Customer("C001","Ana Lopez","ana@gmail.com",120,[])
c2 = Customer("C002","Luis Perez","luis@gmail.com",200,[])
c3 = Customer("C003","Maria Torres","maria@gmail.com",90,[])
c4 = Customer("C004","Carlos Diaz","carlos@gmail.com",300,[])
c5 = Customer("C005","Laura Ruiz","laura@gmail.com",50,[])
c6 = Customer("C006","Pedro Gomez","pedro@gmail.com",180,[])
c7 = Customer("C007","Sofia Ramirez","sofia@gmail.com",75,[])
c8 = Customer("C008","Miguel Castro","miguel@gmail.com",220,[])
c9 = Customer("C009","Valeria Ortiz","valeria@gmail.com",140,[])
c10 = Customer("C010","Daniel Vega","daniel@gmail.com",60,[])

e1 = Employee("P001","E001","Jorge Martinez","jorge@cafe.com","BARISTA")
e2 = Employee("P002","E002","Elena Sanchez","elena@cafe.com","SERVER")
e3 = Employee("P003","E003","Ricardo Flores","ricardo@cafe.com","MANAGER")
e4 = Employee("P004","E004","Patricia Luna","patricia@cafe.com","BARISTA")
e5 = Employee("P005","E005","Raul Mendoza","raul@cafe.com","SERVER")
e6 = Employee("P006","E006","Gabriela Soto","gabriela@cafe.com","BARISTA")
e7 = Employee("P007","E007","Fernando Rios","fernando@cafe.com","SERVER")
e8 = Employee("P008","E008","Diana Vargas","diana@cafe.com","MANAGER")
e9 = Employee("P009","E009","Andres Pineda","andres@cafe.com","BARISTA")
e10 = Employee("P010","E010","Lucia Herrera","lucia@cafe.com","SERVER")

bp1 = Base_product("BP001","Sandwich",55)
bp2 = Base_product("BP002","Bagel",40)
bp3 = Base_product("BP003","Croissant",45)
bp4 = Base_product("BP004","Granola Bar",25)
bp5 = Base_product("BP005","Yogurt Cup",35)
bp6 = Base_product("BP006","Fruit Bowl",50)
bp7 = Base_product("BP007","Energy Bar",30)
bp8 = Base_product("BP008","Toast",20)
bp9 = Base_product("BP009","Ham Sandwich",65)
bp10 = Base_product("BP010","Cheese Sandwich",60)

d1 = Drinking("D001","Espresso",40,"SMALL","HOT",[])
d2 = Drinking("D002","Latte",60,"MEDIUM","HOT",[])
d3 = Drinking("D003","Cappuccino",65,"MEDIUM","HOT",[])
d4 = Drinking("D004","Mocha",70,"LARGE","HOT",[])
d5 = Drinking("D005","Americano",50,"MEDIUM","HOT",[])
d6 = Drinking("D006","Cold Brew",75,"LARGE","COLD",[])
d7 = Drinking("D007","Iced Latte",70,"LARGE","COLD",[])
d8 = Drinking("D008","Caramel Macchiato",80,"LARGE","HOT",[])
d9 = Drinking("D009","Flat White",65,"MEDIUM","HOT",[])
d10 = Drinking("D010","Vanilla Latte",75,"LARGE","HOT",[])

ds1 = Dessert("DS001","Cheesecake",90,False,False)
ds2 = Dessert("DS002","Chocolate Cake",85,False,False)
ds3 = Dessert("DS003","Brownie",50,False,False)
ds4 = Dessert("DS004","Vegan Cookie",45,True,True)
ds5 = Dessert("DS005","Apple Pie",70,False,False)
ds6 = Dessert("DS006","Carrot Cake",80,False,False)
ds7 = Dessert("DS007","Gluten Free Muffin",55,False,True)
ds8 = Dessert("DS008","Tiramisu",95,False,False)
ds9 = Dessert("DS009","Cupcake",40,False,False)
ds10 = Dessert("DS010","Vegan Brownie",60,True,True)

pp1 = Purchase({"Espresso":2,"Brownie":1},"PENDING")
pp2 = Purchase({"Latte":1,"Cheesecake":1},"PENDING")
pp3 = Purchase({"Cappuccino":3},"PREPARING")
pp4 = Purchase({"Mocha":2,"Cupcake":2},"DELIVERED")
pp5 = Purchase({"Americano":1},"PENDING")
pp6 = Purchase({"Cold Brew":2,"Apple Pie":1},"PREPARING")
pp7 = Purchase({"Iced Latte":1},"DELIVERED")
pp8 = Purchase({"Caramel Macchiato":2},"PENDING")
pp9 = Purchase({"Flat White":1,"Brownie":2},"PREPARING")
pp10 = Purchase({"Vanilla Latte":3},"DELIVERED")

i1 = Inventory({
    "Coffee Beans":100,
    "Milk":80,
    "Sugar":120,
    "Chocolate":50,
    "Flour":60,
    "Eggs":90,
    "Butter":70,
    "Almond Milk":40
})
#The activity says that is neccessary to create 10 obejct of each class, but In the Inventory class, it's not the best choice to have more than one inventory
i2 = Inventory({
    "Coffee Beans":100,
    "Milk":80,
    "Sugar":120,
    "Chocolate":50
})

i3 = Inventory({
    "Coffee Beans":90,
    "Milk":70,
    "Sugar":110,
    "Chocolate":45
})

i4 = Inventory({
    "Coffee Beans":85,
    "Milk":65,
    "Sugar":105,
    "Chocolate":40
})

i5 = Inventory({
    "Coffee Beans":75,
    "Milk":60,
    "Sugar":95,
    "Chocolate":35
})

i6= Inventory({
    "Coffee Beans":60,
    "Milk":50,
    "Sugar":90,
    "Chocolate":30
})

i7 = Inventory({
    "Coffee Beans":55,
    "Milk":45,
    "Sugar":80,
    "Chocolate":25
})

i8 = Inventory({
    "Coffee Beans":50,
    "Milk":40,
    "Sugar":70,
    "Chocolate":20
})

i9 = Inventory({
    "Coffee Beans":45,
    "Milk":35,
    "Sugar":60,
    "Chocolate":18
})

i10 = Inventory({
    "Coffee Beans":40,
    "Milk":30,
    "Sugar":55,
    "Chocolate":15
})


while True:
    print("\n--MENU SYSTEM OF THE COFFEE STORE 'LOS GOMEZ'--\n")
    print("1.PERSON")
    print("2.CUSTOMER")
    print("3.EMPLOYEE")
    print("4.BASE PRODUCTS")
    print("5.DRINKINGS")
    print("6.DESSERTS")
    print("7.PURCHASES")
    print("8.INVENTORY")
    print("9.EXIT")

    x=int(input("\nSELECT A CLASS TO SEE ITS OBJECTS AND METHODS\n"))
    match x:
        case 1:
            print("\n--------PERSON--------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.Prove login\n")  
            print("\n3.Prove Update Data\n")  
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    p1.print_object()
                    p2.print_object()
                    p3.print_object()
                    p4.print_object()
                    p5.print_object()
                    p6.print_object()
                    p7.print_object()
                    p8.print_object()
                    p9.print_object()
                    p10.print_object()
                case 2:
                    print("\n-----USE OF LOGIN----- \n")
                    p1.login("john@mail.com")
                case 3:
                    print("\n-----USE OF UPDATE DATA----- \n")
                    print("\nUSER ORIGINAL:\n")
                    p3.print_object()
                    p3.update_data(1011, "Ricardo", "ricardo@mail.com")
                    print("\nNEW DATA OF THE USER:\n")
                    p3.print_object()
                case _:
                    print("OPTION NOT VALID")      
        case 2:
            print("\n-------CUSTOMER--------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.DO PURCHASE\n")  
            print("\n3.CONSULT HISTORY\n")  
            print("\n4.USE POINTS\n")  
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    c1.print_object()
                    c2.print_object()
                    c3.print_object()
                    c4.print_object()
                    c5.print_object()
                    c6.print_object()
                    c7.print_object()
                    c8.print_object()
                    c9.print_object()
                    c10.print_object()
                case 2:
                    print("\n-----USE OF DO PURCHASE---- \n")
                    c1.do_purchase()  
                case 3:
                    print("\n-----USE OF CONSULT HISTORY-----\n ")
                    c1.consult_History()
                case 4:
                    print("\n-----USE OF USE POINTS----- \n")
                    c3.use_points()
                case _:
                    print("\nOPTION NOT VALID\n")      
        case 3:
            print("\n--------EMPLOYEE--------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.UPDATE INVENTORY\n")  
            print("\n3.CHANGE STATUS\n")   
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    e1.print_object()
                    e2.print_object()
                    e3.print_object()
                    e4.print_object()
                    e5.print_object()
                    e6.print_object()
                    e7.print_object()
                    e8.print_object()
                    e9.print_object()
                    e10.print_object()
                case 2:
                    print("\n-----USE OF UPDATE INVENTORY-----\n ")
                    e1.update_Inventory(2,"Milk",i1)
                case 3:
                    print("\n-----CHANGE STATUS-----\n ")
                    e1.change_status(1)
                case _:
                    print("\nOPTION NOT VALID\n")      
        case 4:
            print("\n-------BASE PRODUCTS--------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    bp1.print_object()
                    bp2.print_object()
                    bp3.print_object()
                    bp4.print_object()
                    bp5.print_object()
                    bp6.print_object()
                    bp7.print_object()
                    bp8.print_object()
                    bp9.print_object()
                    bp10.print_object()    
        case 5:
                print("\n--------DRINKINGS-------\n")
                print("\nWhat do you want to do?\n")
                print("\n1.See OBJECTS\n")   
                print("\n2.ADD EXTRA\n")  
                print("\n3.CALCULATE FINAL PRICE\n")  
                x1=int(input())
                match x1:
                    case 1:
                        print("\n--------SEE OBJECTS------\n")
                        d1.print_object()
                        d2.print_object()
                        d3.print_object()
                        d4.print_object()
                        d5.print_object()
                        d6.print_object()
                        d7.print_object()
                        d8.print_object()
                        d9.print_object()
                        d10.print_object()
                    case 2:
                        print("\n-----USE OF ADD EXTRA---- \n")
                        d1.add_Extra()
                    case 3:
                        print("\n-----USE OF CALCULATE FINAL PRICE-----\n ")
                        d1.Calculate_Final_Price()
                    case _:
                        print("\nOPTION NOT VALID\n")    
        case 6:
            
            print("\n--------DESSERTS-------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    ds1.print_object()
                    ds2.print_object()
                    ds3.print_object()
                    ds4.print_object()
                    ds5.print_object()
                    ds6.print_object()
                    ds7.print_object()
                    ds8.print_object()
                    ds9.print_object()
                    ds10.print_object()
                case _:
                    print("\nOPTION NOT VALID\n")      

        case 7:
            print("\n--------PURCHASE-------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.CALCULATE TOTAL\n")  
            print("\n3.CHECK STOCK\n")  
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    pp1.print_object()
                    pp2.print_object()
                    pp3.print_object()
                    pp4.print_object()
                    pp5.print_object()
                    pp6.print_object()
                    pp7.print_object()
                    pp8.print_object()
                    pp9.print_object()
                    pp10.print_object()
                case 2:
                    print("\n-----USE OF CALCULATE TOTAL----\n ")
                    pp1.Calculate_total()
                case 3:
                    print("\n-----USE OF CHECK STOCK-----\n ")
                    pp2.Check_stock(i1,"Milk")
                case _:
                    print("OPTION NOT VALID")      
        case 8:
            print("\n--------INVENTORY-------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.REDUCE STOCK\n")  
            print("\n3.NOTIFY IF THE INVENTORY DOESN'T HAVE STOCK\n")  
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    i1.print_object()
                    i2.print_object()
                    i3.print_object()
                    i4.print_object()
                    i5.print_object()
                    i6.print_object()
                    i7.print_object()
                    i8.print_object()
                    i9.print_object()
                    i10.print_object()
                case 2:
                    print("\n-----USE OF REDUCE STOCK---- \n")
                    i1.reduce_Stock("Milk",5)
                case 3:
                    print("\n-----NOTIFY IF THE INVENTORY DOESN'T HAVE STOCK----- \n")
                    i1.notify_No_stock("Milk")
                case _:
                    print("\nOPTION NOT VALID\n")      
        case 9:
            print("\nTHANKS FOR HAVE USED OUR PROGRAM!\n")
            break
            

        case _:
            print("\nOPTION NOT VALID\n")        




