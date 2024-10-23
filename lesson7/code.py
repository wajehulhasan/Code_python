#   the syntax of the function

'''
def function_name (parameters):
    # function body
    return value

'''

# BASIC FUNCTION

def greet ():
    print('Hello World')

greet()

# FUNCTION WITH PARAMETERS
def greet(name):
    print(f'Hello {name}')

greet('wajeh')


# FUNCTION WITH RETURN VALUES

def add(a,b):
    return a + b

result = add(5, 10)
print(result)


# FUNCTION WITH DEFAULT VALUES
def greet(name='wajeh'):
    print(f'hello {name}!')

greet()
greet('my listener')


# POSITIONAL ARGUMENTS
def subtract(a,b):
    return a - b

result1 = subtract(5,10)
result2 = subtract(10,5)

print(f'Result1 is {result1} and Result2 is {result2}')



# KEYWORD ARGUMENTS

def subtract(a,b):
    return a - b

result1 = subtract(a=5,b=10)
result2 = subtract(b=10,a=5)

print(f'Result1 is {result1} and Result2 is {result2}')


#  Variable length arguments
def number_of_items(*items, **details):
    print(f'Name of items')
    for item in items:
        print(f' - {item}')
    print('Order details')
    for key, value in details.items():
        print(f'{key}: {value}')




number_of_items('apple', 'banana', 'orange', 'kiwi', name='wajeh', adress='not provided')

