#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def initialize_inventory(products):
    inventory = {}
    for product in products:
        print("Amount of:", product)
        valor = input()
        inventory[product] = int(valor)
        print()
    return inventory

def get_customer_orders():
    custom_orders = set()
    while True:
        product = input("Enter the name of the product you want to order: ")
        if product in products_list:
            custom_orders.add(product)
        else:
            print("No availability of product", product)
        choice = input("Do you want to add another product? (yes/no): ").lower()
        if choice == 'no': # Fixed comparison operator
            break
    return custom_orders

def update_inventory(customer_orders, inventory):
    for product in customer_orders:
        inventory[product] -= 1
    return inventory

def calculate_order_statistics(customer_orders, products):
    order_status = {
        "total_order": len(customer_orders),
        "percentage_products": (len(customer_orders) / len(products)) * 100
    }
    return order_status

def print_order_statistics(order_statistics):
    print("Order statistics:")
    print("Total Products Ordered:", order_statistics["total_order"])
    print("Percentage of Products Ordered:", order_statistics["percentage_products"])

def print_updated_inventory(inventory):
    print("Updated Inventory:", inventory)

# Step 1
products_list = ["t-shirt", "mug", "hat", "book", "keychain"]

# Step 2
inventory = initialize_inventory(products_list)

# Step 3: Get customer orders
custom_orders = get_customer_orders()

# Step 4: Update inventory based on customer orders
inventory = update_inventory(custom_orders, inventory)

# Step 5: Calculate order statistics
order_status = calculate_order_statistics(custom_orders, products_list)

# Step 6: Display order statistics
print_order_statistics(order_status)

# Step 7: Display updated inventory
print_updated_inventory(inventory)

