import pytest
import coffee

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

def test_redeem_free_coffee_for_customer():
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
