class Person():
    def __init__(self,id_person,name,email):
        self.name=name
        self.email=email
        self.id_person=id_person
    def login(self,email):
        if self.email==email:
            print(f"\nWelcome {self.name} to our online system\n")
        else:
             print(f"\nYour email is incorrect or you did not register yet\n")
    def update_data(self,id_person,name,email):
        self.name=name
        self.email=email
        self.id_person=id_person
        print(f"\nThe data was updated succesfully\n")
    def print_object(self):
        print(f"\nID:{self.id_person}\t|\t{self.name}\t|\t{self.email}\t\n")
class Customer(Person):
    list_cus=[]
    def __init__(self,id_person,name,email,Fidelity_points,Purchase_History):
       super().__init__(id_person,name,email)
       self.Fidelity_points=Fidelity_points
       self.Purchase_History=Purchase_History
       Customer.list_cus.append(self)
    def do_purchase(self):
        print(f"\nStarting Purchase process..\n")
        print(f"\nCustomer:{self.name} (Points:{self.Fidelity_points})")
        print(f"\nWhat do you can to buy?\n")
        list_pp={}
        while True:
            print(f"\nSelect one of the following options:\n")
            print(f"\n1.Drinkings\n")
            print(f"\n2.Desserts\n")
            print(f"\n3.That's all\n")
            x=int(input("\n"))
            
            match x:
                case 1:
                    print("\nThe available drinkings are:\n")
                    for drink in Drinking.list:
                        drink.print_object()
                    x1=int(input("How many different types of products do you want?"))
                    for i in range(x1):
                        list_pp[i]=0
                        print("Enter the name of the product")
                        name_=input("\n")
                        z=int(input("How many?"))
                        if name_ in list_pp:#check if the id_ already exist
                            list_pp[name_]+=z
                            del list_pp[i]#deletes the unnecesary item
                        else:
                            list_pp[name_]=list_pp.pop(i)#change the key and deletes it
                            list_pp[name_]=z
                case 2:
                    print("\nThe available desserts are:\n")
                    for dessert in Dessert.list:
                        dessert.print_object()
                    x11=int(input("How many different types of products do you want?"))
                    for i in range(x11):
                        list_pp[i]=0
                        print("Enter the name of the product")
                        name_1=input("\n")
                        z1=int(input("How many?"))
                        if name_1 in list_pp:#check if the id_ already exist
                            list_pp[name_1]+=z1
                            del list_pp[i]#deletes the unnecesary item
                        else:
                            list_pp[name_1]=list_pp.pop(i)#change the key and deletes it
                            list_pp[name_1]=z1
                case 3:
                    print("Thanks for your purchase")
                    break                 
        Purchase_=Purchase(list_pp,"WITHOUT PAY")
        Purchase_.Calculate_total()
        self.Purchase_History.append(Purchase_)
        print("\nVISUALIZE PURCHASE\n")
        Purchase_.print_object()
        list_pp.clear()                
    def print_object(self):
        print(f"\nID:{self.id_person}\t|\t{self.name}\t|\t{self.email}\t|\tPOINTS:{self.Fidelity_points}\t\n")
    def consult_History(self):
        print(f"\nThe current purchases are:\n")
        for p in self.Purchase_History:
            p.print_object()
    def use_points(self):
        print(f"\nSearching customer with ID: {self.id_person}\n")
        if(self.Fidelity_points>=160):
                    print(f"You can get a free coffee!")
        else:
                    print(f"You need more points....")
class Employee(Person):
     def __init__(self,id_person,id_employee,name,email,Rol):
       super().__init__(id_person,name,email)
       self.Rol=Rol
       self.id_employee=id_employee
     def update_Inventory(self,numb,product,inve):
       print(f"Inventory before the Update of {numb} {product}:")
       inve.print_object()
       for keys,p in inve.ingredients.items():
           if keys==product:
                inve.ingredients[keys]=numb
       print("The inventory was changed")
       inve.print_object()
     def change_status(self,id_Purchase_):
         for c in Purchase.list_Purchases:
             if(c.id_Purchase==id_Purchase_):
                 t=input("Introduce the new status for this purchase")
                 c.status=t
                 print("Your change was submitted:")
                 c.print_object()
     def print_object(self):
        print(f"\nID:{self.id_person}\t|\t{self.name}\t|\t{self.email}\t|\tID_EMPLOYEE:{self.id_employee}\t|\tROL:{self.Rol}\t\n")
