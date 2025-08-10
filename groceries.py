# Ask user to enter groceries as a comma-separated string
print('Please Enter the Groceries you bought (comma-separated):')
N = input("")

# Convert the string into a list, remove extra spaces, and normalize all items to lowercase
converting_list = [item.strip().lower() for item in N.split(',')]

# Show the initial groceries list
print('The Groceries you bought are:', converting_list)

# Ask if the user wants to add any items
YesOrNo = input('Do you want to add an item? (Yes or No): ').lower()

# If user says yes, get extra items and add them to the list
if YesOrNo == 'yes':
    Extra_items = input('Enter the item(s) to add (comma-separated): ')
    converting_list += [item.strip().lower() for item in Extra_items.split(',')]
    print('Item(s) added.')
else:
    print('No items added.')

# Ask if the user wants to remove any items
removingg = input('Do you want to remove any items? (Yes or No): ').lower()

# If user says yes, remove the specified item if it exists
if removingg == 'yes':
    Remove_items = input('Enter the item to remove: ').strip().lower()
    if Remove_items in converting_list:
        converting_list.remove(Remove_items)
        print('Item removed.')
    else:
        print('Item not found.')

# Show the final grocery list
print('Final list:', converting_list)

# Also show the list as a tuple (immutable version)
print('As tuple:', tuple(converting_list))
