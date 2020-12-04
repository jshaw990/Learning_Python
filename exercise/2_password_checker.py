# password checker

username = input('Enter Username\n')
password = input('Enter Password\n')

password_length = len(password)
password_hash = '*' * password_length

print(f'{username}, your password, {password_hash} is {password_length} letters long')