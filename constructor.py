#shudu matro class er constructor function __init__() e property/attribute initialize korle class er onno kuno method e sei property/attribute ke self diye access kora zay
#class theke create howya instance/object self argument er moddhye available hoy.

class Item:
    # class attributeses
    payRate=.8 # cal 20% discount
    def __init__(self,name: str,price: float=100,quantity: int=0):
        #Run validation for constructor recieved arguments
        assert len(name)>=3, f"Product name need at last 3 letter!"
        assert price>=0,f"{price} can't be less than zero!"
        assert quantity>=0, f"{quantity} will be at least 1 or grater than!"
        #assign value for self object
        self.name=name
        self.price=price
        self.quantity=quantity
        print(f"{name}, created in constructor method")
    def calTotalPrice(self):
        return self.quantity*self.price
    def calDiscount(self):
        self.price=self.price*Item.payRate
phone=Item("Phone",300,5)
laptop=Item("Laptop",500,3)
# __dict__ magic attriutes use korle class attribute insatance level e vailable hoy na
phone.calTotalPrice()
phone.calDiscount()
# print(phone.price) //after 20% discount 240
