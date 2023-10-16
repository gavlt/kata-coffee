"""
Design a loyalty program for a coffee shop. Customers collect one stamp per coffee; when they reach six stamps, they have one free coffee. The application exposes the following public operations.

The Rules:
 - I've provided some types but please change them!
 - There are some provided rules for this challenge which was originally in Java. I've adapted them to Python but not tested them. We can flex if it is too hard, even that will be an interesting outcome.
   - Logic Classes (i.e. not dataclasses) can have a maximum of 2 fields and 4 methods.
   - Method bodies have a maximum of 3 lines of code, no tricky code to get around this.
"""

class CoffeeShop:
  def create_customer(id: str):
    pass

  def create_stamp_by_customer(id: str):
    pass

  def list_stamps_and_coffees_by_customer(id: str) -> (int, int):
    pass

  def redeem_free_coffee_for_customer(id: str):
    pass

