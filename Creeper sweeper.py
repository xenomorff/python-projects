print('''
welcome to creeper sweeper.

click on a box to find the diamonds but make sure not to find the creepers!
''')
print('How many rows would you like?')
num_rows = input('>')
print(' How many columns?')
num_cols = input('>')
print(num_rows,num_cols)

for count in range(num_cols):
    for count in range(num_rows):
        print('~', end=' ')
    print()
