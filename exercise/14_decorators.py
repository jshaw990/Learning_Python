# decorators
# create an @authenticated decorator
# that only allows the function to run if user1 valid is set to true

user1 = {
    'name': 'Sara',
    'valid': True
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper

@authenticated
def message_fiends(user):
    print('Message has been sent')

message_fiends(user1)