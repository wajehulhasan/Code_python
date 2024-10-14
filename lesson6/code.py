# loops syntax
#  for VARIABLE in ITERATOR
        # Body of the code 

    # while condition:
        # Body of the code
shopping_list = ['eggs', 'juice', 'rice','coffee','tea', 'milk']
for item in shopping_list:
    print(item)

name = 'wajeh ul hasan'

for char in name:
    print(char)

for i in range(0,11):
    print(i)   
for i in range(11):
    print(i)
for i in range(0,11,1):
    print(i)  

# the above three examples are the same with 0 difference
# the syntax of range has 3 parameters START STOP STEPSIZE
# When we donot privide the START it defaults to 0
# When we donot provide the STEPSIZE it defaults to 1


# break 

for item in shopping_list:
    if item == 'tea':
        break 
    print(item) 

print('now we are starting the continue')
# continue 

for item in shopping_list:
    if item == 'tea':
        continue
    print(item) 



# loops continue and break
print('Now we are starting the combination/hybrid')
for i in range(20):
    if i % 2 == 0:
        continue
    if i == 13:
        break
    print(i)

