#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
  
  def add_item(self, title, price, quantity = 1):
    self.total = self.total + price * quantity
    for i in range(quantity):
      self.items.append(title)

    self.last_transaction = price * quantity

  def apply_discount(self):
    self.total = self.total - (self.total * (self.discount / 100))
    if(self.discount == 0):
      print("There is no discount to apply.")
    else:
     print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= self.last_transaction