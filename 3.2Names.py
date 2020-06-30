names = []
print('Give me a name that you would like to add to the list')
names.append(input())
print('Do you want to add another name? Type \'yes\' if you want to add another names or anything else if you want to stop')
response = input()
while response == 'yes':
    print('Give me a name that you would like to add to the list')
    names.append(input())
    print('Do you want to add another name? Type \'yes\' if you want to add another names or anything else if you want to stop')
    response = input()
names.reverse()
print(names)
      
