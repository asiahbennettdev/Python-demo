# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Grapes', 'Bannna', 'Starfruit', 'Orange', 'Pineapple')

# Using a constructor
# fruits2 = tuple(('Grapes', 'Bannna', 'Starfruit', 'Orange', 'Pineapple'))


# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pear'

# Delete tuple
del fruits2

# Get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)


