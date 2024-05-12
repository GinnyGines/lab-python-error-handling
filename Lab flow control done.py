#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1
products_list = ["t-shirt", "mug", "hat", "book", "keychain"]

# Step 2
inventory = {}

# Step 3: Initialize inventory
for product in products_list:
    print("Amount of:", product)
    valor = input()
    inventory[product] = int(valor)
    print()

# Step 4: Define a function to get customer orders
def get_customer_orders():
    custom_orders = set()
    while True:
        product = input("Enter the name of the product you want to order: ")
        if product in products_list:
            custom_orders.add(product)
        else:
            print("No availability of product", product)
        choice = input("Do you want to add another product? (yes/no): ").lower()
        if choice == 'yes': # Changed comparison operator
            break
    return custom_orders

# Step 5: Get customer orders
custom_orders = get_customer_orders()

# Step 6: Display customer orders
print("Customer orders:", custom_orders)

# Step 7: Calculate order statistics
order_status = {
    "total_order": len(custom_orders),
    "percentage_products": (len(custom_orders) / len(products_list)) * 100
}

# Step 8: Display order statistics
print("Order statistics:")
print("Total Products Ordered:", order_status["total_order"])
print("Percentage of Products Ordered:", order_status["percentage_products"])

# Step 9: Update inventory based on customer orders
for product in custom_orders:
    inventory[product] -= 1

# Step 10: Display updated inventory
print("Updated Inventory:", inventory)


# In[ ]:




