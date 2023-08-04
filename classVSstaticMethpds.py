import csv
class Item:
    # class attributeses
    payRate=.8 # calculation 20% discount
    all=[]
    def __init__(self,name: str,price: float=100,quantity: int=0):

        #Run validation for constructor recieved arguments
        assert len(name)>=3, f"Product name need at last 3 letter!"
        assert price>=0,f"{price} can't be less than zero!"
        assert quantity>=0, f"{quantity} will be at least 1 or grater than and can't a fraction!"

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

    @classmethod
    def instantiateFromCSV(cls):
        with open("itemm.csv","r") as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    def __repr__(self):
        return f"Item('{self.name}',{self.quantity},{self.price})"
    @staticmethod
    def isInteger(num):

        #We will count the floats that are zero like (10.0, 5.0)
        if isinstance(num, float):

            #countout the floats that are zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


Item.instantiateFromCSV()
Item.isInteger(7.6) # False 7.0 True 9 True



