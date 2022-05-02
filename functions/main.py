# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line


def greet(name):
    return (f'Hello, {name}!')


greet('Bob')


def add(a, b, c):
    sum = a + b + c
    return sum


add(5, 3, 2)


def positive(a):
    if(a > 0):
        return True
    else:
        return False


positive(50)
positive(-50)
positive(0)


def negative(a):
    if(a < 0):
        return True
    else:
        return False


negative(50)
negative(-50)
negative(0)
