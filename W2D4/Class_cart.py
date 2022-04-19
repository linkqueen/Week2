# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    
    def __init__(self):
        self.cart = {}
        
    def add_cart(self,item):
        if item not in self.cart:
            quantity = int(input('How many would you like?'))
            print((f'{quantity} {item} added to your car')) #not printing
            self.cart[item]=quantity
            print((f'{quantity} {item} added to your car'))
        else:
            more =int(input('how many more?'))
            n = self.cart[item] + more
            print((f'{more} more {item} added to your car')) #not printing
            self.cart.update({item:n})
            
              
    def delete_cart(self,delete):
        if delete in self.cart:
            remove = int(input('How many would you like to remove?'))
            item = self.cart[delete] - remove
            self.cart[delete]= item
            print(f'{remove} {delete} removed from your cart.')
        if not self.cart:
            print('Item is not in cart. Would you like to add?')
        
    def show_cart(self):
            for item in self.cart:
                print(f'Your cart contains:{self.cart}')
                break
            if not self.cart:
                print('your cart is empty')
    def clear_cart(self):
        self.cart.clear()
        print('Your cart is empty.')
    
class UI():
    
    def __init__(self,person):
        self.person = person
        
    def live_shopping(self):
        while True:
            response = input("Do you want to : Show/Add/Delete/Clear or Quit?")
            if response.lower().strip() == "quit":
                self.person.showshow_cart()
                print('Thank you for shopping at Learn Python')
                break
               
            elif response.lower().strip() == "show":
                self.person.show_cart()
                
            elif response.lower().strip() == "add":
                add =input('What would you like to add?') 
                self.person.add_cart(add)
               
            elif response.lower().strip() == "delete":
                delete =input('Which item would you like to delete?')
                self.person.delete_cart(delete)
               
            elif response.lower().strip() == "clear":
                self.person.clear_cart()
            else:
                print('There\'s nothing in your cart')

               

#Driver Code
target = Cart()
ui = UI(target)
ui.live_shopping()
target.cart()