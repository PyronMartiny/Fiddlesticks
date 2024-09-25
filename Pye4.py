inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 23, 43]


for index, inventory_tuple in enumerate(zip(inventory_names,inventory_numbers)):
 
    print(f'{inventory_tuple[0]} [id: {index} - inventory: {inventory_tuple[1]}') 