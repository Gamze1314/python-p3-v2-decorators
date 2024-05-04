# Decorators


# takes a function as an argument
# has inner function defined inside of it
# returns the inner function

def decorator(func):
    def inner_func():
        print("I am an inner function")
        func()  # Call the original function
        print("I am the output that lets you know the function has been called")

    return inner_func  # Return the inner function


def get_called():
    print("I am a function")


# Decorate the get_called function. variables in Python are dynamically typed and can be rebound to different objects.
get_called = decorator(get_called)

# Call the decorated function
get_called()
