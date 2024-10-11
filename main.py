import random
user = input('what is u name?')
age = input('what is your age?')
ask_s = input(f'Hello {user}, age,{age}! please hit enter')

question = ['whats your favorite food?','what if your favorite color?','what is your dream vacation?','favorite pet?','favorite color,']

picker = input(random.choice(question))

print('byee')
