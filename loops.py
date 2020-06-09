# Create a list
# numbers = [1,2,3,4,5]
fruits = ['Apples', 'Orange', 'Bannana', 'Kiwi', 'Grapes']
#  Use a constructor 
# numbers2 = list((1,2,3,4,5))

#  Get a value
print(fruits[1])

# Append to list 
fruits.append('Mangos')

# Remove from list 
fruits.remove('Kiwi')

# Insert into position
fruits.insert(2, 'Strawberries')

# Reverse the list
fruits.reverse()

# Sort list 
fruits.sort()

# Remove with pop
fruits.pop(4)

# Reverse sort 
fruits.sort(reverse=True)

# Change value 
fruits[0] = 'Blueberries'

print(fruits)
