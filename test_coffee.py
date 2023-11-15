import pytest
import coffee
import datetime

def test_create_customer__creates_customer_with_no_stamps():
  coffee_shop = coffee.CoffeeShop()
  coffee_shop.create_customer("foo")
  assert coffee_shop.count_stamps_by_customer("foo") == 0
  
def test_create_customer__creates_customer_with_one_stamp():
  coffee_shop = coffee.CoffeeShop()
  coffee_shop.create_customer("foo")
  coffee_shop.create_stamp_by_customer("foo")
  assert coffee_shop.count_stamps_by_customer("foo") == 1

def test_count_stamps_by_customer__non_existent_customer():
  coffee_shop = coffee.CoffeeShop()
  with pytest.raises(coffee.NoSuchCustomerError):
    coffee_shop.count_stamps_by_customer("foo")

def test_create_stamp_by_customer__non_existent_customer():
  coffee_shop = coffee.CoffeeShop()
  with pytest.raises(coffee.NoSuchCustomerError):
    coffee_shop.create_stamp_by_customer("foo")

def test_redeem_free_coffee_for_customer():
  coffee_shop = coffee.CoffeeShop()
  coffee_shop.create_customer("foo")
  for _ in range(6):
    coffee_shop.create_stamp_by_customer("foo")
  coffee_shop.redeem_free_coffee_for_customer("foo")
  assert coffee_shop.count_stamps_by_customer("foo") == 0

def test_redeem_free_coffee_for_customer_with_stamps_left():
  coffee_shop = coffee.CoffeeShop()
  coffee_shop.create_customer("foo")
  for _ in range(15):
    coffee_shop.create_stamp_by_customer("foo")
  coffee_shop.redeem_free_coffee_for_customer("foo")
  assert coffee_shop.count_stamps_by_customer("foo") == 9

def test_redeem_free_coffee_not_enough_stamps():
  coffee_shop = coffee.CoffeeShop()
  coffee_shop.create_customer("foo")
  with pytest.raises(coffee.NotEnoughStampsError):
    coffee_shop.redeem_free_coffee_for_customer("foo")

def test_create_customer__existing_raises_exception():
  coffee_shop = coffee.CoffeeShop()
  coffee_shop.create_customer("foo")
  with pytest.raises(coffee.CustomerAlreadyExistsError):
    coffee_shop.create_customer("foo")

def test_redeem_free_coffee_for_customer_with_expiry():
  coffee_shop = coffee.CoffeeShop()
  coffee_shop.create_customer("foo")
  for _ in range(6):
    coffee_shop.create_stamp_by_customer("foo", date=datetime.date(2023, 1, 1))
  with pytest.raises(coffee.NotEnoughStampsError):
    coffee_shop.redeem_free_coffee_for_customer("foo", date=datetime.date(2023, 2, 1))
  assert coffee_shop.count_stamps_by_customer("foo", date=datetime.date(2023, 1, 1)) == 6
  assert coffee_shop.count_stamps_by_customer("foo", date=datetime.date(2023, 1, 30)) == 6
  assert coffee_shop.count_stamps_by_customer("foo", date=datetime.date(2023, 2, 1)) == 0

def test_redeem_free_coffee_redeem_correct_stamps_with_expiry():
  coffee_shop = coffee.CoffeeShop()
  coffee_shop.create_customer("foo")
  for _ in range(2):
    coffee_shop.create_stamp_by_customer("foo", date=datetime.date(2023, 1, 1))
  for _ in range(6):
    coffee_shop.create_stamp_by_customer("foo", date=datetime.date(2023, 2, 1))
  coffee_shop.redeem_free_coffee_for_customer("foo", date=datetime.date(2023, 2, 2))
  assert coffee_shop.count_stamps_by_customer("foo", date=datetime.date(2023, 2, 2)) == 0
