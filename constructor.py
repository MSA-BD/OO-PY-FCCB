#shudu matro class er constructor function __init__() e property/attribute initialize korle class er onno kuno method e sei property/attribute ke self diye access kora zay
#class theke create howya instance/object self argument er moddhye available hoy.

class Item:
    # class attributeses
    payRate=.8 # calculation 20% discount
    all=[]
    def __init__(self,name: str,price: float=100,quantity: int=0):
        #Run validation for constructor recieved arguments
        assert len(name)>=3, f"Product name need at last 3 letter!"
        assert price>=0,f"{price} can't be less than zero!"
        assert quantity>=0, f"{quantity} will be at least 1 or grater than!"
        #assign value for self object
        self.name=name
        self.price=price
        self.quantity=quantity
        # print(f"{name}, created in constructor method")

        #Action to execute
        Item.all.append(self)
        #self means every instance
    def calTotalPrice(self):
        return self.quantity*self.price
    def calDiscount(self):
        self.price=self.price*self.payRate
    def __repr__(self):
        return (f"(Item('{self.name},{self.quantity},{self.price}')),")


phone=Item("Phone",500,5)
laptop=Item("Laptop",1000,3)
cable=Item("Cable",465,3)
mouse=Item("Mouse",533,3)
keyboard=Item("Keyboard",465,3)
print(phone,laptop,cable,mouse,keyboard)
# __dict__ magic attriutes use korle class attribute insatance level e available hoy na

#calculate phone discount price with diffrent payRate
# phone.payRate=0.7
# phone.calTotalPrice()
# phone.calDiscount()
# print(phone.price)

#calculate laptop discount price with another payRate
# laptop.payRate=0.6
# laptop.calTotalPrice()
# laptop.calDiscount()
# print(laptop.price)

# print 5 instances
for instance in Item.all:
    pass
    # print(instance.name)



#__str__ vs __repr__



