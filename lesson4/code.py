 # String 
text = 'python is1 easy to learn'
text1 = '''python 
this is line 2
this is line 3'''

print(text)
print(text1)

# String Slicing 
print(text[0:5])
#  0 is included and 5 is excluded
print(len(text))
print((text[5:10]))
print(len(text[5:10]))

# negatiev slicing
print(text[0:-4])
print(text[0:(len(text)-4)])
print(text[0:20])


# String Methods 

a = ' python is super easy to learn and understand'

print(len((a)))

print(a.upper())

print(a.lower())

print(a.capitalize())

print(a.title())

print(a.find('easy'))

print(a.count('is'))

print(a.replace('easy', 'hard'))    

print(a.rstrip('!')) # removes ! from the end of the string

print(a.strip())

#  strings are immutable

a.upper() #
b = a.upper() 
print(b)

print(a.isalnum())
print(a.isdigit())
print(a.isalpha())


test = 'python is super easy to learn and understand'

print(test.isalpha())
