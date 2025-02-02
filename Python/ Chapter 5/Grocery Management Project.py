inventory = {'milk','bread','eggs','butter'}
# Add
inventory.add("Cheese")
inventory.add("fruit")
# Remove
inventory.remove("butter")
#Check if a specify item is in inventory
item_to_check = 'eggs'
if item_to_check in inventory:
    print(f"{item_to_check} is available")
else:
    print(f"{item_to_check} is not available ")

# List of item are out of stocks and need to be removed
out_of_stock = {"cheese","fruit"}
inventory.difference_update(out_of_stock)

# Creating a New Set for items sale
sale_items = {"bread","Milk","juice"}
# to combine in inventory sale items
complete_list = inventory.union(sale_items)
print(f"Complete list of items in store and on sale",complete_list)

# Creating a set for items available in store but not on sale
exclusive_store_items = inventory.difference(sale_items)
print(f"Items Exclusive in Store",exclusive_store_items)

# checking the inventory is subset of complete list
issub = inventory.issubset(complete_list)
print(f"store inventory is a subset of the complete list",issub)

# Clear inventory
inventory.clear()
print("Shop Is closed",inventory)



