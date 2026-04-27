class cart:
     
    def __init__(self):
        self.iteam={}
        self.price={"Book":50,"pen":10} 
            
    def add_iteam(self,iteramss,quality):   
        self.iteam[iteramss]=quality
        
    def remove(self,iteramss):
        del self.iteam[iteramss]
        
    def updated(self,iteramss,update):
        self.iteam[iteramss]=update
    
    def add_iteams(self):
        total=0 
        for i,j in self.iteam.items():
            total+=j*self.price[i]
        return total
    
    def get(self):
        cart_itram=[]
        for i in self.iteam.keys():
            cart_itram.append(i)
        return cart_itram

class_cart=cart()
class_cart.add_iteam("Book",3)
class_cart.add_iteam("pen",5)
print(class_cart.iteam)
print(class_cart.get())
print(class_cart.add_iteams())
