'''
Leran OOP-Python from freeCodeCamp.org youtube video for beginner
https://github.com/MSA-BD/OO-PY-FCCB.git
'''
print("Learn OOP Python from FCC")
randomString=str('5')
# print(randomString,type(randomString))
#       5, <class 'str'>
'''
ekhane str class theke randomString name instance create kora hoyeche. 
str,int python er built-in class.
randomString instance er type hocce <class 'str'>
'''
# real worl example

class Item:
    def calTotalPrice(self,x,y):
        '''
        return self.price*self*quantity kora zabe na. ekhane item1 self argument er moddhye takleo self. diye property/attribute name, quantity and price access kora zabe na
         karon class Item er magicMethod __init__() e property gulu class er jonno initialize kora hoy ni. ejonno ei property/attribute class method e self. diye access kora zabe na.      '''
        return x*y
item1=Item()
item1.name='Phone'
item1.price=300
item1.quantity=5
totalPrice=item1.calTotalPrice(item1.price,item1.quantity)
# name, price , quantity eguluke attribute bola hoy
# print(totalPrice) //1500
# print(type(item1)) //<class __main__.Item>