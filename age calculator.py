print('What is your name?')
name = input('>')
name = name.title()
name = name.strip()
print('Well hello there',name)

print('How old are you',name+'?')
years = input('>')
years = int(years)
days_old = years * 365.242
#print('you are about' + str(days_old) + ' days old.')
print('{}, You are about {} days old.' .format(name,days_old))



