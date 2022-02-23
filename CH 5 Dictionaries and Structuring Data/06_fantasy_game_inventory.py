# This function accepts a dictionary as an argument, and outputs the player's inventory
# items, the quantity for each item, and the total quanity of items. 

player_inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

def display_inventory(inventory: dict) -> str:
  print('Inventory:')
  item_total = 0 # accumulator for counting all items
  for k, v in inventory.items(): # loop through dictionary keys and values
    print(str(v) + ' ' + k) # empty space for readability when printing inventory items
    item_total += v
  print('Total number of items: '+ str(item_total))

display_inventory(player_inventory)
