# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'Asiah',
    'last_name': 'Doe',
    'age': 28
}

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Jameeka', 'age': 25},
    {'name': 'Kareem', 'age': 35},
    {'name': 'Bennie', 'age': 20},
    {'name': 'Suprano', 'age': 27}
]

print(people)
print(people[3]['name'])
print(people[0]['age'])
