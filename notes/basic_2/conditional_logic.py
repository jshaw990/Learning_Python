# conditional logic

is_logged_in = True
is_active = False

if is_logged_in and is_active:
    print('You are logged in')
elif is_logged_in:
    print('You are logged in, but not the active user')
else: # catch all
    print('You are not logged in')

