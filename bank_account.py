class Car(object):
    
 def _init_(self,model,color, company, speed_limit):
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.model = model
    
 def start(self):
   print("started") 

 def stop(self):
   print("stopped")

 def accelarate(self):
   print("accelarating....")
   "accelarator functionality here"

 def change_gear(self,gear_type):
   print("gear changed")
   "gear related functionaly here"

audi = Car("A6","red","audi",80)
lamborgini = Car("F69","gold", "lamborgini",67.3)
print(audi.start())