# Strings in python are surrounded by wither single or double quotation marks. Let's look at string formatting and some stringn methods


name = 'Asiah'
age = 28 

# Concatenate 
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')


# String Methods

s = 'hello world'

# Capitalize string 
print(s.capitalize())

