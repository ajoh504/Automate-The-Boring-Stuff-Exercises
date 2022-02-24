'''This function receives two arguments: a dictionary (inventory items and their quantity)
and a list (loot dropped by a dragon). The function updates the dictionary with all of 
the loot contained in the list, and returns the newly updated inventory'''

player_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby',]

def add_to_inventory(inventory: dict, added_items: list) -> dict:
  new_inventory = inventory # return this dictionary as updated inventory
  print(new_inventory)
  for i in added_items: 
    if i in new_inventory: # check if list items are in inventory dictionary
      new_inventory[i] += 1
    elif i not in new_inventory:
      new_inventory.setdefault(i, 0) # add new inventory item using setdefault()
      new_inventory[i] += 1
  print(new_inventory)

add_to_inventory(player_inventory, dragon_loot)
