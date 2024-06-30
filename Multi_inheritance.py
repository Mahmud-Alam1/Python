class MultiplicationTable: # parent
  def _init_(self,number):
       self.number=number
  
  def print_table(self) : 
    for i in range(1,11): # 11<11   i---> 1  11
      print(f"{self.number}*{i}={self.number*i}") #  24 *1=24
    print("------------------------------")

class Multilvel(MultiplicationTable):# child class
  def _init_(self, number):
    super()._init_(number)
  def print_table(self):
    print(f"multiplication table of{self.number}:")
    super().print_table()

table24=Multilvel(24)
table24.print_table()

table50=Multilvel(50)

table29=Multilvel(29)



table50.print_table()

table29.print_table()