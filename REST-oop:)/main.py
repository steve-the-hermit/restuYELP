from Customer import Customer
from Restaurant import Restaurant
from Review import Review


customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Burger Palace")
restaurant2 = Restaurant("Pizza Hut")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant2, 5)

print(customer1.full_name())  # John Doe
print(restaurant1.average_star_rating())  # 4.0

# ...

if __name__ == "__main__":
    # Test cases and operations
    pass
