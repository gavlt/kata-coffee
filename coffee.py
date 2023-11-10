"""
Design a loyalty program for a coffee shop. Customers collect one stamp
per coffee; when they reach six stamps, they have one free coffee.
The application exposes the following public operations.

The Rules:
 - I've provided some types but please change them!
 - There are some provided rules for this challenge which was originally in Java. I've adapted them to Python but not tested them. We can flex if it is too hard, even that will be an interesting outcome.
   - Logic Classes (i.e. not dataclasses) can have a maximum of 2 fields
     and 4 methods.
   - Method bodies have a maximum of 3 lines of code, no tricky code
     to get around this.
"""

from typing import Dict

class NotEnoughStampsError(Exception):
  pass

class CustomerAlreadyExistsError(Exception):
  pass

class NoSuchCustomerError(Exception):
  pass

class CoffeeShop:
  customer_stamps: Dict[str, int]

  def __init__(self):
    self.customer_stamps = {}

  def create_customer(self, id: str) -> None:
    if id in self.customer_stamps:
      raise CustomerAlreadyExistsError()
    self.customer_stamps[id] = 0

  def create_stamp_by_customer(self, id: str) -> None:
    if id not in self.customer_stamps:
      raise NoSuchCustomerError()
    self.customer_stamps[id] += 1

  def count_stamps_by_customer(self, id: str) -> int:
    if id not in self.customer_stamps:
        raise NoSuchCustomerError()
    return self.customer_stamps[id]

  def redeem_free_coffee_for_customer(self, id: str) -> None:
    if self.customer_stamps[id] < 6:
      raise NotEnoughStampsError()
    self.customer_stamps[id] -= 6
