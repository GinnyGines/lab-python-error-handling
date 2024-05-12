#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def initialize_inventory(products):
    inventory = {}
    for product in products:
        valid_quantity = False
        while not valid_quantity:
            try:
                quantity = int(input(f"Enter the quantity of {product}s available: "))
                if quantity < 0:
                    raise ValueError("Invalid quantity! Please enter a non-negative value.")
                valid_quantity = True
            except ValueError as error:
                print(f"Error: {error}")
        inventory[product] = quantity
    return inventory

def calculate_total_price(customer_orders):
    total_price = 0
    for product in customer_orders:
        valid_price = False
        while not valid_price:
            try:
                price = float(input(f"Enter the price of {product}: "))
                if price < 0:
                    raise ValueError("Invalid price! Please enter a non-negative value.")
                valid_price = True
            except ValueError as error:
                print(f"Error: {error}")
        total_price += price
    return total_price

def get_customer_orders(inventory):
    valid_orders = False
    while not valid_orders:
        try:
            number_of_orders = int(input("Enter the number of customer orders: "))
            if number_of_orders < 0:
                raise ValueError("Invalid number of orders! Please enter a non-negative value.")
            valid_orders = True
        except ValueError as error:
            print(f"Error: {error}")

    customer_orders = []
    for _ in range(number_of_orders):
        valid_product = False
        while not valid_product:
            product = input("Enter the name of a product that a customer wants to order: ")
            if product not in inventory:
                print("Error: Product not found in inventory. Please enter a valid product name.")
            elif inventory[product] == 0:
                print("Error: Product out of stock. Please enter a different product name.")
            else:
                valid_product = True
                customer_orders.append(product)
    return customer_orders

# Step 1: Initialize inventory with error handling
products_list = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = initialize_inventory(products_list)

# Step 2: Get customer orders with error handling
custom_orders = get_customer_orders(inventory)

# Step 3: Calculate total price of customer orders with error handling
total_price = calculate_total_price(custom_orders)

print("Total Price:", total_price)

