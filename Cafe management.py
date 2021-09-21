menu = {"Burger": 50, "Cold Coffee": 25, "Pizza": 100, "Tea": 10, "Hot Coffee": 10, "French Fries": 30}
ol = []


class Customer:
    def detail(self, name, total_people, bill):
        self.name = name
        self.ppl = total_people
        self.bill = bill
        if bill > 0 and self.ppl == 1:
            print(self.name, "your bill for", self.ppl, "person is", str(bill) + "₹")
        elif bill > 0 and self.ppl > 1:
            print(self.name, "your bill for", self.ppl, "person is", str(bill) + "₹")
        else:
            print("You have not ordered anything.")


def menuDisplay():
    global menu
    print("Menu:(Item name: Cost)\n", menu)
    print()


def refine(unrefinedOrderList):
    for i in range(len(unrefinedOrderList)):
        tempobj = unrefinedOrderList[i]
        if tempobj[0].isspace():
            unrefinedOrderList[i] = tempobj[1:]
        
        b = " "
        if b in unrefinedOrderList[i]:
            temp = unrefinedOrderList[i].split()
            for j in range(len(temp)):
                temp[j] = temp[j].capitalize()
            s = b.join(temp)
            unrefinedOrderList[i] = s
        
        else:
            unrefinedOrderList[i] = unrefinedOrderList[i].capitalize()
    
    return unrefinedOrderList


def getOrder():
    global ol
    ch = 'y'
    print("For ordering more than one item separate each item with a coma(,)")
    
    while ch == 'y':
        s = input("Place your order:")
        ol = s.split(sep=",")
        ch = input("Do you want to order more items?(y/n):")
    ol = refine(ol)
    
    return ol


def displayOrder(order):
    actual = []
    notlist = set()
    
    for x in order:
        if x in menu:
            actual.append(x)
        
        else:
            notlist.add(x)
    print("Your order list:\n", actual)
    
    if notlist:
        print(notlist, "is not present in the menu")
        print("Please order something for the given menu")
    
    return actual


def bill(o):
    global menu
    total = 0
    cl = []
    tol = set(o)
    
    for obj in tol:
        count = 0
        for objct in o:
            if obj == objct:
                count += 1
        cl.append(count)
    endol = list(zip(tol, cl))
    
    for i in range(len(o)):
        total = total + menu[o[i]]
    
    try:
        if endol[0]:
            print("Items you ordered and their quantity:\n", endol)
            return total
    except:
        return total


sit_size = 20
order = []
gOrder = []
print("Welcome to the cafe")
name = input("Enter your name:")
ppl = int(input("For how many people do you want to book seats?:"))
print()

if ppl > sit_size:
    print("Sorry " + name + " we do not have enough space")
    print("There are", ppl - sit_size, "people more than the cafe can accommodate.")

else:
    sit_size = sit_size - ppl
    print("Enter the number to corresponding to use the menu.")
    end = False
    while not end:
        inp = int(input("1.Show Food Menu\n2.Place Order\n3.Order List\n99.Exit And Display Bill\n"))
        print()
        
        if inp == 1:
            menuDisplay()
        
        elif inp == 2:
            gOrder = getOrder()
            order = order + gOrder
        
        elif inp == 3:
            order = displayOrder(order)
        
        elif inp == 99:
            order = displayOrder(order)
            end = True
        
        else:
            print("Please enter a valid choice.\n")
    
    total = bill(order)
    c = Customer()
    c.detail(name, ppl, total)

print("Thank you")