class Base_product():
    list_products=[]
    def __init__(self,id_product,name,base_price):
        self.name=name
        self.id_product=id_product
        self.base_price=base_price
    def print_object(self):
        print(f"\nID:{self.id_product}\t|\t{self.name}\t|\tBASE PRICE: {self.base_price}\t\n")
class Drinking(Base_product):
    list=[]
    list_general_modifiers={"Almond Milk":50,"Oat Milk":40,"Soy Milk":20,"Extra Sugar":10,"Extra ice":80}
    def __init__(self,id_product,name,base_price,size,temperature,modifiers):
       super().__init__(id_product,name,base_price)
       self.size=size
       self.temperature=temperature
       self.modifiers=modifiers
       Base_product.list_products.append(self)
       Drinking.list.append(self)
    def add_Extra(self):
        print(f"Do You want to add some modifiers to your drinking?")
        t=input()
        if(t=="Yes"):
                f=int(input("How many?"))
                for i in range(f):
                    print("The avaialable modifiers are")
                    for mod,value in Drinking.list_general_modifiers.items():
                        print(f"-{mod}|\t-${value}\n")
                    g=input("Select one")
                    self.modifiers.append(g)
                print("You have selected all your extras!")
                for g in self.modifiers:
                    print(f"Modifier:{g}")
        else:
            print("Dont worry!, the taste is going to be delicious even if it doesn't have extras")
    def Calculate_Final_Price(self):
        print(f"Your initial price is {self.base_price}\n")
        for g in self.modifiers:
            for mod,value in Drinking.list_general_modifiers.items():
                            if g==mod:
                                self.base_price+=value
        if(len(self.modifiers)!=0):
            print("You selected extras")
            for g in self.modifiers:
                    print(f"Modifier:{g}\n")
            print(f"All Your extras were added, your new price is {self.base_price}")
        else:
            print("Your price continues being the same, beacuse you don't selected extras")
    def print_object(self):
        print(f"\nID:{self.id_product}  | {self.name} | BASE PRICE: {self.base_price} | SIZE:{self.size} | TEMPERATURE: {self.temperature}  | MODIFIERS :{self.modifiers} \n")
class Dessert(Base_product):
  list=[]
  def __init__(self,id_product,name,base_price,isVegan,Without_Gluten):
       super().__init__(id_product,name,base_price)
       self.isVegan=isVegan
       self.Without_Gluten=Without_Gluten
       Base_product.list_products.append(self)
       Dessert.list.append(self)
  def print_object(self):
         print(f"\nID:{self.id_product}  | {self.name} | BASE PRICE: {self.base_price} | IS VEGAN?:{self.isVegan} | DOESN'T IT HAVE GLUTEN?: {self.Without_Gluten}\n")
class Purchase():
    counter=0
    list_Purchases=[]
    def __init__(self,products,status):
        Purchase.counter+=1
        self.products=products
        self.status=status
        self.total=0
        self.id_Purchase=Purchase.counter
        Purchase.list_Purchases.append(self)
    def Calculate_total(self):
       for p in self.products:
           for t in Base_product.list_products:
               if p==t.name:
                    self.total+=(self.products[p]*(t.base_price))
       print(f"Your final total is {self.total}")
       return self.total
    def Check_stock(self,inve,ingg):
        if inve.ingredients[ingg]<=0:
                print("There isn't enough ingredients")
                return False
        else:    
            print("Everything is good")
            return True
    def print_object(self):
        if self.total==0:
            for p in self.products:
                for t in Base_product.list_products:
                    if p==t.name:
                        self.total+=(self.products[p]*(t.base_price))
        print(f"\nPRODUCTS:")
        for p,k in self.products.items():
            print(f"PRODUCT {p} : {k} ")
        print(f"STATUS {self.status} \t|\tTOTAL: {self.total}\t \n")
class Inventory():
    def __init__(self,ingredients):
        self.ingredients=ingredients
    def reduce_Stock(self,ing,amount):
        print(f"Inventory before the reduction of {amount} {ing}:")
        self.print_object()
        for l,p in self.ingredients.items():
             if l==ing:
                 self.ingredients[l]-=amount
        print(f"Your stock was changed")
        self.print_object()
    def notify_No_stock(self,ingg):
            if self.ingredients[ingg]==0:
                print(f"There isn't stock in {ingg}")
            else:
                 print(f"There is still stock in {ingg}")
    def print_object(self):
         for l,p in self.ingredients.items():
            print(f"INGREDIENT:{l}-{self.ingredients[l]}\t")

         print("\n")
